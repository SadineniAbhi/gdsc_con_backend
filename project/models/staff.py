from project import db

class Staff(db.Model):
    staff_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    free_times = db.relationship('FreeTime', backref='staff_member', lazy='dynamic')

class FreeTime(db.Model):
    free_time_id = db.Column(db.Integer, primary_key=True)
    free_day = db.Column(db.Integer())
    time = db.Column(db.String(length=30), nullable=False)
    location = db.Column(db.String(length=50), nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.staff_id'), nullable=False)