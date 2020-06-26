# grab the RDF (OWL) CDISC CT standards from the NIH website
# Place every version in its own directory named based on the date
# Author: Jimmy James
# yes I know this is kind of web scraping - not cool in this day and age
# but BeautifulSoup was just too juicy not to take it for a 'spin'
# For all you Pythonistas out there, yes you will probably die laughing at my code
# but I did this without officially knowing Python - doesn't that say something about
# Python? Yes Sir, it says you can code in Python without 'knowing' Python - How cool is that?


import sys
from bs4 import BeautifulSoup
import os
import urllib3
import re
import certifi
import pycurl
import zipfile


def getStandard(standard: str) -> str:
    # The top level directory (location) where you want your OWL files
    # location = 'D:\\Data\\CT_OWL'
    location = 'D:\\Data\\test'
    # CDASH and SDTM are in the same source location
    if standard == 'CDASH':
        stdLoc = 'SDTM'
    else:
        stdLoc = standard

    rootDir = location + "\\" + standard + "\\"
    try:
        os.mkdir(rootDir)
    except OSError:
        print("Creation of the directory %s failed" % rootDir)
    else:
        print("Successfully created the directory %s " % rootDir)
    http = urllib3.PoolManager()
    html_page = http.request('GET', 'https://evs.nci.nih.gov/ftp1/CDISC/' + stdLoc + '/Archive/')
    soup = BeautifulSoup(html_page.data.decode('utf-8'), 'html.parser')
    for link in soup.findAll('a', attrs={'href': re.compile(standard + ".*OWL.zip")}):
        dt = re.search("\\d{4}-\\d{2}-\\d{2}", link.get('href'))
        targetLocation = rootDir + dt.group()
        try:
            os.mkdir(targetLocation)
        except OSError:
            print("Creation of the directory %s failed" % targetLocation)
        else:
            print("Successfully created the directory %s " % targetLocation)
        with open(targetLocation + "\\" + link.get('href'), 'wb') as f:
            c = pycurl.Curl()
            c.setopt(c.URL, 'https://evs.nci.nih.gov/ftp1/CDISC/' + stdLoc + '/Archive/' + link.get('href'))
            c.setopt(c.WRITEDATA, f)
            c.setopt(c.CAINFO, certifi.where())
            c.perform()
            c.close()
        with zipfile.ZipFile(targetLocation + "\\" + link.get('href'), 'r') as zip_ref:
            zip_ref.extractall(targetLocation)
        os.remove(targetLocation + "\\" + link.get('href'))


# Input String for which standards are required
# CDASH | SDTM | SEND | ADaM | Define-XML | ALL

vslist = ['CDASH', 'SDTM', 'SEND', 'ADaM', 'Define-XML']

std = 'ALL'

if std not in vslist + ['ALL']:
    sys.exit(std + " not recognised")
if std == 'ALL':
    for st in vslist:
        getStandard(st)
else:
    getStandard(std)
