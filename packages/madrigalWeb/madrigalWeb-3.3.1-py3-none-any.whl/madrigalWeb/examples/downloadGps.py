#!/usr/bin/env python


# $Id: downloadGps.py 7369 2021-04-22 17:55:08Z brideout $

import os, os.path, sys, gzip
import datetime

import madrigalWeb.madrigalWeb


usage = """downloadGps.py <startDay as YYYY-MM-DD> <endDay as YYYY-MM-DD> <dataDir> <name> <email> <institution>
Example: 
downloadGps.py 2005-01-01 2005-01-31 /data/gps 'Bill Rideout' 'brideout@haystack.mit.edu' 'MIT'

Files have the following columns: year,month,day,hour,min,sec,gdlat,glon,tec,dtec"""

if len(sys.argv) != 7:
    print(usage)
    print('wrong number of arguments')
    sys.exit()


Data_Dir = sys.argv[3]
user_fullname = sys.argv[4]
user_email = sys.argv[5]
user_affiliation = sys.argv[6]

try:
    os.makedirs(Data_Dir)
except:
    pass

if not os.access(Data_Dir, os.R_OK):
    raise IOError, 'unable to create directory %s' % (Data_Dir)


madrigalUrl = 'http://cedar.openmadrigal.org'
parmStr = 'year,month,day,hour,min,sec,gdlat,glon,tec,dtec'
    
try:
    items = sys.argv[1].split('-')
    if len(items) != 3:
        raise ValueError, 'Dates must be in form YYYY-MM-DD, not %s' % (sys.argv[1])
    syear = int(items[0])
    smonth = int(items[1])
    sday = int(items[2])
    sDatetime = datetime.datetime(syear, smonth, sday)

    
    items = sys.argv[2].split('-')
    if len(items) != 3:
        raise ValueError, 'Dates must be in form YYYY-MM-DD, not %s' % (sys.argv[2])
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


madObj = madrigalWeb.madrigalWeb.MadrigalData(madrigalUrl)

expList = madObj.getExperiments(8000,
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
    thisFile = fileList[0].name

    # download all the days found here
    while expStartDatetime < sDatetime + datetime.timedelta(0, 3600*12) and \
          sDatetime + datetime.timedelta(0, 3600*12) < expEndDatetime and \
          sDatetime + datetime.timedelta(0, 3600*12) < eDatetime:
    
        print 'Downloading TEC data for %i-%02i-%02i' % (sDatetime.year,
                                                         sDatetime.month,
                                                         sDatetime.day)
        
        
        # open output file
        outFilename = os.path.join(Data_Dir, 'Tec_%04i_%02i_%02i.txt' % (sDatetime.year,
                                                                        sDatetime.month,
                                                                        sDatetime.day))
        
        # create filter string
        filterStr = ' date1=%i/%i/%i time1=00:00:00 date2=%i/%i/%i time2=23:59:59 ' % (sDatetime.month,
                                                                                       sDatetime.day,
                                                                                       sDatetime.year,
                                                                                       sDatetime.month,
                                                                                       sDatetime.day,
                                                                                       sDatetime.year)

        result = madObj.isprint(thisFile, parmStr, filterStr,
                                user_fullname, user_email, user_affiliation)

        if len(result) > 10000:
            outFile = open(outFilename, 'w')
            outFile.write(result)
            outFile.close()
        else:
            print 'No data in filename %s' % (outFilename)

        sDatetime = sDatetime + datetime.timedelta(1)
