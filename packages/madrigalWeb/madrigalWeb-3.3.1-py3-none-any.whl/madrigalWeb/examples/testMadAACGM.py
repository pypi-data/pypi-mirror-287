"""testConversion to and from AACGM coords

$Id: testMadAACGM.py 3304 2011-01-17 15:25:59Z brideout $
"""
import os, os.path, sys

import madrigal.cedar
import madrigal.metadata

madDB = madrigal.metadata.MadrigalDB()
madroot = madDB.getMadroot()

gdlat = 42.54
glon = -71.49
gdalt = 240.53
paclat = 53.57
paclon = 5.91  


# create a cedar file with 1D parms paclat, paclon, and gdalt
tmpFile = '/tmp/cedar.test'
cedarObj = madrigal.cedar.MadrigalCedarFile(tmpFile, True)
dataRec = madrigal.cedar.MadrigalDataRecord(31, 3410, 
                                            2000,1,1,0,0,0,0,
                                            2000,1,1,0,5,0,0,
                                            ['paclat', 'paclon', 'gdalt'],[],0)

dataRec.set1D('paclat', paclat)
dataRec.set1D('paclon', paclon)
dataRec.set1D('gdalt', gdalt)
cedarObj.append(dataRec)
cedarObj.write()

# now run isprint versus tmp file
cmd = '%s/bin/isprint file=%s gdlat glon gdalt paclat paclon' % (madroot, tmpFile)
os.system(cmd)

os.remove(tmpFile)