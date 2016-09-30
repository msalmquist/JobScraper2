
import re
import urllib, urllib.request
# from bs4 import BeautifulSoup
import time
from random import randint
import skills

""" 
Author: msa
"""
##----------------------------------
def ProcessJobPage(urlString):
    uh = urllib.request.urlopen(urlString)
    # print(serviceurl + queryEncode)
    data = uh.read().decode()
    jobResults = re.findall('jobmap.*;', data)
    #print('Num of jobs this page:', len(jobResults))
    # totNumJobs = re.findall('a href="/jobs(.+)</a>?', data)
    #print("Job count: ", totNumJobs)
    for result in jobResults:
        if re.search('jk:', result) == None:
            continue
        jkVal = re.findall("jk:'(.*?)',", result)
        cmpIdVal = re.findall("cmpid:'(.*?)',", result)
        jobTitle = re.findall("title:'(.*?)',", result)
        print(jobTitle[0])
        try:
            jobQueryEncode = urllib.parse.urlencode({'jk':jkVal[0], 'fccid':cmpIdVal[0]})
            uh2 = urllib.request.urlopen(joburlBase + jobQueryEncode)
            data2 = uh2.read().decode()
            #print(data2.encode('utf-8'))
            skills.ProcessTextBlock(data2)
        except:
            print("Unable to process job page...")
        time.sleep(randint(5,20))
# ---end ProcessJobPage ---

jobString = '.net'
cityLocation = 'austin'
stateLocation = 'tx'
location = cityLocation + ',+' + stateLocation
jobListingNumber = 0
jobsPerPage = 10
serviceurl = 'http://indeed.com/jobs?'
MAXJOBS = 100

joburlBase = 'http://indeed.com/rc/clk?'
#locationToFind = 'South Federal University' # test location
locationToFind = 'University of Sarajevo' # actual location
initialQueryEncode = urllib.parse.urlencode({'q':jobString, 'l':location, 'rq':'1', 'fromage':'last'})
dummy = 4
urlString = serviceurl + initialQueryEncode
jobCount = 0;
while jobCount < 100:
    print('Processing jobs:', str(jobCount),'-',str(jobCount + jobsPerPage))
    ProcessJobPage(urlString)
    jobCount = jobCount + jobsPerPage
    queryEncodeNextJobListPage = urllib.parse.urlencode({'q':jobString, 'l':location, 'start':str(jobCount)})
    urlString = serviceurl + queryEncodeNextJobListPage
##---------------------------------------------
skills.PrintResults()



