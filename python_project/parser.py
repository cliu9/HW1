import os
import sys
import time
import urllib2
import xml.etree.ElementTree as ET
import csv

# Get the root node of the XML hierarchy, and total detector number
tree=ET.parse('stream.xml')
root=tree.getroot()
z=root.getchildren()[2].getchildren()[0].getchildren()[3]
length = len(z)

f= open('streamdata.csv','w')
writer = csv.writer(f) 
writer.writerow(['Detector-ID']+['Status'])
## Get the ID and status from XML
for i in range(1,length,1):
         detid =z.getchildren()[i].getchildren()[0].text
         status=z.getchildren()[i].getchildren()[1].text
         writer.writerow([detid]+[status]) ## must use [] to make sure the data is a list.OW, the string would be segmented.
f.close()
