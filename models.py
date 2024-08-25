from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(10), unique=True, nullable=False)
    room_number = db.Column(db.String(5), nullable=False)
    floor_number = db.Column(db.String(2), nullable=False)
    balance = db.Column(db.Float, default=0)
    meal_status = db.Column(db.Boolean, default=False)
    total_meals = db.Column(db.Integer, default=0)
    password = db.Column(db.String(150), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    is_dining_manager = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<User {self.name}>'
