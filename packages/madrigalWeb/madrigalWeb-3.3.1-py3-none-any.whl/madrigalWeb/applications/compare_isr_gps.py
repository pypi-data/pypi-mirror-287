# -*- coding: utf-8 -*-

"""compare_isr_gps.py is a script that accesses Madrigal data to compare ISR electron density profiles with the 
Total Electron Content determined by GPS to calculate plasmaspheric TEC.

$Id: compare_isr_gps.py 7369 2021-04-22 17:55:08Z brideout $
"""

# standard python imports
import os, os.path, sys
import argparse
import datetime

# Millstone imports
import madrigalWeb.madrigalWeb

# constants
url = 'http://cedar.openmadrigal.org'
gpsStartDT = datetime.datetime(1999,1,1)

# define the appropriate kindats for each ISR
kindat_dict = {10:[1800,1801,1802],
               20:[2010,2015,2018,2019,2020,30001,30008,30009,30014,30015],
               21:[2010,2015,2018,2019,2020],
               30:[13300],
               61:[5950,],
               72:[6000,6001,6102,6111,6112,6115,6116,6117,6118,6119,6120,6121,6122,6202,6204,6205,6207,6208,6209,6210,6302,6305,6306,6309,6310,6311,6313,6314,6402,6501,6708,6714,6800,6801],
               74:[6000,6001,6041,6042,6402,6404,6604,6707,6708,6709,6710,6711,6712,6800,6801],
               80:[5501,5502,5503,5504,5505,15525],
               91:[5950,],
               95:[6800,6810,6831]}

# locations of each ISR (lat, lon)
location_dict = {10:[-11.95,-76.87],
               20:[18.345,-66.75],
               21:[18.345,-66.75],
               30:[42.619,-71.49],
               61:[65.130,-147.471],
               72:[69.583,19.21],
               74:[69.6,19.2],
               80:[67.0,-51.0],
               91:[74.73,-94.9],
               95:[78.09,16.02]}


class tec_data:
    def __init__(self, radar_tec, err_radar_tec, gps_tec, err_gps_tec,
                 radar_min_alt, radar_max_alt):
        """__init__ creates a tec_data object
        
        Inputs:
            radar_tec - total TECu between radar_min_alt and radar_max_alt
            err_radar_tec - error in radar_tec
            gps_tec - total TECu as measured by to GPS satellite
            err_gps_tec - error in gps_tec
            radar_min_alt, radar_max_alt - altitude range in km covered by isr radar
        """
        self.radar_tec = float(radar_tec)
        self.err_radar_tec = float(err_radar_tec)
        self.gps_tec = float(gps_tec)
        self.err_gps_tec = float(err_gps_tec)
        self.radar_min_alt = float(radar_min_alt)
        self.radar_max_alt = float(radar_max_alt)
        
    def __str__(self):
        retStr = '%f %f %f %f %f %f' % (self.radar_tec, self.err_radar_tec,
                                        self.gps_tec, self.err_gps_tec,
                                        self.radar_min_alt, self.radar_max_alt)
        return(retStr)
        
        
def get_gps_dict(startDT, endDT, lat, lon,
                 username, email, affiliation):
    """get_gps_dict returns a dict with keys = datetime, value = tuple of TEC, Err TEC
    
    Inputs:
        startDT, endDT - datetime range
        lat, lon - instrument location
        username, email, affiliation - user information
    """
    madWebObj = madrigalWeb.madrigalWeb.MadrigalData('http://cedar.openmadrigal.org')
    exps = madWebObj.getExperiments(8000, startDT.year, startDT.month, startDT.day, 
                                    startDT.hour, startDT.minute, startDT.second, 
                                    endDT.year, endDT.month, endDT.day, 
                                    endDT.hour, endDT.minute, endDT.second)
    exps.sort()
    ret_dict = {}
    filterStr = ' filter=gdlat,%i,%i filter=glon,%i,%i filter=tec,, filter=dtec,, ' % \
        (lat - 1, lat + 1, lon - 1, lon + 1)
    parms = 'year,month,day,bhm,tec,dtec'
    for exp in exps:
        files = madWebObj.getExperimentFiles(exp.id)
        for f in files:
            if f.kindat != 3500:
                continue
            if f.category != 1:
                continue
            data = madWebObj.isprint(f.name, parms, filterStr, username, email, affiliation)
            lines = data.split('\n')
            last_dt = None
            total_tec = 0.0
            total_dtec = 0.0
            count = 0
            for line in lines:
                items = line.split()
                if len(items) < 6:
                    continue
                hour = int(float(items[3]))/100
                minute = int(float(items[3])) % 100
                this_dt = datetime.datetime(int(items[0]), int(items[1]), int(items[2]), 
                                        hour, minute)
                if this_dt != last_dt and not last_dt is None:
                    if count > 0:
                        tec = total_tec / count
                        dtec = total_dtec / count
                        ret_dict[last_dt] = (tec, dtec)
                    total_tec = 0.0
                    total_dtec = 0.0
                    count = 0
                last_dt = this_dt
                total_tec += float(items[4])
                total_dtec += float(items[5])
                count += 1
                
    return(ret_dict)
                
                
def get_gps_at_datetime(dt, gps_dict):
    """get_gps_at_datetime returns a tuple of gps tec, err gps tec at closest time to dt
    from gps_dict (keys = datetime, value = tuple of TEC, Err TEC)
    """
    # first try rounding down to 5 minute interval
    minute = dt.minute
    minute = (minute / 5) * 5
    key_dt = datetime.datetime(dt.year, dt.month, dt.day, dt.hour, minute)
    if gps_dict.has_key(key_dt):
        return(gps_dict[key_dt])
    key_dt += datetime.timedelta(minutes=5)
    if gps_dict.has_key(key_dt):
        return(gps_dict[key_dt])
    return((None, None))
    
        
        
def get_data(filename, instCode, kindat, data_dict, madWebObj,
             gps_dict, username, email, affiliation):
    """get_data populates data_dict with data from filename
    
    Inputs:
        filename - full name of data file
        instCode - instrument code
        kindat - kindate code
        data_dict - key = datetime, value = tec_data object
        madWebObj = madrigalWeb.MadrigalData object
        gps_dict - dict returned by get_gps_dict
        username, email, affiliation - user information
    """
    if instCode == 30:
        parms = 'year,month,day,hour,min,sec,tec,gdalt,ne,dne'
        filterStr = 'filter=tec,, filter=ne,, filter=dne,,'
        data = madWebObj.isprint(filename, parms, filterStr, username, email, affiliation)
        lines = data.split('\n')
        last_dt = None
        last_min = None
        last_max = None
        last_tec = None
        for line in lines:
            items = line.split()
            if len(items) < 10:
                continue
            this_dt = datetime.datetime(int(items[0]), int(items[1]), int(items[2]), 
                                        int(items[3]), int(items[4]), int(items[5]))
            if this_dt != last_dt and not last_dt is None:
                if not None in (last_min, last_max, last_tec):
                    gps_tec, err_gps_tec = get_gps_at_datetime(last_dt, gps_dict)
                    if not gps_tec is None:
                        data = tec_data(last_tec, 0.1, gps_tec, err_gps_tec,
                                        last_min, last_max)
                        data_dict[last_dt] = data
                    last_min = None
                    last_max = None
                    last_tec = None
                
            last_tec = float(items[6])
            gdalt = float(items[7])
            ne = float(items[8])
            dne = float(items[9])
            if ne/dne > 10:
                # count this altitude
                if not last_min is None:
                    if gdalt < last_min:
                        last_min = gdalt
                else:
                    last_min = gdalt
                if not last_max is None:
                    if gdalt > last_max:
                        last_max = gdalt
                else:
                    last_max = gdalt
            last_dt = this_dt
            
        
    else:
        raise ValueError, 'Inst code %i not yet implemented' % (instCode)
        


### main begins here ###
if __name__ == '__main__':

    # command line interface
    parser = argparse.ArgumentParser(description='compare_isr_gps.py is a script that accesses Madrigal data to compare ISR electron density profiles with GPS.')
    parser.add_argument('--startDT', metavar='start datetime string', 
                        help='Start UT datetime in format YYYY-MM-DDTHH:MM:SS - no earlier than 1999-01-01', required=True)
    parser.add_argument('--endDT', metavar='end datetime string', 
                        help='End UT datetime for archiving in format YYYY-MM-DDTHH:MM:SS', required=True)
    parser.add_argument('--instCode', metavar='Inst code for ISR', type=int,
                        help='Codes: 10-Jicamarca, 20-Arecibo linefeed, 21-Arecibo Gregorian, 30-Millstone, 61 Poker Flat, 72-Tromsø UHF, 74-Tromso VHF, 80-Sondrestrom, 91-Resolute Bay, 95-Svalbard', 
                        required=True)
    parser.add_argument('--name', required=True, help='User full name')
    parser.add_argument('--email', required=True, help='User email address')
    parser.add_argument('--affiliation', required=True, help='User affiliation (Use None if none)')
    parser.add_argument('--output', required=True, help='Where to save data as ascii file')
    
    args = parser.parse_args()
    
    # create datetimes
    try:
        startDT = datetime.datetime.strptime(args.startDT, '%Y-%m-%dT%H:%M:%S')
    except:
        print('startDT <%s> not in expected YYYY-MM-DDTHH:MM:SS format' % (args.startDT))
        sys.exit(-1)
    if startDT < gpsStartDT:
        print('startDT must be after %s, not %s' % (str(gpsStartDT), str(startDT)))
        sys.exit(-1)
    try:
        endDT = datetime.datetime.strptime(args.endDT, '%Y-%m-%dT%H:%M:%S')
    except:
        print('endDT <%s> not in expected YYYY-MM-DDTHH:MM:SS format' % (args.endDT))
        sys.exit(-1)
    if startDT >= endDT:
        print('startDT %s must be before endDT %s' % (str(startDT), str(endDT)))
        sys.exit(-1)
        
    data_dict = {} # key = datetime, value = tec_data object
        
    keys = kindat_dict.keys()
    keys.sort()
    if args.instCode not in keys:
        print('inst code %i not in available isr list %s' % (args.instCode, str(keys)))
        sys.exit(-1)
        
    lat, lon = location_dict[args.instCode]
    lat = round(lat)
    lon = round(lon)
    
    madWebObj = madrigalWeb.madrigalWeb.MadrigalData(url)
    
    exps = madWebObj.getExperiments(args.instCode, startDT.year, startDT.month, startDT.day, 
                                    startDT.hour, startDT.minute, startDT.second, 
                                    endDT.year, endDT.month, endDT.day, 
                                    endDT.hour, endDT.minute, endDT.second)
    
    if len(exps) == 0:
        # try non-local website
        exps = madWebObj.getExperiments(args.instCode, startDT.year, startDT.month, startDT.day, 
                                    startDT.hour, startDT.minute, startDT.second, 
                                    endDT.year, endDT.month, endDT.day, 
                                    endDT.hour, endDT.minute, endDT.second, 0)
        
        newUrl = exps[0].madrigalUrl
        madWebObj = None
        madWebObj = madrigalWeb.madrigalWeb.MadrigalData(newUrl)
        exps = madWebObj.getExperiments(args.instCode, startDT.year, startDT.month, startDT.day, 
                                    startDT.hour, startDT.minute, startDT.second, 
                                    endDT.year, endDT.month, endDT.day, 
                                    endDT.hour, endDT.minute, endDT.second)
        
        
        
    
    for exp in exps:
        startDT = datetime.datetime(exp.startyear, exp.startmonth, exp.startday,
                                    exp.starthour, exp.startmin, exp.startsec)
        endDT = datetime.datetime(exp.endyear, exp.endmonth, exp.endday,
                                    exp.endhour, exp.endmin, exp.endsec)
        gps_dict = get_gps_dict(startDT, endDT, lat, lon,
                                args.name, args.email, args.affiliation)
        files = madWebObj.getExperimentFiles(exp.id)
        for f in files:
            if f.kindat not in kindat_dict[args.instCode]:
                continue
            if f.category != 1:
                continue
            get_data(f.name, args.instCode, f.kindat, data_dict, madWebObj,
                     gps_dict, args.name, args.email, args.affiliation)
            
            
    # print all data
    f = open(args.output, 'w')
    f.write('year, month, day, hour, min, sec, radar_tec, err_radar_tec, radar_min_alt, radar_max_alt, gps_tec, err_gps_tec\n')
    keys = data_dict.keys()
    keys.sort()
    for key in keys:
        o = data_dict[key]
        f.write('%i    %i    %i   %i   %i   %i  %6.2f  %6.2f  %6.2f  %6.2f  %6.2f  %6.2f\n' % \
                (key.year, key.month, key.day, key.hour, key.minute, key.second,
                 o.radar_tec, o.err_radar_tec, o.radar_min_alt, o.radar_max_alt,
                 o.gps_tec, o.err_gps_tec))
        
    f.close()
    
    
    
    
    
    