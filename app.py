import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)
USER_NOT_LOGGED_STATUS = 1


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        connection = sqlite3.connect('/Users/ronaldocosta/Documents/pessoal/calendar/agenda.db')
        cursor = connection.cursor()

        user_email = request.form['email']
        user_password = request.form['password']

        query = "SELECT * FROM agenda_usuario WHERE usuario_email = '"+user_email+"' AND usuario_senha = '"+user_password+"'"
        cursor.execute(query)

        results = cursor.fetchall()

        if len(results) == 0:
            print('Incorrect credentials provided')
        else:
            cursor.execute("UPDATE agenda_usuario SET usuario_status = 2 WHERE usuario_email = '"+user_email+"'")
            connection.commit()
            connection.close()
            return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        connection = sqlite3.connect('/Users/ronaldocosta/Documents/pessoal/calendar/agenda.db')
        cursor = connection.cursor()

        query = "INSERT INTO agenda_usuario (usuario_nome, usuario_email, usuario_senha, usuario_status) VALUES( ?, ?, ?, ?)"
        data_tuple = (request.form['name'], request.form['email'], request.form['password'], USER_NOT_LOGGED_STATUS)

        cursor.execute(query, data_tuple)
        connection.commit()
        connection.close()

        return render_template('login.html')


@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')
