#!/usr/bin/python
import psycopg2
import sys
import pprint
import json
import subprocess

#database data
host = "candidate.suade.org"
dbname = "suade"
user = "interview"
password = "LetMeIn"

#template dictionary, specifying which template to select given a template flag
templates = {
        's': "SimpleReportTemplate.py",
        'x': "XMLTemplate.py"
    }

#create report with record data and template 
def createReport(record, pdf_template):
    subprocess.call(["python", templates[pdf_template], record[0][1]])

def main(report_id, pdf_template):
    #select the corresponding report with report_id
    conn_string = "host=" + host + " dbname=" + dbname + " user=" + user + " password=" + password
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reports WHERE id=%s", report_id)
    record = cursor.fetchall()

    #if there is no record with this id, throw exception
    if (len(record) == 0):
        raise Exception("Specified ID is not present in database")
        print "Specified ID is not present in database"
    
    #if there is no template with this flag, throw exception
    if (pdf_template not in templates):
        raise Exception("Specified template does not exist")
        print "Specified template does not exist"
    
    createReport(record, pdf_template)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])