#!/python33/python
#Python 3 Example of how to use https://macvendors.co to lookup vendor from mac address
print ("Content-Type: text/html\n")

import json
import codecs
import urllib.request as urllib2


def mac():
    e=input("mac_address:")
    #API base url,you can also use https if you need
    url = "http://macvendors.co/api/"
    #Mac address to lookup vendor from
    mac_address = e

    request = urllib2.Request(url+mac_address, headers={'User-Agent' : "API Browser"}) 
    response = urllib2.urlopen( request )
    #Fix: json object must be str, not 'bytes'
    reader = codecs.getreader("utf-8")
    obj = json.load(reader(response))

    #Print company name
    print (obj['result']['company']);

    #print company address
    print (obj['result']['address']);
    return

count = 0
while (count < 10):
   mac()
