import os,sys,os.path
import time


import madrigalWeb.madrigalWeb

"""realTimeMadrigal.py is a demonstration script that shows how real-time data
can be imported from any Madrigal site that is updated on a real-time basis.

In this example, data is imported from http://madrigal.haystack.mit.edu from
"Millstone Hill IS Radar".  The following Madrigal parameters are retrieved:

year,month,day,hour,min,sec,gdlat,glon,gdalt,az,el,vo,dvo

for all records from the past 15 minutes.

Although the particular Madrigal site (http://madrigal.haystack.mit.edu), the
instrument ("Millstone Hill IS Radar"), the parameters, and the times are
hard-coded in this example, they could be easily be modified to be arguments.

To avoid missing data, we choose one parameter to be the filter parameter: vo

To run this script requires the python Madrigal API be installed, which can be
downloaded from http://cedar.openmadrigal.org/madrigalDownload/"""

# $Id: realTimeMadrigal.py 7369 2021-04-22 17:55:08Z brideout $

#constants
madrigalUrl = 'http://madrigal.haystack.mit.edu'
instrument = 'Millstone Hill IS Radar'

user_fullname = 'Put your name here!!!'
user_email = 'your@email.here'
user_affiliation = 'Put your affiliation here!!!'


# each line of data contains the following parameters
params = 'year,month,day,hour,min,sec,gdlat,glon,gdalt,azm,elm,vo,dvo'
filterParm = 'vo'
timeDelay = 15

# create the main object to get all needed info from Madrigal
madrigalObj = madrigalWeb.madrigalWeb.MadrigalData(madrigalUrl)

# these next few lines convert instrument name to code
code = None
instList = madrigalObj.getAllInstruments()
for inst in instList:
    if inst.name.lower() == instrument.lower():
        code = inst.code
        break

if code == None:
    raise ValueError, 'Unknown instrument %s' % (instrument)

# next, get a list of real time experiments in the last timeDelay minutes
startTime = time.gmtime(time.time() - timeDelay*60.0)
endTime = time.gmtime(time.time())


try:
    expList = madrigalObj.getExperiments(code, startTime[0],
                                     startTime[1],
                                     startTime[2],
                                     startTime[3],
                                     startTime[4],
                                     startTime[5],
                                     endTime[0],
                                     endTime[1],
                                     endTime[2],
                                     endTime[3],
                                     endTime[4],
                                     endTime[5])

except:
    raise ValueError, 'No realtime experiments found'

# assume there's only one realtime experiment, and get the file names
fileList = madrigalObj.getExperimentFiles(expList[0].id)

if len(fileList) == 0:
    raise ValueError, 'No realtime experiment files found'


# get data from each of the files
startDateStr = time.strftime('%m/%d/%Y', startTime)
startDateStr = ' date1=' + startDateStr
startTimeStr = time.strftime('%H:%M:%S', startTime)
startTimeStr = ' time1=' + startTimeStr
endDateStr = time.strftime('%m/%d/%Y', endTime)
endDateStr = ' date2=' + endDateStr
endTimeStr = time.strftime('%H:%M:%S', endTime)
endTimeStr = ' time2=' + endTimeStr

filterString = 'filter=%s,-1E30,1E30' % (filterParm) + startDateStr + startTimeStr + endDateStr + endTimeStr
for dataFile in fileList:
    result = madrigalObj.isprint(dataFile.name, params, filterString,
                                 user_fullname, user_email, user_affiliation)
    # make sure it succeeded
    if result.find('No records were selected') != -1:
        continue
    if result.find('****') != -1:
        continue
    print result



