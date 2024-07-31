"""demoMadrigalWebServices.py runs a test of the Madrigal Web Services interface
   for the Haystack madrigal server.  It produces interactive prompts on the terminal,
   and prints out sample data.

   usage:

   python demoMadrigalWebServices.py 

   Assumes the basic Madrigal test files have been installed.

"""

# $Id: demoMadrigalWebServices.py 7369 2021-04-22 17:55:08Z brideout $

import madrigalWeb.madrigalWeb
import sys
import string
import difflib


# constants
user_fullname = 'Bill Rideout - automated test'
user_email = 'brideout@haystack.mit.edu'
user_affiliation = 'MIT Haystack'

print 'The first step is to connect to a Madrigal server:'
print '\tmadConn = madrigalWeb.madrigalWeb.MadrigalData("http://madrigal.haystack.mit.edu")'
print ''

madConn = madrigalWeb.madrigalWeb.MadrigalData("http://madrigal.haystack.mit.edu")

reply = raw_input('')

print 'The next step could be to ask for which instruments are available.'
print 'Each instrument is a python object:'
print '\tinstList = madConn.getAllInstruments()'

instList = madConn.getAllInstruments()

reply = raw_input('')

print 'Print the first instrument: instList[0]\n'

reply = raw_input('')

print instList[0]

reply = raw_input('')

print 'Next get a list of all experiments for Millstone Hill Radar in January 1998:'
print "\texpList = madConn.getExperiments(30, 1998,1,1,0,0,0,1998,1,31,0,0,0)"
        
expList = madConn.getExperiments(30, 1998,1,1,0,0,0,1998,1,31,0,0,0)

reply = raw_input('')

print 'Print the first experiment: expList[0]\n'

reply = raw_input('')

print expList[0]

reply = raw_input('')

print 'Since this is a local experiment, you can use the present madConn to get a list of all files in that experiment:'
print '\tmadConn.getExperimentFiles(expList[0].id)'

fileList = madConn.getExperimentFiles(expList[0].id)

reply = raw_input('')

print 'Print the first file: fileList[0]\n'

reply = raw_input('')

print fileList[0]

reply = raw_input('')

print 'To simply print this file call simplePrint:'
print '\tresult = madConn.simplePrint(fileList[0].name, user_fullname, user_email, user_affiliation)'
result = madConn.simplePrint(fileList[0].name, user_fullname, user_email, user_affiliation)

reply = raw_input('')

print 'Print first 2000 characters of the result:'

reply = raw_input('')

print result[:2000]

reply = raw_input('')

print 'To simply download this file in simple ascii or other format, call downloadFile:'
print '\tresult = madConn.downloadFile(fileList[0].name, "/tmp/test.txt", user_fullname, user_email, user_affiliation, "simple")'
result = madConn.downloadFile(fileList[0].name, "/tmp/test.txt", 
                              user_fullname, user_email, user_affiliation, "simple")
print('Download complete')

reply = raw_input('')

print 'If you want to choose which parameters to print, including what derived parameters might be available, ' + \
    'we want to know what measured parameters are in that file, and what derived parameters are available:'
print '\tparmList = madConn.getExperimentFileParameters(fileList[0].name)'
parmList = madConn.getExperimentFileParameters(fileList[0].name)

reply = raw_input('')

print 'Print the first parameter: parmList[0]\n'

reply = raw_input('')

print parmList[0]

reply = raw_input('')

print 'Finally, print out some data from that file using selected parameters and filters:'

print "\tresult = madConn.isprint(fileList[0].name, 'gdalt,ti','filter=recno,0,4 filter=ti,200,2000',user_fullname, user_email, user_affiliation)"

result = madConn.isprint(fileList[0].name, 'gdalt,ti','filter=recno,0,4 filter=ti,200,2000',user_fullname, user_email, user_affiliation)

reply = raw_input('')

print 'print data: result'

reply = raw_input('')

print result

print 'You can also search a Madrigal site for experiments at other Madrigal sites.'
print 'In the next example we call getExperiments for PFISR (code=61) using the Millstone site'
print "\texpList = madConn.getExperiments(61, 2008,1,1,0,0,0,2008,1,31,0,0,0, local=0)"
expList = madConn.getExperiments(61, 2008,1,1,0,0,0,2008,1,31,0,0,0, local=0)

reply = raw_input('')

print 'Print the first experiment: expList[0]\n'

reply = raw_input('')

# make sure its from SRI
for exp in expList:
    if exp.siteid == 3:
       break
       
print(exp)

print 'To connect to this non-local experiment, we need to connect to its madrigalUrl.'
print 'To get the url of this site, use the madrigalUrl attribute:'
print '\tsriUrl = expList[0].madrigalUrl'
sriUrl = exp.madrigalUrl

reply = raw_input('')

print 'Print sriUrl\n'

reply = raw_input('')

print sriUrl

reply = raw_input('')

print 'Using this url, you would then be able to access data from the SRI Madrigal site:'
print '\tmadConn = madrigalWeb.madrigalWeb.MadrigalData(sriUrl)'
madConn = madrigalWeb.madrigalWeb.MadrigalData(sriUrl)

reply = raw_input('')

print 'Then just repeat the same commands used for the Millstone Madrigal site.\n'

print("""Finally, there is a script called globalIsprint.py that allows you to search a part or all
a single Madrigal database, using and parameters and filters you want, to download all the data you
want into a file with a single command.  This script is built using the methods listed above.\n""")


print 'Demo complete.'
