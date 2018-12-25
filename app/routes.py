# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 03:39:52 2018

@author: Gipfeli
"""

from app import app

@app.route('/')
@app.route('/index')

def index():
	return "Hello World"