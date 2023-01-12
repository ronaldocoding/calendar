import sqlite3


def create_database():
    connection = sqlite3.connect("/tmp/agenda.db")
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
