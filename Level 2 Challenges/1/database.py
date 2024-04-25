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
                        description TEXT,
                        price REAL NOT NULL,
                        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        self.conn.commit()

    def random_datetime(self):
    # Generate Random Date Time in the range
        init = datetime.datetime(2010, 1, 1)
        final = datetime.datetime(2022, 12, 31)

        date = self.fake.date_time_between(start_date=init, end_date=final)

        return date

    def generate_products(self, n):
    # Generate (n) Random Products and insert database

        for _ in range(n):
            name = self.fake.word()
            description = self.fake.sentence()
            price = round(random.uniform(10, 1000), 2)
            created = self.random_datetime()
            updated = created + datetime.timedelta(days=random.randint(1, 365))

            self.cur.execute('''INSERT INTO products (name, description, price, created, updated)
                        VALUES (?, ?, ?, ?, ?)''', (name, description, price, created, updated))

        self.conn.commit()