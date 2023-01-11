import sqlite3

NOT_LOGGED_STATUS = 1

connection = sqlite3.connect('./agenda.db')
cursor = connection.cursor()

cursor.execute(
    'CREATE TABLE IF NOT EXISTS '
    'agenda_usuario('
    'usuario_nome TEXT, '
    'usuario_email TEXT, ' 
    'usuario_senha TEXT, '
    'usuario_status INTEGER, '
    'usuario_id_pk INTEGER PRIMARY KEY AUTOINCREMENT'
    ')'
)
connection.commit()
connection.close()
