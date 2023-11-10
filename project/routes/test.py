from project import app
from flask import jsonify
from flask_jwt_extended import get_jwt_identity,jwt_required

@app.route("/test", methods=["GET"])
@jwt_required()
def test():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


