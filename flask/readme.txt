Flask samples for CS257
Jeff Ondich
Last updated 17 April 2025

1. flask-sample.py
- This is where you should start in getting to know Flask.
- This sample illustrates a simple API that returns JSON results.
- The /actor/<last_name> route illustrates endpoints with variable URL components (<last_name> in this case)
- The /movies route illustrates an endpoint using GET parameters (i.e. the name=value pairs that comes after a ? in a URL)

2. template-sample.py
- This sample is more advanced, and you can ignore it until you're working on your web application's user interface.
- This sample illustrates a couple ways Flask's templating features can be used
* [index.html, hello.html, shared-header/*.html] using url_for to generate links to files stored in the static folder
* [hello.html] incorporating user input into a template, with automatic protection against injection attacks
* [shared-header/*.html] using {% include ... %} to share common HTML code across multiple templates

