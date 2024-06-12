from flask import Flask, render_template, request
import sqlite3
from sqlite3 import Error

app = Flask(__name__)
DATABASE = "webtags.db"

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
    pass

@app.route('/blue')
def render_blue():
    pass

@app.route('/red')
def render_red():
    pass

@app.route('/green')
def render_green():
    pass

@app.route('/white')
def render_white():
    pass




if __name__ == '__main__':
    app.run()
