"""runCalcMultipleTimes.py is an example script that shows how to efficiently call 
madCalculator for multiple time.

$Id: runCalcMultipleTimes.py 7369 2021-04-22 17:55:08Z brideout $
"""

import os, os.path, sys
import datetime

import madrigalWeb.madrigalWeb

"""The following hard-coded arguments are choosen to get MSIS atomic oxygen at 400 km directly
over Millstone Hill at noon local time from Mar 1, 1996 to Dec 31, 2008
"""

startDate = datetime.datetime(1996,3,1,0,0,0)
endDate = datetime.datetime(2008,12,31,0,0,0)
parms = 'NOL' # log of neutral atomic oxygen
lat = [42.619]
lon = [-71.49]
alt = [400.0]
ltOffset = datetime.timedelta(hours=288.51/15.0)
stepTime = datetime.timedelta(hours=24.0)


# the following are the arguments to madCalculator3
yearList = []
monthList = []
dayList = []
hourList = []
minList = []
secList = []
latList = []
lonList = []
altList = []

# fill out list
thisDate = startDate + ltOffset
while thisDate < endDate:
    yearList.append(thisDate.year)
    monthList.append(thisDate.month)
    dayList.append(thisDate.day)
    hourList.append(thisDate.hour)
    minList.append(thisDate.minute)
    secList.append(thisDate.second)
    latList.append(lat)
    lonList.append(lon)
    altList.append(alt)
    thisDate += stepTime
    
# information only
print('about to call madCalculator3 for %i separate times' % (len(yearList)))
    
# connect to Madrigal
madWeb = madrigalWeb.madrigalWeb.MadrigalData('http://madrigal.haystack.mit.edu')

result = madWeb.madCalculator3 (yearList, monthList, dayList, hourList, minList, secList,
                                latList, lonList, altList, parms)

# print out each line
for data in result:
    print(data)





