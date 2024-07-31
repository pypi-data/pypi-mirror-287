"""downloadTecMapsMovies.py is a python script that will download all
TEC maps and movies for a set time range

$Id: downloadTecMapsMovies.py 7375 2021-04-28 13:56:35Z brideout $
"""

# standard python imports
import os, sys, os.path
import argparse
import datetime

# Madrigal imports (pip install madrrigalWeb)
import madrigalWeb.madrigalWeb

# constants
url = 'http://cedar.openmadrigal.org'
gpsStartDT = datetime.datetime(1999,1,1)
kinst = 8000


def gatherFiles(startDT, endDT, output):
    """gatherFiles is the main function that gathers all TEC files
    
    Inputs:
        startDT, endDT - start and end datetimes
        output - directory to write data into.  Each day will create a subdirectory
            in output in form YYYY-MM-DD
    """
    madWebObj = madrigalWeb.madrigalWeb.MadrigalData(url)
    expList = madWebObj.getExperiments(kinst, startDT.year, startDT.month, startDT.day, 0, 0, 1, endDT.year, endDT.month, endDT.day, 1, 0, 0)
    expList.sort()
    for exp in expList:
        thisDT = datetime.datetime(exp.startyear, exp.startmonth, exp.startday)
        destDir = os.path.join(output, thisDT.strftime('%Y-%m-%d'))
        if not os.access(destDir, os.W_OK):
            os.mkdir(destDir)
        madFiles = madWebObj.getExperimentFiles(exp.id)
        expDir = os.path.dirname(madFiles[0].name)
        imageDir = os.path.join(expDir, 'images')
        imageFiles = madWebObj.listFileTimes(imageDir)
        for filename, filedate in imageFiles:
            madWebObj.downloadWebFile(filename, os.path.join(destDir, os.path.basename(filename)))
            print('downloaded %s' % (filename))


### main begins here ###
if __name__ == '__main__':

    # command line interface
    parser = argparse.ArgumentParser(description='downloadTecMapsMovies.py is a python script that will download all TEC maps and movies for a set time range')
    parser.add_argument('--start', metavar='start date string', 
                        help='Start date in format YYYY-MM-DD - no earlier than 1999-01-01', required=True)
    parser.add_argument('--end', metavar='end date string', 
                        help='End date in format YYYY-MM-DD', required=True)
    parser.add_argument('--output', required=True, help='Directory to save files in')
    
    args = parser.parse_args()
    
    # create datetimes
    try:
        startDT = datetime.datetime.strptime(args.start, '%Y-%m-%d')
    except:
        print('start <%s> not in expected YYYY-MM-DD format' % (args.start))
        sys.exit(-1)
    if startDT < gpsStartDT:
        print('start must be after %s, not %s' % (str(gpsStartDT), str(startDT)))
        sys.exit(-1)
    try:
        endDT = datetime.datetime.strptime(args.end, '%Y-%m-%d')
    except:
        print('end <%s> not in expected YYYY-MM-DD' % (args.end))
        sys.exit(-1)
    if startDT >= endDT:
        print('start %s must be before end %s' % (str(startDT), str(endDT)))
        sys.exit(-1)
        
    if not os.path.isdir(args.output):
        print('output %s must be a directory' % (args.output)) 
        sys.exit(-1)
    if not os.access(args.output, os.W_OK):
        print('output %s must be writable' % (args.output)) 
        sys.exit(-1)
        
    gatherFiles(startDT, endDT, args.output)
        