# ReportBackEnd
Python API endpoint to generate report documents given a report_id and the specification for the document.

### Setting up

On a terminal run python app.js (Some libraries may need to be downloaded using pip install <lib>)

### How to use

1. Send a http POST request to the server with data {"id":"report_id", "template":"report_template"}. Where report_id is the id of the desired report in the postgreSQL database and report_template is a flag specifying what template to use. 

Currently the supported templates are s (Simple PDF) and x (XML).

2. The specified document will be saved to the directory as report_(organization_name).(pdf|xml)

### Developer

Parameters for the postgreSQL database are specified in ReportExportService.py.

New templates can be created for pdf convesion. In this case you will have to add a new (flag, filename) pair to the templates dictionary in ReportExportService.

A test server is available in ReportExportServiceTests.py. This is necessary in order not to interrupt the running of the server while testing. Necessary test cases are 
1. Invalid report_id
2. Invalid template_name