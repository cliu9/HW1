import os
import sys
import time
import urllib2
import xml.etree.ElementTree as ET
import numpy

# Get the root node of the XML hierarchy, and total detector number
tree=ET.parse('stream.xml')
root=tree.getroot()
z=root.getchildren()[2].getchildren()[0].getchildren()[3]
length = len(z)

f = open('det.csv','w')
# Get the 'Detector-id' and its 'status' from XML
f.write('Detector-id'+';'+'Status'+'\n')
for i in range(1,length,1):
  detid =z.getchildren()[i].getchildren()[0].text
  status=z.getchildren()[i].getchildren()[1].text
  f.write(detid+';'+status+'\n')
f.close()
 

