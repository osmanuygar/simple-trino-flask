# Simple Trino Flask App

This is a Flask app that allows you to query a Trino cluster and display the results in a web browser.

## Installation

To install the app and its dependencies, follow these steps:
```bash
# Clone the repository:
$ git clone https://github.com/osmanuygar/trino-flask-app.git
$ cd trino-flask-app

# Create a virtual environment and activate it:
$ python3 -m venv venv
$ source venv/bin/activate

#Install the dependencies:
$ pip install -r requirements.txt
```

## Configuration
Before you can use the app, you need to configure it with the connection details for your Trino cluster. Edit the config.txt file and set the values for host, username, password.

## Usage
To start the app, run the following command:
```bash
python run.py
```

This will start a local web server at http://localhost:5000/.

To query your Trino cluster, go to http://localhost:5000/query in your web browser. Enter your SQL query and click the "Submit" button. The results will be displayed in a table below the form.

