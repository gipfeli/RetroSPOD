# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 03:39:52 2018

@author: Gipfeli
"""

from app import app

@app.route('/')
@app.route('/index')

def index():
	user = {'username': 'Gipfeli'}
	return '''
<html>
	<head>
		<title>Home Page - Microblog</title>
	</head>
	<body>
		<h1>Hello ''' +user['username'] + '''!</h1>
	</body>
</html>'''