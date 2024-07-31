#!/usr/bin/env python

"""downloadISR.py downloads all ISR data from the selected days

See usage string below
"""

# $Id: downloadISR.py 7369 2021-04-22 17:55:08Z brideout $

import os, os.path, sys, gzip
import datetime
import getopt

import madrigalWeb.madrigalWeb


usage = """python downloadISR.py  --radar=[m,a,s,j] --region=[E,F] --output=filename
[--el=lower,upper] [--az=start,stop] [--mode=[S,A]]
<startDay as YYYY-MM-DD> <endDay as YYYY-MM-DD>
where
    m -> Millstone, a -> Arecibo, s -> Sondrestrom, j -> Jicamarca
    E = E region (below 200 km alt), F = F region (above 200 km alt)
    mode can be selected to be S=single pulse, or A=alternating code, but only for Millstone
    Elevations go from 0 to 90
    Azimuth must be between -180 to 180.  Aways moves clockwise, so
        --az=170,-170 goes from 170 to 180, and -180 to -170.
Example: python downloadISR.py --radar=m --output=/tmp/test.txt --el=80,90 2005-01-01 2005-01-31 """


# constants
user_fullname = 'Takuya Tsugawa'
user_email = 'tsugawa@haystack.mit.edu'
user_affiliation = 'MIT Haystack'

madrigalUrlDict = {'m': (30, 'http://madrigal.haystack.mit.edu'),
                   'a': (20, 'http://madrigal.naic.edu/madrigal/'),
                   's': (80, 'http://isr.sri.com/madrigal/'),
                   'j': (10, 'http://jro1.igp.gob.pe/madrigal/')}

parmStr = 'year,month,day,hour,min,sec,gdalt,gdlat,glon,nel,te,ti,vo,dti,dvo'

# parse command line
arglist = ''
longarglist = ['radar=',
               'region=',
               'el=',
               'az=',
               'output=',
               'mode=']

optlist, args = getopt.getopt(sys.argv[1:], arglist, longarglist)


# set default values
radar = None
lowerEl = 0.0
upperEl = 90.0
lowerAz = -180.0
upperAz = 180.0
region = None
output = None
mode = None

# check if none passed in
if len(optlist) == 0:
    print usage
    sys.exit(0)
    

for opt in optlist:
    if opt[0] == '--radar':
        radar = opt[1].lower()
    elif opt[0] == '--output':
        output = opt[1]
    elif opt[0] == '--mode':
        mode = opt[1].upper()
        if mode not in ('S', 'A'):
            print 'mode must be either S (single-pulse) or A (alternating code)'
            sys.exit(-1)
    elif opt[0] == '--region':
        region = opt[1].upper()
        if region not in ('E', 'F'):
            print 'region must be either E or F'
            sys.exit(-1)
    elif opt[0] == '--el':
        elItems = opt[1].split(',')
        try:
            lowerEl = float(elItems[0])
            upperEl = float(elItems[1])
        except:
            print '--el argument must be in form --el=lowerEl,upperEl'
            sys.exit(-1)
    elif opt[0] == '--az':
        azItems = opt[1].split(',')
        try:
            lowerAz = float(azItems[0])
            upperAz = float(azItems[1])
        except:
            print '--az argument must be in form --az=beginAz,endAz'
            sys.exit(-1)

    else:
        raise ValueError, 'Illegal option %s\n%s' % (opt[0], usage)

# check that all required arguments passed in
if radar == None:
    print '--radar=[m,a,s,j] argument required (m=Millstone,a=Arecibo, s=Sondrestrom, or j=Jicamarca)'
    sys.exit(-1)
if radar not in ('m','a','s','j'):
    print '--radar=[m,a,s,j] argument must be (m=Millstone,a=Arecibo, s=Sondrestrom, or j=Jicamarca)'
    sys.exit(-1)
if region == None:
    print '--region=[E,F] required'
    sys.exit(-1)
if output == None:
    print '--output=filename required'
    sys.exit(-1)
if radar != 'm' and mode != None:
    print '--mode can only be used for Millstone ISR'
    sys.exit(-1)
    
try:
    items = args[0].split('-')
    if len(items) != 3:
        raise ValueError, 'Dates must be in form YYYY-MM-DD, not %s' % (args[0])
    syear = int(items[0])
    smonth = int(items[1])
    sday = int(items[2])
    sDatetime = datetime.datetime(syear, smonth, sday)

    
    items = args[1].split('-')
    if len(items) != 3:
        raise ValueError, 'Dates must be in form YYYY-MM-DD, not %s' % (args[1])
    eyear = int(items[0])
    emonth = int(items[1])
    eday = int(items[2])
    eDatetime = datetime.datetime(eyear, emonth, eday, 23,59,59)

except:
    print 'Problem with dates, must be in form YYYY-MM-DD'
    print usage
    sys.exit(-1)

if sDatetime > eDatetime:
    print 'The end date cannot be before the start date'
    sys.exit(-1)

kinst = madrigalUrlDict[radar][0]
madrigalUrl = madrigalUrlDict[radar][1]


madObj = madrigalWeb.madrigalWeb.MadrigalData(madrigalUrl)

expList = madObj.getExperiments(kinst,
                                sDatetime.year,
                                sDatetime.month,
                                sDatetime.day,
                                sDatetime.hour,
                                sDatetime.minute,
                                sDatetime.second,
                                eDatetime.year,
                                eDatetime.month,
                                eDatetime.day,
                                eDatetime.hour,
                                eDatetime.minute,
                                eDatetime.second)

outFile = open(output, 'w')
outFile.write('%s\n' % (parmStr))

# loop through each day
for exp in expList:
    expStartDatetime = datetime.datetime(exp.startyear,
                                         exp.startmonth,
                                         exp.startday,
                                         exp.starthour,
                                         exp.startmin,
                                         exp.startsec)
    expEndDatetime = datetime.datetime(exp.endyear,
                                       exp.endmonth,
                                       exp.endday,
                                       exp.endhour,
                                       exp.endmin,
                                       exp.endsec)

    fileList = madObj.getExperimentFiles(exp.id)
    # see if its realtime
    if fileList[0].category == 4 and radar == 'm':
        # choose the right realtime file
        thisFile = fileList[0].name # just in case not found
        for testFile in fileList:
            if region == 'E' and (mode == 'A' or mode == None) and testFile.name.find('b.000') != -1:
                thisFile = testFile.name
                break
            elif region == 'E' and mode == 'S' and testFile.name.find('a.000') != -1:
                thisFile = testFile.name
                break
            elif region == 'F' and (mode == 'S' or mode == None) and testFile.name.find('a.000') != -1:
                thisFile = testFile.name
                break
            elif region == 'F' and mode == 'A' and testFile.name.find('c.000') != -1:
                thisFile = testFile.name
                break
    else:
        thisFile = fileList[0].name

    # download all the days found here
    while expStartDatetime < eDatetime  and \
          expEndDatetime  > sDatetime and \
          sDatetime < eDatetime:
    
        print 'Downloading ISR %s region data for %i-%02i-%02i' % (region,
                                                                   sDatetime.year,
                                                                   sDatetime.month,
                                                                   sDatetime.day)
        
        # create filter string
        filterStr = ' date1=%i/%i/%i time1=00:00:00 date2=%i/%i/%i time2=23:59:59 ' % (sDatetime.month,
                                                                                       sDatetime.day,
                                                                                       sDatetime.year,
                                                                                       sDatetime.month,
                                                                                       sDatetime.day,
                                                                                       sDatetime.year)
        if lowerAz <= upperAz:
            secFilterStr = ' el=%f,%f az=%f,%f ' % (lowerEl, upperEl, lowerAz, upperAz)
        else:
            secFilterStr = ' el=%f,%f az=%f,180.0or-180.0,%f ' % (lowerEl, upperEl, lowerAz, upperAz)
        filterStr += secFilterStr

        # handle millstone and other radars differently (Millstone may have mode != None)
        if region == 'E' and mode == 'A':
            thirdFilterStr = ' filter=gdalt,,200.0 filter=mdtyp,96.9,97.1 '
        elif region == 'E' and mode == 'S':
            thirdFilterStr = ' filter=gdalt,,200.0 filter=mdtyp,114.9,115.1 '
        elif region == 'E':
            thirdFilterStr = ' filter=gdalt,,200.0 '
        elif region == 'F' and mode == 'S':
            thirdFilterStr = ' filter=gdalt,200.0, filter=mdtyp,114.9,115.1 '
        elif region == 'F' and mode == 'A':
            thirdFilterStr = ' filter=gdalt,200.0, filter=mdtyp,96.9,97.1 '
        elif region == 'F':
            thirdFilterStr = ' filter=gdalt,200.0, '
        filterStr += thirdFilterStr
        
        result = madObj.isprint(thisFile, parmStr, filterStr,
                                user_fullname, user_email, user_affiliation)

        result = result.replace('missing', 'NaN    ')

        if len(result) > 10000:   
            outFile.write(result)
        else:
            print 'No data in for day %s' % (str(sDatetime))

        sDatetime = sDatetime + datetime.timedelta(1)

        
