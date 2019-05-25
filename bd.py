import random

def config(app):
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
    app.config['MYSQL_DATABASE_DB'] = 'prova2'


def get_db(mysql):
    conn = mysql.connect()
    cursor = conn.cursor()

    return conn, cursor

def cadastrar(cursor, conn, url):
    numero = random.randint(10000, 99999)
    cursor.execute(f'INSERT INTO cadastro (url, codigo) values ("{url}", {numero})')
    conn.commit()

def url_curt(cursor, teste):
    cursor.execute(f'SELECT urlencurtada, url, codigo from cadastro where url="{teste}"')
    consulta = cursor.fetchall()
    cursor.close()
    print(consulta)
    return consulta

