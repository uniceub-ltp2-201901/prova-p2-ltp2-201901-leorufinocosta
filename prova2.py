from flask import Flask, render_template, request, redirect, url_for
from flaskext.mysql import MySQL
from bd import*

app = Flask(__name__)
mysql = MySQL()
mysql.init_app(app)

config(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/cadastrar', methods=['POST'])
def teste():
    if request.method == 'POST':
        url = request.form.get('url')
        conn, cursor = get_db(mysql)
        cadastrar(cursor, conn, url)
        cursor.close()
        conn.close()
        return render_template('home.html',top='Cadastramento efetuado com sucesso!')
    else:
        return redirect(url_for('cadastrar'))

@app.route('/codigo', methods=['POST'])
def teste2():
    if request.method == 'POST':
        teste = request.form.get('teste')
        cursor = mysql.get_db().cursor()
        teste2 = url_curt(cursor, teste)
        if teste2 is None:
            return render_template('home.html', error='Nada encontrado!')
        else:
            cursor = mysql.get_db().cursor()
            return render_template('url_curta.html', consulta=url_curt(cursor, teste))
    return




if __name__ == '__main__':
    app.run(debug=True)