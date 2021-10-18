import sqlite3
from sqlite3.dbapi2 import Error
from typing import Type
# local database used is sqlite3, no download necessary (saved right to the disk)
def createACustomer(id: int, name: str, total: float):
    try:
        if not isinstance(id, int) or not isinstance(name, str) or not isinstance(total, float):
            raise TypeError()
        connection = sqlite3.connect('customers.db')
        cursor = connection.cursor()
        createCustomerTable(connection, cursor)
        sql = '''INSERT INTO Customers(ID, Name, Total) VALUES(?,?,?)'''
        cursor.execute(sql, (id, name, total))
        connection.commit()
        connection.close()
        return True
    except Error as e:
        return False
    except TypeError as te:
        return False

def createAnOrder(custId: int, goods_total: float):
    try:
        if not isinstance(custId, int) or not isinstance(goods_total, float):
            raise TypeError()
        connection = sqlite3.connect('customers.db')
        cursor = connection.cursor()
        createOrderTable(connection, cursor)
        sql = '''INSERT INTO Oders(Cust_ID, Goods_Total) VALUES(?,?)'''
        cursor.execute(sql, (custId, goods_total))
        connection.commit()
        connection.close()
        return True
    except Error as e:
        return False
    except TypeError as te:
        return False

def getCustomers():
    connection = sqlite3.connect('customers.db')
    cursor = connection.cursor()
    sql = '''SELECT Name FROM Customers'''
    cursor.execute(sql)
    connection.commit()
    if len(cursor.fetchall()) > 0:
        connection.close()
        return True
    else:
        connection.close()
        return False

def createCustomerTable(connection, cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS Customers
                (ID INT, Name TEXT, Total REAL)''')
    connection.commit()

def createOrderTable(connection, cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS Orders
                (Cust_ID INT, Goods_Total REAL)''')
    connection.commit()
