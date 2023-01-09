import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/index.html', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
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
            return render_template('register.html')

    return render_template('index.html')


@app.route('/register.html')
def register():
    return render_template('register.html')
