from project import db

class TasksFinished(db.Model):
    taskid = db.Column(db.Integer, primary_key=True)
    tasktitle = db.Column(db.String(200))