# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 03:39:52 2018

@author: Gipfeli
"""

from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'Gipfeli'}
        
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]           
        
    return render_template('index.html', title = 'Home', user=user, posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

if __name__ == '__main__':
    app.run(host='0.0.0.0')