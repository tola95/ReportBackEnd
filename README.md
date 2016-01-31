# ReportBackEnd
Python API endpoint to generate report documents given a report_id and the specification for the document.

### Setting up

On a terminal run python app.js (Some libraries may need to be downloaded using pip install <lib>)

### How to use

Send a http POST request to the server with data {"id":"report_id", "template":"report_template"}. Where report_id is the id of the desired report in the postgreSQL database and report_template is a flag specifying what template to use. 

Currently the supported templates are s (Simple PDF) and x (XML).