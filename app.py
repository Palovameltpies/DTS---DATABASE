from flask import Flask, render_template, request
import sqlite3
from sqlite3 import Error

app = Flask(__name__)
DATABASE = "MTG_Database.sqlite"

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
    query = "SELECT name, type, power, toughness, stock, price FROM MTG_DATABASE WHERE colour = ?"
    connection = create_connection(DATABASE)
    cursor = connection.cursor()
    cursor.execute(query, ("Black",))

    data_list = cursor.fetchall()
    print(data_list)

    return render_template('black.html', data=data_list)

@app.route('/blue')
def render_blue():
    query = "SELECT name, type, power, toughness, stock, price FROM MTG_DATABASE WHERE colour = ?"
    connection = create_connection(DATABASE)
    cursor = connection.cursor()
    cursor.execute(query, ("Blue",))

    data_list = cursor.fetchall()
    print(data_list)

    return render_template('blue.html', data=data_list)

@app.route('/red')
def render_red():
    query = "SELECT name, type, power, toughness, stock, price FROM MTG_DATABASE WHERE colour = ?"
    connection = create_connection(DATABASE)
    cursor = connection.cursor()
    cursor.execute(query, ("Red",))

    data_list = cursor.fetchall()
    print(data_list)

    return render_template('red.html', data=data_list)

@app.route('/green')
def render_green():
    query = "SELECT name, type, power, toughness, stock, price FROM MTG_DATABASE WHERE colour = ?"
    connection = create_connection(DATABASE)
    cursor = connection.cursor()
    cursor.execute(query, ("Green",))

    data_list = cursor.fetchall()
    print(data_list)

    return render_template('green.html', data=data_list)

@app.route('/white')
def render_white():
    query = "SELECT name, type, power, toughness, stock, price FROM MTG_DATABASE WHERE colour = ?"
    connection = create_connection(DATABASE)
    cursor = connection.cursor()
    cursor.execute(query, ("White",))

    data_list = cursor.fetchall()
    print(data_list)

    return render_template('white.html', data=data_list)


@app.route('/collection')

def render_collection():
    query = "SELECT name, type, power, toughness, stock, price FROM MTG_DATABASE"
    connection = create_connection(DATABASE)
    cursor = connection.cursor()
    cursor.execute(query, )

    data_list = cursor.fetchall()
    print(data_list)

    return render_template('full_collection.html', data=data_list)

@app.route('/search', methods=['GET','POST'])
def render_search():
    look_up = request.form['Search']
    title = "Search for: '" + look_up + "' "
    look_up = "%" + look_up + "%"

    query = "SELECT name, type, power, toughness, stock, price FROM MTG_DATABASE WHERE name LIKE ? OR type LIKE ? OR colour LIKE ?"
    connection = create_connection(DATABASE)
    cursor = connection.cursor()
    cursor.execute(query, (look_up, look_up, look_up))

    data_list = cursor.fetchall()
    print(data_list)

    return render_template('full_collection.html', data=data_list, page_title=title)


if __name__ == '__main__':
    app.run()
