# db.py
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy (DB)
db = SQLAlchemy()

def init_db(app):
    # Initialize the database with Flask app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Using SQLite in-memory for now
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # Create all tables
    with app.app_context():
        db.create_all()
