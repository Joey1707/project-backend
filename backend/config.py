import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable Flask-SQLAlchemy's modification tracking
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL', 
        'mysql+mysqlconnector://unvdnu4aakpz3k7n:IHIbeUFxZeEYDLo79v1A@b5brukhwg56tuq8wy9tu-mysql.services.clever-cloud.com:3306/b5brukhwg56tuq8wy9tu')  # Replace with your actual credentials)
    