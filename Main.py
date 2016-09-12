import traceback
from sqlite3 import *
import sqlite3
from Car import Car
import sys

def Main():
    print("Welcome to a car shop")
    while True:
        display_main_menu()
        # Create_car_table()
        choices =  input("Select an option\n")
        if choices == '1':
            print("Search for a Car Method\n")
            search_car()

        elif choices == '2':
            print("Adding Car Method\n")
            add_car()

        elif choices == '3':
            print("Sell Car Method\n")
            sell_car()

        elif choices == '4':
            sys.exit()

        else:
            print("Not a valid option\n")

def display_main_menu():
    print('1) Search Car\n'
          '2) Add Car\n'
          '3) Sell Car\n'
          '4) Exit\n')

def Create_car_table():
    conn = sqlite3.connect('car.db')
    print("DB is opened")
    print("Create Table method")

    conn.execute(('''
    CREATE TABLE IF NOT EXISTS cars(
    MAKE VARCHAR(50) NOT NULL,
    CARYEAR INTEGER NOT NULL,
    MODEL VARCHAR(50) NOT NULL,
    PRICE INTEGER NOT NULL);'''))

    # car_test_data()
    conn.close()
    print("DB closed")

def create_car(make, year, model, price):
    make = Car(make, year, model, price)
    return make

#Add a new Car to the database
def add_car():
    print("Add Car Method")
    make = ''
    year = 0
    model = ''
    price = 0

    make = input("What is the make of the car?\n")
    year = int(input("What is the year of the car?\n"))
    model = input("What is the mocel of the car?\n")
    price = int(input("What is the price of the car?\n"))

    car_make = create_car(make, year, model, price)
    add_car_to_database(car_make)

def add_car_to_database(c):
    #From group project, movies catalog
    conn = sqlite3.connect('car.db')
    print("Db open")
    print("Add car method")
    add_cursor = conn.cursor()
    try:
        add_cursor.execute('INSERT INTO cars VALUES (?,?,?,?)', (c.make, c.year, c.model, c.price))
        conn.commit()
    except Error as e:
        print("Error: ", e, "occured")

def sell_car():

    conn = sqlite3.connect('car.db')
    print("Sell Car Method")
    make = ''
    year = 0
    model = ''
    price = 0

    make = input("What is the make of car\n")
    year = int(input("What is the year of car\n"))
    model = input("What is the model of car")
    price = int(input("What is the price of car"))

    delete_cursor = conn.cursor()
    delete_cursor.execute('DELETE FROM cars WHERE LIKE (?,?,?,?)', (make,year,model,price))

    conn.close()
    print("DB is closed")

def search_car():
    display_search_option()
    search_options = int(input("Select a search option\n"))
    if search_options == 1:
        conn = sqlite3.connect('car.db')
        make = ''
        make = input("What make of car are you looking for?")
        try:
            conn.execute('SELECT * FROM cars WHERE make LIKE ?', (make))
            for cars in conn.fetchall():
                print(create_car(cars[0], str(cars[1]), cars[2], cars[3]))
        except Error as e:
            print('Error: ', e, 'occured')

    elif search_options == 2:
        conn = sqlite3.connect('car.db')
        year = 0
        year = int(input("What year of car are you looking for?"))

        try:
            conn.execute('SELECT * FROM cars WHERE year=?', year)
        except Error as e:
            print('Error: ', e, 'occured')

    elif search_options == 3:
        conn = sqlite3.connect('car.db')
        model = ''
        model = input("What model are you looking for?")

        try:
            conn.execute('SELECT * FROM cars WHERE model LIKE ?', ('%' + model + '%'))
        except Error as e:
            print('Error: ', e, 'occured')

    elif search_options == 4:
        conn = sqlite3.connect('car.db')
        price = 0
        price = int(input("Type the price range"))
        if price >= 0 or price <= 20000:
            try:
                conn.execute('SELECT * FROM cars WHERE price >= 0 OR price <= 20000')
            except Error as e:
                print('Error: ', e, 'occured')
        elif price > 20000 or price <= 50000:
            try:
                conn.execute('SELECT * FROM cars WHERE price > 20000 OR price <= 50000')
            except Error as e:
                print('Error: ', e, 'occured')
    elif search_options == 5:
        sys.exit()
    else:
        print("Not a valid option")

def display_search_option():
    print('1) Search by make\n'
          '2) Search by year\n'
          '3) Search by model\n'
          '4) Search by price\n'
          '5) Exit Program\n')
#Tried to add but didn't seem to work
def car_test_data():
    conn = sqlite3.connect('car.db')
    print("Adding car data")

    conn.execute('INSERT INTO cars VALUES'('Toyota', 2009, 'Corolla', 16000))
    conn.execute('INSERT INTO cars VALUES'("Honda", 2001, "Accord", 15000))
    conn.execute('INSERT INTO cars VALUES'("Subaru", 2004, "Impreza", 25000))
    conn.execute('INSERT INTO cars VALUES'("Toyota", 2009, "Tundra", 22000))
    conn.execute('INSERT INTO cars VALUES'("Chevrolet", 2017, "Camaro", 32000))
    conn.execute('INSERT INTO cars VALUES'("Mitsubishi", 2003, "Evolution", 25000))

    print("Done adding test data")

    print("Db closed")
    conn.close()

Create_car_table()
# car_test_data()
Main()