"""plotSatelliteScans.py is a script defined by Phil Erickson to create plots for experiments
with scans to map to satellite passes.

$Id: plotSatelliteScans.py 7369 2021-04-22 17:55:08Z brideout $
"""


# standard python imports
import os, os.path, sys
import argparse
import datetime

# third party imports
import numpy
import matplotlib.pyplot
import matplotlib.lines

# Millstone imports
import madrigalWeb.madrigalWeb


def createPlots(expId, dest, alt, startDT, endDT, madWebObj):
    """createPlots creates plots for a single Madrigal experiment
    
    Inputs:
        expId - experiment id
        dest - Path to directory to store plots in
        alt - Alt in km at which to plot values
        startDT -  Start UT datetime for plotting. Used when not all scans in exp desired
        endDT - End UT datetime for plotting. Used when not all scans in exp desired
        madWebObj - madrigalWeb.madrigalWeb.MadrigalData to fetch data
    """
    misaFile = None
    vectorFile = None
    madFiles = madWebObj.getExperimentFiles(expId)
    for madFile in madFiles:
        if madFile.category != 1:
            continue
        if madFile.kindat == 3430:
            misaFile = madFile.name
        elif madFile.kindat == 13305:
            vectorFile = madFile.name
            
    if misaFile is None:
        raise ValueError, 'No misa single pulse file found for exp id %i' % (expId)
    
    if vectorFile is None:
        raise ValueError, 'No vector file found for exp id %i' % (expId)
    
    dt_vector, ePe, ePn = getVectorData(vectorFile, alt, madWebObj)
    
    scanIterator = ScanIterator(misaFile, alt, madWebObj)
    
    for dt, invlat, ne, te, ti in scanIterator:
        # only create plots in time period
        if dt < startDT or dt > endDT:
            continue
        print(dt)
        plotOneScan(dt, invlat, ne, te, ti, dt_vector, ePe, ePn, dest)
        
    print('plotting complete')
    
    
def plotOneScan(dt, invlat, ne, te, ti, dt_vector, ePe, ePn, dest):
    """plotOneScan creates a single plot of one scan at datetime dt
    
    Inputs:
        dt - datetime at beginning of this scan
        invlat - array or invlats of the scan data at given alt
        ne - array or invlats of the scan data at given alt
        te
        ti
        dt_vector
        ePe
        ePn
        dest
    """
    f, ((ax1, ax2), (ax3, ax4)) = matplotlib.pyplot.subplots(2, 2)
    ax1.scatter(invlat, ne)
    ax1.set_title('Ne')
    ax1.set_xlabel('Inv lat')
    ax1.set_ylabel('Ne (m^-3)')
    ax1.grid()
    
    ax2.scatter(invlat, te)
    ax2.set_title('Te')
    ax2.set_xlabel('Inv lat')
    ax2.set_ylabel('Elect temp (k)')
    ax2.grid()
    
    ax3.scatter(invlat, ti)
    ax3.set_title('Ti')
    ax3.set_xlabel('Inv lat')
    ax3.set_ylabel('Ion temp (k)')
    ax3.grid()
    
    ax4.scatter(dt_vector, ePe, label="E", color='r')
    ax4.scatter(dt_vector, ePn, label="N", color='b')
    # find y limits
    arr = numpy.array(ePe + ePn)
    maxValue = numpy.max(numpy.abs(arr))
    steps = int(maxValue/0.002) + 1
    ax4.set_title('E field during exp')
    ax4.set_xlabel('UT time')
    ax4.set_xlim((startDT, endDT))
    ax4.set_ylim((steps*(-0.002), steps*(0.002)))
    midDT = startDT + (endDT-startDT)/2
    ax4.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%H:%M'))
    ax4.set_xticks((startDT, midDT, endDT),)
    ax4.set_ylabel('Electric field at 350 km')
    ax4.legend(fontsize=8)
    # add line and label
    ymin, ymax = ax4.get_ylim()
    l = matplotlib.lines.Line2D([dt,dt], [ymin,ymax])
    ax4.add_line(l)
    # figure out where to put the label
    if dt - startDT < endDT - dt:
        xposition = dt + datetime.timedelta(minutes=10)
    else:
        xposition = dt - datetime.timedelta(minutes=40)
    ax4.text(xposition, ymin + (ymax-ymin)*0.3, dt.strftime('%H:%M'))
    ax4.grid()
    
    
    
    
    
    f.suptitle('Scan data at %s' % (dt.strftime('%Y-%m-%d %H:%M:%S')))
    matplotlib.pyplot.tight_layout()
    matplotlib.pyplot.savefig(os.path.join(dest, 'scan_%s.png' % (dt.strftime('%Y_%m_%d_%H_%M_%S'))))
    
    
    
    
class ScanIterator:
    """ScanIterator returns a tuple of (dt, invlat, ne, te, ti)
    with each iteration
    """
    def __init__(self, misaFile, alt, madWebObj):
        """
        misaFile - full path to file with misa single pulse data
        alt - Alt in km at which to plot values
        madWebObj - madrigalWeb.madrigalWeb.MadrigalData to fetch data
        """
        parms = 'year,month,day,hour,min,sec,gdalt,scntyp,invlat,ne,te,ti,azm'
        filter = 'filter=ne,, filter=te,, filter=ti,, filter=gdalt,%f,%f' % (alt-20.0, alt + 20.0)
        data = madWebObj.isprint(misaFile, parms, filter, 'Phil Erickson', 'pje@mit.edu', 'MIT')
        self.lines = data.split('\n')
        self.position = 0
        self.alt = float(alt)
    

    def __iter__(self):
        return(self)

    def next(self):
        dt = None
        invlat = []
        ne = []
        te = []
        ti = []
        inScan = False
        while(True):
            if self.position >= len(self.lines):
                if dt is None:
                    raise StopIteration
                else:
                    self.position += 1
                    return((dt, invlat, ne, te, ti))
                
            items = self.lines[self.position].split()
            if len(items) < 13:
                self.position += 1
                continue
            scntyp = float(int(items[7]))
            if scntyp != 2 and not inScan:
                # scan not found yet
                self.position += 1
                continue
            elif scntyp == 2 and not inScan:
                inScan = True
                dtList = [int(float(value)) for value in items[:6]]
                dt = datetime.datetime(*dtList)
            elif scntyp != 2 and inScan:
                # scan complete - return data
                self.position += 1
                return((dt, invlat, ne, te, ti))
            # if we gor here, there is more scan data to add
            azm = float(items[12])
            found = False # we only take one point, marked true when right gdalt found
            while(True):
                # this loop walks through all gdalts until new time found
                this_azm = float(items[12])
                if this_azm != azm:
                    # new position
                    break
                if not found:
                    this_gdalt = float(items[6])
                    if this_gdalt >= self.alt:
                        # this is the gdalt we want
                        invlat.append(float(items[8]))
                        ne.append(float(items[9]))
                        te.append(float(items[10]))
                        ti.append(float(items[11]))
                # move to next line
                self.position += 1
                if self.position >= len(self.lines):
                    return((dt, invlat, ne, te, ti))
                items = self.lines[self.position].split()
                
                
    
    
    
    
def getVectorData(vectorFile, alt, madWebObj):
    """getVectorData returns a tuple of three arrays of equal 1D length: dt, e field perp E, E field perp n
    """
    parms = 'year,month,day,hour,min,sec,epe,epn'
    filter = 'filter=epe,, filter=epn,, filter=gdalt,%f,%f' % (alt-20, alt+20)
    data = madWebObj.isprint(vectorFile, parms, filter, 'Phil Erickson', 'pje@mit.edu', 'MIT')
    dt_vector = [] 
    perpEVel = [] 
    perpNVel = []
    lines = data.split('\n')
    lastDT = None
    vipeList = []
    vipnList = []
    for line in lines:
        items = line.split()
        if len(items) < 8:
            continue
        dtList = [int(items[i]) for i in range(6)]
        dt = datetime.datetime(*dtList)
        if dt != lastDT and not lastDT is None:
            vipe = numpy.array(vipeList)
            vipn = numpy.array(vipnList)
            perpEVel.append(numpy.mean(vipe))
            perpNVel.append(numpy.mean(vipn))
            dt_vector.append(lastDT)
            lastDT = dt
            vipeList = []
            vipnList = []
        elif lastDT is None:
            lastDT = dt
        vipeList.append(float(items[6]))
        vipnList.append(float(items[7]))
        
    # add last point
    vipe = numpy.array(vipeList)
    vipn = numpy.array(vipnList)
    perpEVel.append(numpy.mean(vipe))
    perpNVel.append(numpy.mean(vipn))
    dt_vector.append(lastDT)
        
    return((dt_vector, perpEVel, perpNVel))
        
            
    



### main begins here ###
if __name__ == '__main__':

    # command line interface
    parser = argparse.ArgumentParser(description='plotSatelliteScans.py is a script to create plots for experiments with scans to map to satellite passes.')
    parser.add_argument('--startDT', metavar='start datetime string', 
                        help='Start UT datetime for plotting in format YYYY-MM-DDTHH:MM:SS', required=True)
    parser.add_argument('--endDT', metavar='end datetime string', 
                        help='End UT datetime for plotting in format YYYY-MM-DDTHH:MM:SS', required=True)
    parser.add_argument('--dest', metavar='Path to directory to store plots in', 
                        default='/data0/results/plasma_line_metadata')
    parser.add_argument('--alt', metavar='Alt in km at which to plot values', 
                        default=350)
    
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
        
    if not os.access(args.dest, os.R_OK):
        raise IOError, 'dest directory %s does not exist' % (args.dest)
    
    madWebObj = madrigalWeb.madrigalWeb.MadrigalData('http://madrigal.haystack.mit.edu')
    
    exps = madWebObj.getExperiments(30, startDT.year, startDT.month, startDT.day, startDT.hour, startDT.minute, startDT.second,
                                    endDT.year, endDT.month, endDT.day, endDT.hour, endDT.minute, endDT.second)
    
    exps.sort()
    
    
    for exp in exps:
        if exp.name.find('Alternate processing') != -1:
            # skip USRP
            continue
        expId = exp.id
        createPlots(expId, args.dest, args.alt, startDT, endDT, madWebObj)
        