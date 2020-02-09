from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    # Display content of Index site
    ### return "Hello World"
    user = {'username': 'gipfeli'}
    posts = [
    	{
    		'author': {'username': 'John'},
    		'body': 'Windy night in Uzwil'
    	},
    	{
    		'author': {'username': 'Wick'},
    		'body': 'Fortune favors the bold!'
    	}		
    ]
    return render_template('index.html', 
    						title = 'Home', 
    						user=user,
    						posts=posts)