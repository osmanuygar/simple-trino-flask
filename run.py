from flask import Flask, render_template, request
from trino import dbapi
import trino
import configparser

app = Flask(__name__)
config = configparser.ConfigParser()
config.read(r'config.txt')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/query', methods=['POST'])
def query():
    query = """{0}""".format(request.form['query'])
    print(query)
    conn = dbapi.connect(
        host=config.get('global', 'host'),
        port=443,
        http_scheme='https',
        auth=trino.auth.BasicAuthentication(config.get('global', 'username'), config.get('global', 'password'))
    )
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('query.html', rows=rows)


if __name__ == '__main__':
    app.run(debug=True)
