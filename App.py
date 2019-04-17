from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from Products import Products
from AppConstants import AppConstants


app = Flask(__name__)
appConstants = AppConstants()

@app.route('/')
def home():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		products = []
		for product in appConstants.products :
			products.append(Products(product["name"], product["description"], product["price"], product["ownerName"]).getProducts())
		print(products)
		return "Logged in successfully"
 
@app.route('/login', methods=['POST'])

def do_admin_login():
	userCredentials = {"username": "admin", "password": "password"}
	if request.form['password'] == userCredentials['password'] and request.form['username'] == userCredentials['username']:
		session['logged_in'] = True
	else:
		flash('wrong password!')
	return home()
 
if __name__ == "__main__":
	app.secret_key = os.urandom(12)
	app.run(debug=True,host='192.168.11.105', port=4000)