#!/usr/bin/env python

"""downloadCedarAsciiGps.py downloads all GPS data from the selected days
to the selected directory in Cedar Ascii format

Other formats can be selected by simply changing format name
"""

# $Id: downloadCedarAsciiGps.py 7369 2021-04-22 17:55:08Z brideout $

import os, os.path, sys, gzip
import datetime
import traceback

import madrigalWeb.madrigalWeb

usage = """downloadCedarAsciiGps.py <startDay as YYYY-MM-DD> <endDay as YYYY-MM-DD> <outputDir>
Example: downloadCedarAsciiGps.py 2005-01-01 2005-01-31 /data/gps"""


# constants
format = 'ascii'
user_fullname = 'Guiping Liu'
user_email = 'guiping@ssl.berkeley.edu'
user_affiliation = 'University of California Berkeley'

madrigalUrl = 'http://cedar.openmadrigal.org'

# try to parse arguments
if len(sys.argv) != 4:
    print usage
    sys.exit(-1)
    
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
    traceback.print_exc()
    print 'Problem with dates, must be in form YYYY-MM-DD'
    print usage
    sys.exit(-1)

if sDatetime > eDatetime:
    print 'The end date cannot be before the start date'
    sys.exit(-1)
    
Data_Dir = sys.argv[3]
if not os.access(Data_Dir, os.W_OK):
    print('directory %s not writable' % (Data_Dir))
    sys.exit(-1)


madObj = madrigalWeb.madrigalWeb.MadrigalData(madrigalUrl)

expList = madObj.getExperiments(8000,
                                sDatetime.year,
                                sDatetime.month,
                                sDatetime.day,
                                12,0,0,
                                eDatetime.year,
                                eDatetime.month,
                                eDatetime.day,
                                12,0,0)

# loop through each day
for exp in expList:

    fileList = madObj.getExperimentFiles(exp.id)
    thisFile = fileList[0].name
    outFile = os.path.join(Data_Dir, os.path.basename(thisFile))
    
    print('downloading file %s' % (outFile))
    
    madObj.downloadFile(thisFile, outFile, user_fullname, user_email, user_affiliation, format)
