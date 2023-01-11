import sqlite3
import os


def create_database():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    connection = sqlite3.connect(dir_path + "/agenda.db")
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
