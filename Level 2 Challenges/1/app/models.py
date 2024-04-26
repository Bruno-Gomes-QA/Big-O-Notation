from app import db
import datetime

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    department = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    variable_weight = db.Column(db.Boolean, nullable=False)