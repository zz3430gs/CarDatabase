from sqlite3 import *
import sqlite3
from Car import Car
import sys

def Main():
    print("Welcome to a car shop")
    while True:
        display_main_menu()
        Create_car_table()
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

    conn.execute(('''CREATE TABLE IF NOT EXISTS cars(
    MAKE TEXT NOT NULL
    CAR_YEAR INTEGER NOT NULL
    MODEL TEXT NOT NULL
    PRICE INTEGER NOT NULL)'''))

    car_test_data()
    conn.close()
    print("DB closed")

def create_car(make, year, model, price):
    make = Car(make, year, model, price)


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

    car_make = creat_car(make, year, model, price)
    add_car_to_database(car_make)

def add_car_to_database(c):
    #From group project movies catalog
    conn = sqlite3.connect('car.db')
    print("Db open")
    print("Add car method")
    add_cursor = conn.cursor()
    try:
        add_cursor.execute('INSERT INTO cars VALUES (?,?,?,?)', (c.make, c.year, c.model, c.price))
        conn.commit()

    except IntegrityError:
        conn.rollback()

    except Error as e:
        print("Rollinf back changes due to error: ", e)
        traceback.print_exc()
        conn.rollback()

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

    delete_cursor.execute('DELETE FROM cars WHERE (?,?,?,?)', (make,year,model,price))

    conn.close()
    print("DB is closed")

def search_car():
    search_options = int(input("Select a search option"))
    if search_options == '1':
        make = input("What make of car are you looking for?")
        conn = sqlite3.connect('car.db')
        make_cursor = conn.cursor()
        try:
            make_cursor('SELECT * FROM cars WHERE make LIKE ?', ('%' + make + '%'))
            for cars in make_cursor.fetchall():
                print(creat_car(make[0], str(make[1]), make[2], make[3]))
        except Error as e:
            print('Error: ', e, 'occured')

    elif search_options == '2':
        year = int(input("What year of car are you looking for?"))
        conn = sqlite3.connect('car.db')
        year_cursor = conn.cursor()
        try:
            year_cursor('SELECT * FROM cars WHERE year LIKE ?', ('%' + year + '%'))
            for cars in year_cursor.fetchall():
                print(make[0], str(make[1], make[2], make[3]))
        except Error as e:
            print('Error: ', e, 'occured')

    elif search_options == '3':
        model = input("What model are you looking for?")
        conn = sqlite3.connect('car.db')
        model_cursor = conn.cursor()
        try:
            model_cursor('SELECT * FROM cars WHERE model LIKE ?', ('%' + model + '%'))
            for cars in model_cursor.fetchall():
                print(make[0], str(make[1], make[2], make[3]))
        except Error as e:
            print('Error: ', e, 'occured')

    elif search_options == '4':
        conn = sqlite3.connect('car.db')
        price = int(input("Type the price range"))
        price_cursor
        if price >= 0 or price <= 20000:
            try:
                year_cursor('SELECT * FROM cars WHERE price >= 0 OR <=20000')
                for cars in year_cursor.fetchall():
                    print(make[0], str(make[1], make[2], make[3]))
            except Error as e:
                print('Error: ', e, 'occured')
        elif price > 20000 or price <= 50000:
            try:
                year_cursor('SELECT * FROM cars WHERE price > 20000 OR <= 50000')
                for cars in year_cursor.fetchall():
                    print(make[0], str(make[1], make[2], make[3]))
            except Error as e:
                print('Error: ', e, 'occured')
    else:
        print("Not a valid option")


def car_test_data():
    conn = sqlite3('car.db')
    print("Adding car data")

    conn.execute('INSERT INTO cars VALUES'("Toyota", 2009, "Corolla", 16000))
    conn.execute('INSERT INTO cars VALUES'("Honda", 2001, "Accord", 15000))
    conn.execute('INSERT INTO cars VALUES'("Subaru", 2004, "Impreza", 25000))
    conn.execute('INSERT INTO cars VALUES'("Toyota", 2009, "Tundra", 22000))
    conn.execute('INSERT INTO cars VALUES'("Chevrolet", 2017, "Camaro", 32000))
    conn.execute('INSERT INTO cars VALUES'("Mitsubishi", 2003, "Evolution", 25000))

    print("Done adding test data")

    print("Db closed")
    conn.close()


Main()

