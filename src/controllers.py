from res.app import app
from flask import Flask, render_template, request, redirect
from flask_login import current_user
from res.app import authenticate_user
import src.database as database


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        if authenticate_user(email=request.form['email'], 
        password=request.form['password']):
            return redirect('home')
        else:
            return redirect('/')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        database.add_user(
            name=request.form['name'],
            email=request.form['email'],
            password=request.form['password']
        )
        return redirect('/')
    else:
        render_template('register.html')


@app.route('/home')
def home():
    return render_template('home.html')