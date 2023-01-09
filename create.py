import sqlite3

NOT_LOGGED_STATUS = 1

connection = sqlite3.connect('/Users/ronaldocosta/Documents/pessoal/calendar/agenda.db')
cursor = connection.cursor()

cursor.execute(
    'CREATE TABLE IF NOT EXISTS '
    'agenda_usuario('
    'usuario_nome TEXT, '
    'usuario_email TEXT, ' 
    'usuario_senha TEXT, '
    'usuario_status INTEGER, '
    'usuario_id_pk INTEGER '
    ')'
)
connection.commit()

users_list = [
    ('Ronaldo Costa', 'hello@ronaldocosta.dev', '123456', NOT_LOGGED_STATUS, '1'),
    ('Monike Freitas', 'monikefreitas@gmail.com', '453525', NOT_LOGGED_STATUS, '2'),
    ('Thiago Marcelo', 'thiagomarcelo@gmail.com', '986457', NOT_LOGGED_STATUS, '3'),
    ('Melinne Diniz', 'melinnediniz@gmail.com', '345361', NOT_LOGGED_STATUS, '4'),
    ('Fernando Freires', 'fernandofreires@gmail.com', '325246', NOT_LOGGED_STATUS, '5')
]

cursor.executemany('INSERT INTO agenda_usuario VALUES(?, ?, ?, ?, ?)', users_list)
connection.commit()

connection.close()
