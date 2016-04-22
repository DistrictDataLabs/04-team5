from flask import render_template, flash, redirect
from app import app


@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html',
							title='Home'
							)


@app.route('/about')
def about():
	return render_template('about.html',
							title='About'
							)

@app.route('/vizualizations')
def vizualizations():
	return render_template('vizualizations.html',
							title='Vizualizations'
							)

