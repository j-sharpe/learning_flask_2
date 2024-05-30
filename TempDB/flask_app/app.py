import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'j48f903jo3ewrv9i324njkkfaerj5lk34r'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    temps = conn.execute('SELECT * FROM temps').fetchall()
    conn.close()
    return render_template('index.html', temps=temps)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == "POST":
        celsius = request.form.get('celsius', '')
        if not celsius:
            flash('Temperature is required')
        else:
            try:
                fahrenheit = fahrenheit_from(celsius)
                conn = get_db_connection()
                conn.execute('INSERT OR IGNORE INTO temps (celsius, fahrenheit) VALUES (?,?)',
                (celsius, fahrenheit))
                conn.commit()
                conn.close()
            except ValueError:
                flash('Input must be an integer.')
        return redirect(url_for('index'))

    return render_template('create.html')


def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""

    fahrenheit = float(celsius) * 9 / 5 + 32
    fahrenheit = round(fahrenheit, 3)
    return fahrenheit



