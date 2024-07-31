#!/usr/bin/env python

import sys
import os
import string
import time
import datetime
import traceback
import getopt
import re
import random

import madrigalWeb.madrigalWeb
import madrigal._derive

""" This program implements running a global search, and then
    adding geophysical parameters at delayed times.  It's arguments are the same
    as globalIsprint.py, except for arguments of the form --delay=kp,3
"""

usage = """
        Usage:

        globalIsprintDelayedGeo.py --url=<Madrigal url> --parms=<Madrigal parms> --output=<output file> [options]

        where:

        --url=<Madrigal url> - url to homepage of site to be searched
                                  (ie, http://madrigal.haystack.mit.edu/)
                                  This is required.

        --parms=<Madrigal parms> - a comma delimited string listing the desired Madrigal parameters
                                    in mnemonic form.  (Example: gdalt,dte,te).  Data will be returned
                                    in the same order as given in this string.

        --output=<output file name> - the file name to store the resulting data.

        --user_fullname=<user fullname> - the full user name (probably in quotes unless your name is
                                          Sting or Madonna)

        --user_email=<user email>

        --user_affiliation=<user affiliation> - user affiliation.  Use quotes if it contains spaces.

        and options are:

        --delay=<parameter,hours in the past> - a delayed geophysical parameter to append to the data.  Allowed
            parameters are ap, ap3, f10.7, fbar, kp, dst, bimf, bxgse, bygse, bzgse, bxgsm, bygsm, bzgsm, swden, and
            swspd.  Examples::

                --delay=kp,3 (list kp 3 hours previous to present time)

                --delay=bzgsm,9 (list bzgsm 9 hours previous to present time)

        --startDate=<MM/DD/YYY> - start date to filter experiments before.  Defaults to allow all experiments.

        --endDate=<MM/DD/YYY> - end date to filter experiments after.  Defaults to allow all experiments.

        --inst=<instrument list> - comma separated list of instrument codes or names.  See Madrigal documentation
                                   for this list.  Defaults to allow all instruments. If names are given, the
                                   argument must be enclosed in double quotes.  An asterick will perform matching as
                                   in glob.  Examples::
                                   
                                       --inst=10,30
                                       
                                       --inst="Jicamarca IS Radar,Arecibo*"

        --kindat=<kind of data list> - comma separated list of kind of data codes.  See Madrigal documentation
                                       for this list.  Defaults to allow all kinds of data.  If names are given, the
                                       argument must be enclosed in double quotes.  An asterick will perform matching as
                                       in glob. Examples::
                                   
                                            --kindat=3001,13201
                                        
                                            --kindat="INSCAL Basic Derived Parameters,*efwind*,2001"

        --filter=<[mnemonic] or [mnemonic1,[+-*/]mnemonic2]>,<lower limit1>,<upper limit1>[or<lower limit2>,<upper limit2>...]
                            a filter using any measured or derived Madrigal parameter, or two Madrigal parameters either added,
                            subtracted, multiplied or divided.  Each filter has one or more allowed ranges.  The filter accepts
                            data that is in any allowed range.  If the Madrigal parameter value is missing, the filter will always
                            reject that data.  Multiple filter arguments are allowed on the command line.  To skip either a lower
                            limit or an upper limit, leave it blank.  Examples::

                                filter=ti,500,1000  (Accept when 500 <= Ti <= 1000)

                                filter=gdalt,-,sdwht,0,  (Accept when gdalt > shadowheight - that is, point in direct sunlight)

                                filter=gdalt,200,300,1000,1200 (Accept when 200 <= gdalt <= 300 OR 1000 <= gdalt <= 1200)

        --seasonalStartDate=<MM/DD> - seasonal start date to filter experiments before.  Use this to select only part of the
                                year to collect data.  Defaults to Jan 1.  Example:  --seasonalStartDate=07/01 would only allow
                                experiments after July 1st from each year.

        
        --seasonalEndDate=<MM/DD> - seasonal end date to filter experiments after.  Use this to select only part of the
                                    year to collect data.  Defaults to Dec 31.  Example:  --seasonalEndDate=10/31 would only allow
                                    experiments before Oct 31 of each year.

        --showFiles - if given, show file names.  Default is to not show file names.

        --showSummary - if given, summarize all arguments at the beginning.  Default is to not show summary.
        
        --includeNonDefault - if given, include all files, including history.  Default is to search only default files.

        --missing=<missing string> (defaults to "missing")

        --assumed=<assumed string> (defaults to "assumed")

        --knownbad=<knownbad string> (defaults to "knownbad")

        --verbose - if given, print each file processed info to stdout.  Default is to run silently.
                                    
"""

def lookup(ut1, parm, madServer):
    """lookup will get a single parameter from the Madrigal server
    """
    # convert time since 1950 to time since 1970
    convertTime = 631152000 # number of seconds from 1/1/1950 to 1/1/1970
    timelist = datetime.datetime.utcfromtimestamp(ut1 - convertTime)
    result = madServer.madCalculator(timelist.year,
                                     timelist.month,
                                     timelist.day,
                                     timelist.hour,
                                     timelist.minute,
                                     timelist.second,
                                     0,0,0,0,0,0,0,0,0,
                                     parm)


    return result[0][3] # first three values are lat, lon, alt

# parse command line
arglist = ''
longarglist = ['url=',
               'parms=',
               'output=',
               'user_fullname=',
               'user_email=',
               'user_affiliation=',
               'startDate=',
               'endDate=',
               'inst=',
               'kindat=',
               'filter=',
               'seasonalStartDate=',
               'seasonalEndDate=',
               'showFiles',
               'showSummary',
               'includeNonDefault',
               'missing=',
               'assumed=',
               'knownbad=',
               'verbose',
               'delay=']

optlist, args = getopt.getopt(sys.argv[1:], arglist, longarglist)


# set default values
output = None
timeDelayedParm = []

# build globalIsprint command
globalIsprintCmd = './globalIsprint.py '

# check if none passed in
if len(optlist) == 0:
    print usage
    sys.exit(0)

# set some defaults
startDate = None
endDate = None
user_fullname=None
user_email=None
user_affiliation=None
missing = 'missing'
assumed = 'assumed'
knownbad = 'knownbad'
    

for opt in optlist:
    if opt[0] in ('--url',
                  '--parms',
                  '--startDate',
                  '--user_fullname',
                  '--user_email',
                  '--user_affiliation',
                  '--endDate',
                  '--inst',
                  '--kindat',
                  '--filter',
                  '--seasonalStartDate',
                  '--seasonalEndDate',
                  '--missing',
                  '--assumed',
                  '--knownbad'):
        globalIsprintCmd += opt[0] + '="' + opt[1] + '" '
        if opt[0]  == '--missing':
            missing = opt[1]
        if opt[0]  == '--assumed':
            assumed = opt[1]
        if opt[0]  == '--knownbad':
            knownbad = opt[1]
        if opt[0] == '--url':
            url = opt[1]
        if opt[0] == '--url':
            url = opt[1]
        if opt[0] == '--user_fullname':
            user_fullname = opt[1]
        if opt[0] == '--user_email':
            user_email = opt[1]
        if opt[0] == '--user_affiliation':
            user_affiliation = opt[1]
        if opt[0] == '--endDate':
            endDate = opt[1]
        if opt[0] == '--parms':
            if string.lower(opt[1][0:4]) != 'ut1,':
                print 'first parameter must be ut1'
                sys.exit(-1)
    elif opt[0] in ('--showFiles',
                    '--includeNonDefault',
                    '--showSummary',
                    '--verbose'):
        globalIsprintCmd += opt[0] + ' '
        
    elif opt[0] == '--delay':
        tmpList = string.split(opt[1],',')
        if len(tmpList) != 2:
            raise ValueError, 'Incorrect delay usage.  Must be in form: --delay=kp,4'
        timeDelayedParm.append((string.lower(tmpList[0]), int(tmpList[1])))
        
    elif opt[0] == '--output':
        output = opt[1]
        
    else:
        raise ValueError, 'Illegal option %s\n%s' % (opt[0], usage)

# check that all required arguments passed in
if output == None:
    print '--output argument required - must be a valid, writable file path'
    sys.exit(0)

if user_fullname == None:
    print '--user_fullname argument required - must your name'
    sys.exit(0)

if user_email == None:
    print '--user_email argument required - must your email address'
    sys.exit(0)

if user_affiliation == None:
    print '--user_affiliation argument now required - must your affiliation'
    sys.exit(0)

# the following defines data spacing to speed lookup
geoParmsDict = {'ap': 24,
                'ap3': 3,
                'f10.7': 24,
                'fbar': 24,
                'kp': 3,
                'dst': 1,
                'bimf': 1,
                'bxgse': 1,
                'bygse': 1,
                'bzgse': 1,
                'bxgsm': 1,
                'bygsm': 1,
                'bzgsm': 1,
                'swden': 1,
                'swspd': 1}

# create random temp file
random.seed(time.time())
tmpFile = 'tmp%i.tmp' % (random.randint(1,1000000))
globalIsprintCmd += '--output=%s ' % (tmpFile)


# run globalIsprint.py
os.system(globalIsprintCmd)

if os.access(tmpFile, os.R_OK) == 0:
    print 'globalIsprint.py failed - check error message above'
    sys.exit(-1)

# now - add geophysical parameters from earlier times

print 'Now adding additional parameters to the file...'

# first create dictionaries of data so we only need to look up each parm once
# all dictionaries have key = time in hours since 1/1/1950 / time spacing, value = value as double
for item in timeDelayedParm:
    exec(string.replace(item[0],'.','_') + '_dict = {}')

# create connection to server
madServer = madrigalWeb.madrigalWeb.MadrigalData(url)

# figure out the start and end date
if startDate == None:
    startDate = datetime.datetime(1950,1,1)
else:
    startList = string.split(startDate, '/')
    startDate = datetime.datetime(int(startList[2]),int(startList[0]),int(startList[1]))

if endDate == None:
    endDate = datetime.datetime.today()
else:
    endList = string.split(endDate, '/')
    endDate = datetime.datetime(int(endList[2]),int(endList[0]),int(endList[1]),23,59,59)

convertTime = 631152000 # number of seconds from 1/1/1950 to 1/1/1970

# populate the dict for each delayed item
for parm in timeDelayedParm:
    stepHours = geoParmsDict[parm[0]]
    data = madServer.madTimeCalculator(startDate.year,
                                       startDate.month,
                                       startDate.day,
                                       startDate.hour,
                                       startDate.minute,
                                       startDate.second,
                                       endDate.year,
                                       endDate.month,
                                       endDate.day,
                                       endDate.hour,
                                       endDate.minute,
                                       endDate.second,
                                       stepHours,
                                       parm[0])

    # load list into dictionary
    for result in data:
        timestamp = madrigal._derive.getUtFromDate(int(result[0]),
                                          int(result[1]),
                                          int(result[2]),
                                          int(result[3]),
                                          int(result[4]),
                                          int(result[5]),
                                          0)
        timestamp = int(timestamp/(3600 * stepHours))
        try:
            exec(string.replace(parm[0],'.','_') + '_dict[' + str(timestamp) + '] = ' + str(result[6]) )
        except:
            # handle missing
            exec(string.replace(parm[0],'.','_') + '_dict[' + str(timestamp) + '] = "' + missing + '"' )


# open up the temporary file 
fin = open(tmpFile)
fout = open(output, 'w')
lines = fin.readlines()
fin.close()


# set up initial date as 1/1/1950
timelist_old = datetime.datetime(1950,1,1)

for line in lines:
    words = string.split(line)
    try:
        ut1 = int(words[0])
        fout.write('%s ' % (string.strip(line)))
        # see if this is a new day - if so, print
        timelist_new = datetime.datetime.utcfromtimestamp(ut1 - convertTime)
        if timelist_new.day != timelist_old.day:
            timelist_old = timelist_new
            print 'now working on day %i/%i/%i...' % (timelist_old.month,
                                                      timelist_old.day,
                                                      timelist_old.year)
    except:
        # handle the header line
        fout.write(string.strip(line))
        for item in timeDelayedParm:
            fout.write(' %s-%ihr' % (item[0], item[1]))
        fout.write('\n')
        continue

    # add each delayed parameter
    for item in timeDelayedParm:
        spacing = geoParmsDict[item[0]]
        thisTime = int(ut1  / (3600 * spacing )) - int(item[1]/spacing)
        dictStr = string.replace(item[0],'.','_') + '_dict[' + str(thisTime) + ']'
        try:
            newValue = eval(dictStr)
        except KeyError:
            # need to look up this new value
            newValue = lookup(ut1 - item[1]*3600, item[0], madServer)
            try:
                exec(dictStr + ' = ' + str(newValue))
            except:
	        # newValue might be an error string
                exec(dictStr + ' = "' + missing + '"')

        try:
            fout.write(' %g' % (float(newValue)))
        except:
            fout.write(' %s' % (missing))

    fout.write('\n')

try:
    os.remove(tmpFile)
except:
    pass




