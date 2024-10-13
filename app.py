#importing
from flask import Flask, jsonify, Response, request
from flask_cors import CORS
from detect import detect_vehicles  # Import the function, not the route
from db import init_db, db
from models import ParkingLot
import time
import json

# Create Flask app
app = Flask(__name__)

# Enable CORS for frontend communication
CORS(app)

# Initialize the database (using H2 or SQLite for now)
init_db(app)

# SSE route for real-time updates
@app.route('/events', methods=['GET'])
def events():
    def stream():
        while True:
            message = {"status": "Parking spot updated", "time": time.time()}
            yield f"data: {json.dumps(message)}\n\n"
            time.sleep(5)
    return Response(stream(), content_type='text/event-stream')

# YOLO detection route
@app.route('/detect', methods=['POST'])
def detect():
    image_path = "path_to_your_image.jpg"  # Placeholder for image path
    vehicle_count = detect_vehicles(image_path)
    return jsonify({"detected_vehicles": vehicle_count})

# Add parking lot route (POST)
@app.route('/parking_lots', methods=['POST'])
def add_parking_lot():
    data = request.json
    new_lot = ParkingLot(
        name=data['name'],
        address=data['address'],
        total_spots=data['total_spots'],
        available_spots=data['available_spots']
    )
    db.session.add(new_lot)
    db.session.commit()
    return jsonify({"message": "Parking lot added successfully!"}), 201

# Get parking lots info (GET)
@app.route('/parking_lots', methods=['GET'])
def get_parking_lots_info():
    lots = ParkingLot.query.all()
    lots_list = [{"name": lot.name, "address": lot.address, "total_spots": lot.total_spots, "available_spots": lot.available_spots} for lot in lots]
    return jsonify(lots_list)

if __name__ == '__main__':
    app.run(debug=True)
