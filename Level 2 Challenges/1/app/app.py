from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # Configuração do banco de dados
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)