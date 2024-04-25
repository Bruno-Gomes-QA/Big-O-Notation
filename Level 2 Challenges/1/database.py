import sqlite3
from faker import Faker
import random
import datetime

class Database:
    def __init__(self):
    # Create DB, Table products and Utils

        self.fake = Faker()

        self.conn = sqlite3.connect('products.db')
        self.cur = self.conn.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        department TEXT,
                        price REAL NOT NULL,
                        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        variable_weight INTEGER NOT NULL)''')
        self.conn.commit()

    def random_datetime(self):
    # Generate Random Date Time in the range
        init = datetime.datetime(2010, 1, 1)
        final = datetime.datetime(2022, 12, 31)

        date = self.fake.date_time_between(start_date=init, end_date=final)

        return date

    def generate_products(self, products):
    # Generate Products and insert database

        for p in products:
            name = p[0]
            department = p[1]
            price = p[2]
            created = self.random_datetime()
            updated = created + datetime.timedelta(days=random.randint(1, 365))
            variable_weight = p[3]

            self.cur.execute('''INSERT INTO products (name, department, price, created, updated, variable_weight)
                        VALUES (?, ?, ?, ?, ?, ?)''', (name, department, price, created, updated, variable_weight))

        self.conn.commit()