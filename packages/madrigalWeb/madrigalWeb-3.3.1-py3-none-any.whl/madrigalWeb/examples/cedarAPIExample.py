"""  Example requested by Patrick West.

Prints a list of all instruments, along with earliest and latest date data are
available from any Madrigal site

$Id: cedarAPIExample.py 7369 2021-04-22 17:55:08Z brideout $
"""

import madrigalWeb.madrigalWeb

# constants
user_fullname = 'Bill Rideout - example'
user_email = 'brideout@haystack.mit.edu'
user_affiliation = 'MIT Haystack'

# this example would work using the url of any Madrigal site
madrigalUrl = 'http://madrigal.haystack.mit.edu/'

testData = madrigalWeb.madrigalWeb.MadrigalData(madrigalUrl)

# get a list of all instruments
instList = testData.getAllInstruments()

# loop through the instruments
for inst in instList:
    
    # get a list of all experiments at any Madrigal site for that instrument
    expList = testData.getExperiments(inst.code, 1950,1,1,0,0,0,2020,1,1,0,0,0,0)
    
    if len(expList) == 0:
        continue # no data

    expList.sort()  # will order them by date
    
    # print result
    s = 'Instrument %s: earliest date: %04i-%02i-%02i  - latest date: %04i-%02i-%02i' % (inst.name,
                                                                                         expList[0].startyear,
                                                                                         expList[0].startmonth,
                                                                                         expList[0].startday,
                                                                                         expList[-1].endyear,
                                                                                         expList[-1].endmonth,
                                                                                         expList[-1].endday)
    
    print(s)