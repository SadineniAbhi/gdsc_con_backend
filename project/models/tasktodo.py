from project import db

class TasksToDo(db.Model):
    taskid = db.Column(db.Integer, primary_key=True)
    tasktitle = db.Column(db.String(200))
    status = db.Column(db.Boolean)

