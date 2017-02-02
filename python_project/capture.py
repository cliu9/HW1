import os
import sys
import time
import urllib2
import xml.etree.ElementTree as ET

# Get the XML data from online
url_str='http://205.221.97.102/Iowa.Sims.AllSites.C2C/IADOT_SIMS_AllSites_C2C.asmx/OP_ShareTrafficDetectorData?MSG_TrafficDetectorDataRequest=string%20HTTP/1.1'
request=urllib2.Request(url_str,headers={"Accept":"text/xml"})
contents = urllib2.urlopen(request).read()

# Write the data to the stream.file
f = open('stream.xml','w')
f.write(contents)
f.close()

