#!/usr/bin/python
from flask import Flask, request, abort
import subprocess

app = Flask(__name__)

@app.route('/', methods=['POST'])
def report():
	if not request.json or not 'id' in request.json or not 'template' in request.json:
		abort(400)
	subprocess.call(["python", "ReportExportService.py", request.json["id"], request.json["template"]])

	return "201"

if __name__ == '__main__':
	app.run(debug=True)