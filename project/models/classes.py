from project import db

class Classes(db.Model):
    class_id = db.Column(db.Integer(), primary_key=True)
    class_name = db.Column(db.String(length=30), nullable=False, unique=True)
    free_times = db.relationship('LeisureHours', backref='class', lazy='dynamic')

class LeisureHours(db.Model):
    free_time_id = db.Column(db.Integer, primary_key=True)
    free_day = db.Column(db.Integer())
    time = db.Column(db.String(length=30), nullable=False)
    location = db.Column(db.String(length=50), nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.class_id'), nullable=False)



