import sys
from flask import Flask,  render_template, request, redirect
import flask
import json
import subprocess
import time
import requests

import re
import datetime
from urllib.parse import  urljoin

app = flask.Flask(__name__)
i = 0
base_url = 'https://freelancebaatiew.com/'
        # yield i+1

@app.route('/')
def index():
    try:
        
        query = "SELECT * from domain_urls"



    except Exception as e:
        return (str(e))
    

@app.route('/hello')
def hello_world():
    # yield 'hello!!!'
    def hello():
        try:
            i=0
            page_url = requests.get(base_url)

                # yield url+'\n'
        except:
            yield "Unexpected error:", sys.exc_info()[0] +'\n'
            
    return flask.Response(hello(), mimetype='text/html') 





@app.route('/version')
def version():
    return 'Python Version: ' + str(sys.version)

app.run(debug=True,host='0.0.0.0')