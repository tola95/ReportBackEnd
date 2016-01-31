#!/usr/bin/python
import json
import sys
import dicttoxml
from sys import argv

def toPdf(data):
    #convert json data to xml
    xml = dicttoxml.dicttoxml(data)

    f = open("report_" + data["organization"] + ".xml", "wb")
    f.write(xml)
    f.close()

def main(data):
    data_ = json.loads(data)
    toPdf(data_)

if __name__ == '__main__':
    main(sys.argv[1])