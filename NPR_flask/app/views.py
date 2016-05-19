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

@app.route('/visualizations')
def visualizations():
	return render_template('visualizations.html',
							title='Visualizations'
							)
@app.route('/methodology')
def methodology():
	return render_template('methodology.html',
							title='Methodology'
							)
@app.route('/links')
def links():
	return render_template('links.html',
							title='Links'
							)
       
       