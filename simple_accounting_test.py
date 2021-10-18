from unittest.mock import MagicMock,Mock,patch
import unittest
import sqlite3
from SimpleAccounting import *
from SimpleAccounting import getCustomers
from SimpleAccounting import createAnOrder

class SimpleAccountingTests(unittest.TestCase):

    # Testing sqlite3 connections (Mock)
    def test_sqlite3_connect_success(self):

        sqlite3.connect = MagicMock(return_value='connection succeeded')

        dbc = DataBaseClass()
        sqlite3.connect.assert_called_with('test_database')
        self.assertEqual(dbc.connection,'connection succeeded')


    def test_sqlite3_connect_fail(self):

        sqlite3.connect = MagicMock(return_value='connection failed')

        dbc = DataBaseClass()
        sqlite3.connect.assert_called_with('test_database')
        self.assertEqual(dbc.connection, 'connection failed')

    def test_sqlite3_connect_with_sideaffect(self):

        self._setup_mock_sqlite3_connect()

        dbc = DataBaseClass('good_connection_string')
        self.assertTrue(dbc.connection)
        sqlite3.connect.assert_called_with('good_connection_string')

        dbc = DataBaseClass('bad_connection_string')
        self.assertFalse(dbc.connection)
        sqlite3.connect.assert_called_with('bad_connection_string')

    def test_sqlite3_create_valid_customer(self):        
        with patch('SimpleAccounting.sqlite3') as mocksql:
            mocksql.connect().cursor().fetchall.return_value = ['1']
            self.assertTrue(createACustomer(1, "nick", 12.99))
            self.assertTrue(getCustomers())
        
    def test_sqlite3_create_valid_order(self):        
        with patch('SimpleAccounting.sqlite3') as mocksql:
            mocksql.connect().cursor().fetchall.return_value = [True]
            
            self.assertTrue(createAnOrder(1,12.99))

    def test_sqlite3_create_invalid_customer(self):        
        with patch('SimpleAccounting.sqlite3') as mocksql:
            mocksql.connect().cursor().fetchall.return_value = ['1']
            self.assertFalse(createACustomer(1, 2, 12.99))
        
    def test_sqlite3_create_invalid_order(self):        
        with patch('SimpleAccounting.sqlite3') as mocksql:
            mocksql.connect().cursor().fetchall.return_value = [True]
            
            self.assertFalse(createAnOrder(1,"12.99"))

    def _setup_mock_sqlite3_connect(self):

        values = {'good_connection_string':True,
                  'bad_connection_string':False}

        def side_effect(arg):
            return values[arg]

        sqlite3.connect = Mock(side_effect=side_effect)


class DataBaseClass():

    def __init__(self,connection_string='test_database'):        
        self.connection = sqlite3.connect(connection_string)