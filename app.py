#!/usr/bin/python
from flask import Flask, request, abort
import subprocess

#Back end is a flask application
app = Flask(__name__)

@app.route('/', methods=['POST'])
def report():
	#abort if the expected fields are not in request body
	if not request.json or not 'id' in request.json or not 'template' in request.json:
		abort(400)

	#call Report export service with report id and template 
	subprocess.call(["python", "ReportExportService.py", request.json["id"], request.json["template"]])

	return "201"

if __name__ == '__main__':
	app.run(debug=True)