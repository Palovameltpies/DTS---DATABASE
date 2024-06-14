from flask import Flask, render_template, request
import sqlite3
from sqlite3 import Error

app = Flask(__name__)
DATABASE = ""

def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)
        return None

@app.route('/')
def render_home():
    return render_template('base.html')



@app.route('/black')
def render_black():
    return render_template('black.html')

@app.route('/blue')
def render_blue():
    return render_template('blue.html')

@app.route('/red')
def render_red():
    return render_template('red.html')

@app.route('/green')
def render_green():
    return render_template('green.html')

@app.route('/white')
def render_white():
    return render_template('white.html')




if __name__ == '__main__':
    app.run()
