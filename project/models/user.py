from project import db

class User(db.Model):
    userid = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    current_year = db.Column(db.Integer(), nullable=False)
    days_attended = db.Column(db.Integer(),default = 0)
    working_days = db.Column(db.Integer(),default = 0)
    password_hash = db.Column(db.String(length=60), nullable=False)

