from flask import render_template, redirect
from app import app

user = { 'nickname': 'Mazzone'}

@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html",
		title = 'Home',
		user = user
		)

@app.route('/about')
def about():
	return render_template("about.html",
		title = 'About',
		user = user
		)

@app.route('/profile')
def profile():
	return render_template("profile.html",
		title = 'Profile',
		user = user
		)

@app.route('/newsfeed')
def newsfeed():
	return render_template("newsfeed.html",
		title = 'News Feed',
		user = user
		)

