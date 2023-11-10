from flask_jwt_extended import create_access_token, get_current_user
from flask import request, jsonify
from project import app
from project.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/regisiter",methods = ["POST"])
def register():
    username = request.json.get("username",None)
    password = request.json.get("password",None)
    current_year = request.json.get("current_year",None)
    if username == None:
        return jsonify({"msg":"enter user name"})
    elif password == None:
        return jsonify({"msg":"enter passord"})
    hashed_pass = bcrypt.generate_password_hash(password).decode("utf-8")
    newuser = User(username = username,current_year = current_year,password_hash = hashed_pass)
    return jsonify({"msg":"successfully created user"})

