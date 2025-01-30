from flask import Blueprint, request, jsonify
from backend.app import db
from api.backend.routes.userRoutes import User
from werkzeug.security import check_password_hash, generate_password_hash

auth = Blueprint('authRoutes', __name__)

@auth.route('/api/register', methods=['POST'])
def register():
    user_data = request.get_json()
    username = user_data.get('username')
    passwd = user_data.get('passwd')
    email = user_data.get ('email')

    hashed_password = generate_password_hash(passwd, method='scrypt')

    existing_user_name = User.query.filter_by(username=username).first()
    existing_user_email = User.query.filter_by(email=email).first()

    if existing_user_name:
        return jsonify({"error": "Name already taken"}), 400
    if existing_user_email:
        return jsonify({"error": "Email already registered"}), 400
    
    # Adding new user to the database
    hashed_password = generate_password_hash(user_data.get('passwd'), method='scrypt')
    new_user = User(username=username, email=email, passwd=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 200

@auth.route('/debug', methods=['GET'])
def debug():
    # Print out all columns of the User model
    print(User.__table__.columns)
    return jsonify({"message": "Check the server logs for output."}), 200

@auth.route('/login', methods=['POST'])
def login():
    user_data = request.get_json()
    username = user_data.get('username')
    passwd = user_data.get('passwd')

    if not username or not passwd:
        return jsonify({'error': 'missing username or password'}), 400

    user = User.query.filter_by(username=username).first()
    print(f"User found: {user}")
    print(f"Request data: {user_data}")

    if not user:
        print("User not found")
        return jsonify({'error': 'invalid credentials (user)'}), 401

    hashed_password = generate_password_hash(passwd, method='scrypt')
    print("this is the hashed password", hashed_password)
    
    print(f"Stored password hash: {user.passwd}")
    print(f"Provided password: {passwd}")
    print("Password check result:", check_password_hash(user.passwd, passwd))
    result = check_password_hash(user.passwd, passwd)
    print("Password check result:", result)

    if not check_password_hash(user.passwd, passwd):
        return jsonify({'error': 'invalid credentials(passwd)'}), 401

    return jsonify({'message': 'login successful'}), 200




