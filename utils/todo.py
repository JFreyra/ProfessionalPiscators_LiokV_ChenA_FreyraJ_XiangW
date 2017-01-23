import sqlite3

def addTask( user_id, name, position ):
    db=sqlite3.connect("../data/potato.db")
    c=db.cursor()
    q = "SELECT id FROM task"
    c.execute(q)
    infoid = c.fetchall()
    if len(infoid) == 0:
        lengthid = 0
    else:
        lengthid = len(infoid)
    if position > lengthid or position < 0:
        db.close()
        return False
    times = lengthid - position
    counter = lengthid - 1
    num = 0
    while num < times:
        q = "UPDATE task SET id = " + str(counter+1) + ", next_task_id = " + str(counter+2) + " WHERE id = " + str(counter)
        c.execute(q)
        counter-=1
        num+=1
    q = "INSERT INTO task VALUES( " + str(position) + ", " + str(user_id) + ", \"" + name + "\", " + str(position+1) + ")"
    c.execute(q)
    db.commit()
    db.close()
    return True

def deleteTask( position ):
    db=sqlite3.connect("../data/potato.db")
    c=db.cursor()
    q = "DELETE FROM task WHERE id = " + str(position)
    c.execute(q)
    q = "SELECT id FROM task"
    c.execute(q)
    infoid = c.fetchall()
    if len(infoid) == 0:
        lengthid = 0
    else:
        lengthid = len(infoid)
    if position > lengthid or position < 0:
        db.close()
        return False
    times = lengthid - position
    counter = position
    num = 0
    print num
    print times
    while num < times:
        q = "UPDATE task SET id = " + str(counter-1) + ", next_task_id = " + str(counter) + " WHERE id = " + str(counter)
        c.execute(q)
        counter+=1
        num+=1
    db.commit()
    db.close()
    return True

print deleteTask(0)
