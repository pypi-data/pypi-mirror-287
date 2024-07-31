# -*- coding: utf-8 -*-

"""downloadOzoneFiles.py will download a series of ozone files for a given time range and instrument

$Id: downloadOzoneFiles.py 6371 2017-12-11 14:16:19Z brideout $
"""

# standard python imports
import argparse
import datetime
import os, os.path, sys
import fnmatch

# Madrigal imports
import madrigalWeb.madrigalWeb

def getData(madWeb, kinst, dt, destDir):
    
    
    exps = madWeb.getExperiments(kinst, dt.year, dt.month, dt.day, 0, 0, 0,
                                 dt.year, dt.month, dt.day, 23, 59, 59)
    
    subdir = exps[0].url
    subdir = subdir[subdir.find('madtoc/') + len('madtoc/'):]
    
    expDir = os.path.join('/opt/madrigal3', subdir)
    
    files = madWeb.listFileTimes(expDir)
    
    for this_file in files:
        basename = os.path.basename(this_file[0])
        if fnmatch.fnmatch(basename, '[0-9]*.s[0-9]*'):
            madWeb.downloadWebFile(this_file[0], os.path.join(destDir, basename))
            print('downloaded %s' % (basename))
            
    

# script begins here
if __name__ == '__main__': 
    
    kinstStr = 'Choose on of the following numbers: 7600:Chelmsford, 7602:Lancaster, 7603:Bridgewater, 7604:UnionC, 7605:Greensboro, 7606:Lynnfield, 7607:Alaska, 7608:Hermanus, 7609:Antarctic, 7610:Sodankylä, 7611:Lancaster2. 7612:Haystack'
    
    parser = argparse.ArgumentParser(description='downloadOzoneFiles.py downloads all ozone files between start and end date for given instrument.')
    parser.add_argument('--kinst', type=int, required=True, help=kinstStr)
    parser.add_argument('--startDT', required=True, help='Only download files after startDT YYYY-MM-DD')
    parser.add_argument('--endDT', required=True, help='Only download files before endDT YYYY-MM-DD')
    parser.add_argument('--dest', required=True, help='Store downloaded files in dest dir')
    
    args = parser.parse_args()
    
    # verify args
            
    args.startDT = datetime.datetime.strptime(args.startDT, '%Y-%m-%d')
    args.endDT = datetime.datetime.strptime(args.endDT, '%Y-%m-%d')
    if not os.access(args.dest, os.W_OK):
        raise IOError('Cannot write to directory %s' % (args.dest))
    
    url = 'http://cedar.openmadrigal.org'
    madWeb = madrigalWeb.madrigalWeb.MadrigalData(url)
    
    if args.kinst not in range(7600, 7613):
        print('kinst must be one of %s' % (str(range(7600, 7613))))
    
    this_dt = args.startDT
    while(True):
        print('working on date %s' % (str(this_dt)))
        getData(madWeb, args.kinst, this_dt, args.dest)
        this_dt += datetime.timedelta(days=1)
        if this_dt > args.endDT:
            break
    