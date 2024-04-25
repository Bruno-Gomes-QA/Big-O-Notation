from database import Database

db = Database()

with open('sample.txt', 'r') as file:
    products_list = []
    
    for l in file:
        part = [part.strip() for part in l.split('-')]
        product = [part[0], part[1], part[2], part[4]]
        products_list.append(product)

db.generate_products(products_list)
db.conn.close()