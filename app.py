from flask import Flask, render_template, request
import sqlite3
from sqlite3 import Error

app = Flask(__name__)
DATABASE = "identifier.sqlite"

def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)
        return None

@app.route('/')
def render_home():

    return render_template('home.html')



@app.route('/black')
def render_black():
    query = "SELECT name, type, power, toughness, stock, price FROM MTG_DATABASE WHERE colour = ? AND stock>0"
    connection = create_connection(DATABASE)
    cursor = connection.cursor()
    cursor.execute(query, ("Black",))

    data_list = cursor.fetchall()
    print(data_list)

    return render_template('black.html', data=data_list)

@app.route('/blue')
def render_blue():
    query = "SELECT name, type, power, toughness, stock, price FROM MTG_DATABASE WHERE colour = ? AND stock>0"
    connection = create_connection(DATABASE)
    cursor = connection.cursor()
    cursor.execute(query, ("Blue",))

    data_list = cursor.fetchall()
    print(data_list)

    return render_template('blue.html', data=data_list)

@app.route('/red')
def render_red():
    query = "SELECT name, type, power, toughness, stock, price FROM MTG_DATABASE WHERE colour = ? AND stock>0"
    connection = create_connection(DATABASE)
    cursor = connection.cursor()
    cursor.execute(query, ("Red",))

    data_list = cursor.fetchall()
    print(data_list)

    return render_template('red.html', data=data_list)

@app.route('/green')
def render_green():
    query = "SELECT name, type, power, toughness, stock, price FROM MTG_DATABASE WHERE colour = ? AND stock>0"
    connection = create_connection(DATABASE)
    cursor = connection.cursor()
    cursor.execute(query, ("Green",))

    data_list = cursor.fetchall()
    print(data_list)

    return render_template('green.html', data=data_list)

@app.route('/white')
def render_white():
    query = "SELECT name, type, power, toughness, stock, price FROM MTG_DATABASE WHERE colour = ? AND stock>0"
    connection = create_connection(DATABASE)
    cursor = connection.cursor()
    cursor.execute(query, ("White",))

    data_list = cursor.fetchall()
    print(data_list)

    return render_template('white.html', data=data_list)


@app.route('/collection')

def render_collection():
    query = "SELECT name, type, power, toughness, stock, price FROM MTG_DATABASE WHERE stock>0"
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

    if look_up == "%" + "Blue" + "%" or look_up == "%" + "blue" "%":
        search_colour = "Blue_Table"
    elif look_up == "%" + "Black" + "%" or look_up == "%" + "black" "%":
        search_colour = "Black_Table"
    elif look_up == "%" + "Red" + "%" or look_up == "%" + "red" "%":
        search_colour = "Red_Table"
    elif look_up == "%" + "Green" + "%" or look_up == "%" + "green" "%":
        search_colour = "Green_Table"
    elif look_up == "%" + "White" + "%" or look_up == "%" + "white" "%":
        search_colour = "White_Table"
    else:
        search_colour = ""

    if data_list == []:
        print("No values")
        e = "NO VALUES"
    else:
        e=""
    return render_template('full_collection.html', data=data_list, page_title=title, no_values=e,search_colour=search_colour)


if __name__ == '__main__':
    app.run()
