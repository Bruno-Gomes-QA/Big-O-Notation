from database import Database

db = Database()
db.generate_products(10)
db.conn.close()