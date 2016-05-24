from flask import Flask, request, render_template, redirect, url_for, flash
import os
from flask.ext.sqlalchemy import SQLAlchemy
import socket

#SendGrid

app = Flask(__name__)
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']


@app.route('/')
def index():
	return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
	return redirect(url_for('index'))

if __name__ == "__main__":
	# app.debug = True
	app.run()

