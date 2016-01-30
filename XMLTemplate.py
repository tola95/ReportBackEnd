#!/usr/bin/python
import json
import sys
import dicttoxml

def toPdf(data):
    xml = dicttoxml.dicttoxml(data)
    print xml

def main(data):
    data_ = json.loads(data)
    toPdf(data_)

if __name__ == '__main__':
    main(sys.argv[1])