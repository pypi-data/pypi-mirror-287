# -*- coding: utf-8 -*-

"""get_location_tec_data.py returns tec data around a particular location, along with geophysical data.

$Id: get_location_tec_data.py 7369 2021-04-22 17:55:08Z brideout $
"""

# standard python imports
import os, os.path, sys
import argparse
import datetime

# Millstone imports
import madrigalWeb.madrigalWeb

# constants
url = 'http://cedar.openmadrigal.org'
parms = 'year,month,day,hour,min,sec,gdlat,glon,tec,dtec,f10.7,fbar,ap3,ap'

class gps_data:
    def __init__(self, dt, lat, lon, tec, dtec, f107, fbar, ap3, ap):
        """gps_data holds one measurement
        """
        self.dt = dt
        self.lat = float(lat)
        self.lon = float(lon)
        self.tec = float(tec)
        self.dtec = float(dtec)
        self.f107 = float(f107)
        self.fbar = float(fbar)
        self.ap3 = float(ap3)
        self.ap = float(ap)
        
        
def write_data(filename, f, lat, lon, step, sDT, eDT, madWebObj,
               name, email, affiliation):
    """write_data writes all data to f from Madrigal file filename
    
    Inputs:
        filename - Madrigal file with tec data
        f - open file to write to
        lat - center latitude
        lon -center longitude
        step - step size
        sDT - start datetime
        eDT - end datetime
        madWebObj - madrigalWeb.MadrigalData object
        name, email, affiliation - user info
    """
    filterStr = 'date1=%02i/%02i/%04i time1=%02i:%02i:%02i date2=%02i/%02i/%04i time2=%02i:%02i:%02i filter=dtec,, ' % \
        (sDT.month, sDT.day, sDT.year, sDT.hour, sDT.minute, sDT.second,
         eDT.month, eDT.day, eDT.year, eDT.hour, eDT.minute, eDT.second)
    filterStr += ' filter=gdlat,%i,%i ' % (lat - (step-1), lat + (step-1))
    filterStr += ' filter=glon,%i,%i ' % (lon - (step-1), lon + (step-1))
    # make sure geo data all exists
    filterStr += ' filter=f10.7,, filter=fbar,, filter=ap3,, filter=ap,, '
    result = madWebObj.isprint(filename, parms, filterStr, name, email, affiliation)
    if result.find('No records were selected') != -1:
        return
    f.write(result)


### main begins here ###
if __name__ == '__main__':

    # command line interface
    parser = argparse.ArgumentParser(description='get_location_tec_data.py returns tec data around a particular location, along with geophysical data.')
    parser.add_argument('--startDT', metavar='start_YYYY-MM-DDTHH:MM:SS', 
                        help='Start UT datetime in format YYYY-MM-DDTHH:MM:SS', required=True)
    parser.add_argument('--endDT', metavar='end_YYYY-MM-DDTHH:MM:SS', 
                        help='End UT datetime for archiving in format YYYY-MM-DDTHH:MM:SS', required=True)
    parser.add_argument('--lat', required=True, type=int, help='latitude as int between -90 and 90')
    parser.add_argument('--lon', required=True, type=int, help='longitude as int between -180 and 180')
    parser.add_argument('--step', type=int, help='number of steps of one degree around main point to include')
    parser.add_argument('--name', required=True, help='User full name')
    parser.add_argument('--email', required=True, help='User email address')
    parser.add_argument('--affiliation', required=True, help='User affiliation (Use None if none)')
    parser.add_argument('--output', required=True, help='Full path to save data as ascii file')
    
    args = parser.parse_args()
    
    # create datetimes
    try:
        startDT = datetime.datetime.strptime(args.startDT, '%Y-%m-%dT%H:%M:%S')
    except:
        print('startDT <%s> not in expected YYYY-MM-DDTHH:MM:SS format' % (args.startDT))
        sys.exit(-1)
    try:
        endDT = datetime.datetime.strptime(args.endDT, '%Y-%m-%dT%H:%M:%S')
    except:
        print('endDT <%s> not in expected YYYY-MM-DDTHH:MM:SS format' % (args.endDT))
        sys.exit(-1)
    if startDT >= endDT:
        print('startDT %s must be before endDT %s' % (str(startDT), str(endDT)))
        sys.exit(-1)
        
    if args.lat < -90 or args.lat > 90:
        raise ValueError, 'Illegal lat %i - must be between -90 and 90' % (lat)
        
    if args.lon < -180 or args.lon > 180:
        raise ValueError, 'Illegal lon %i - must be between -180 and 180' % (lon)
    
    if args.step < 1:
        raise ValueError, 'Illegal step %i' % (step)
    
    madWebObj = madrigalWeb.madrigalWeb.MadrigalData(url)
    
    exps = madWebObj.getExperiments(8000, startDT.year, startDT.month, startDT.day, 
                                    startDT.hour, startDT.minute, startDT.second, 
                                    endDT.year, endDT.month, endDT.day, 
                                    endDT.hour, endDT.minute, endDT.second)
    
    exps.sort()
    f = open(args.output, 'w')
    f.write('%s\n' % (parms))
    
    for exp in exps:
        files = madWebObj.getExperimentFiles(exp.id)
        for thisFile in files:
            if thisFile.category != 1:
                continue
            write_data(thisFile.name, f, args.lat, args.lon, args.step, 
                       startDT, endDT, madWebObj,
                       args.name, args.email, args.affiliation)
            
        
    f.close()
    
    
    
    
    
    