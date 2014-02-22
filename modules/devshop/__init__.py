#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template

from db.mongo import Mongo

app = Flask(__name__)
app.debug = True #reload changes

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/devshop')
def devshop():
    collection = driver.getCollection('local', 'Clients')
    client = collection.find_one()
    name = client['_id']
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    print("Initialize devshop")
    driver = Mongo()
    #print(driver)
    #driver.test()
    
    app.run(host='0.0.0.0')
    #app.run() #run only locally

