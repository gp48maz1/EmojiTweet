from flask import render_template, redirect
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = { 'nickname': 'Mazzone'}
	return render_template("index.html",
		title = 'Home',
		user = user
		)

@app.route('/about')
def about():
	return render_template("about.html",
		title = 'About')