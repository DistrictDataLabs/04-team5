from flask import render_template, flash, redirect
from app import app


@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Miguel'} # fake user
	posts = [ #fake array of posts
		{
			'author':{'nickname':'John'},
			'body': 'Beautiful day in Portland!'
		}, 
		{
			'author':{'nickname':'Susan'},
			'body': 'The Avengers Movie was so cool!'
		}
	]
	return render_template('index.html',
							title='Home',
							user = user,
							posts = posts)
