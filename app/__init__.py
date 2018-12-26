# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 02:56:40 2018

@author: Gipfeli
"""

from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes