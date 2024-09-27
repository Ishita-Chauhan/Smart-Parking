# models.py
from db import db

class ParkingLot(db.Model):
    __tablename__ = 'parking_lots'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    total_spots = db.Column(db.Integer, nullable=False)
    available_spots = db.Column(db.Integer, nullable=False)

    def __init__(self, name, address, total_spots, available_spots):
        self.name = name
        self.address = address
        self.total_spots = total_spots
        self.available_spots = available_spots
