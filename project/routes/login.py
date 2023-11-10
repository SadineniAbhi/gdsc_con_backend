from project import app,bcrypt
from flask import request, jsonify
from flask_jwt_extended import create_access_token,get_current_user
from project.models.user import User
from flask_bcrypt import Bcrypt

@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    all_usernames = User.query.with_entities(User.username).all()
    usernames = [username[0] for username in all_usernames]
    if username not in all_usernames:
        return jsonify({"msg": "Bad username or password"}), 401
    user = User.query.filter_by(username=username).first()
    
    if not bcrypt.check_password_hash(user.password_hash,password):
        return jsonify({"msg": "Bad username or password"}), 401
    
    access_token = create_access_token(identity=username)
    
    return jsonify(access_token=access_token)

    