from project.models.classes import Classes
from project.models.staff import Staff, FreeTime
from project.models.tasksfinished import TasksFinished
from project.models.tasktodo import TasksToDo
from project.models.tasksfinished import TasksFinished
from project.models.user import User
from project import db,app
""" user1 = User(username="abhi",current_year = 2, days_attended = 10,working_days = 20,password_hash = "abhi2004")
user2 = User(username ="uma",current_year = 3, days_attended = 12,working_days = 15,password_hash = "uma2004") """

""" staff1 = Staff(name="arjun")
staff2 = Staff(name="poojith")
freetime1 = FreeTime(free_day = 1,time = "5 pm",location = "Mech block Room-1222",staff_id = 1)
freetime2 = FreeTime(free_day = 5,time = "10 am",location = "ECE block Room-2333",staff_id = 1)
freetime3 = FreeTime(free_day = 3,time = "9 pm",location = "cse block Room-1222",staff_id = 2)
freetime4 = FreeTime(free_day = 2,time = "1 pm",location = "It block Room-2333",staff_id = 2) """

with app.app_context():
    # Replace 1 with the actual staff_id you're looking for
    staff_id = 1  

    # Using Session.get() to retrieve the staff member
    staff1 = db.session.get(Staff, staff_id)

    # Print or do something with the query result
    print(staff1)
    print(staff1.name)
    freetime = list(staff1.free_times)

    all_usernames = User.query.with_entities(User.username).all()
    usernames = [username[0] for username in all_usernames]

    print(usernames)

