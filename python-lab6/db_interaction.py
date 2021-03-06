import pymysql


def import_tasks():
    sql_delete = "DELETE FROM tasks"
    connection = pymysql.connect(user='root', password='root', database='task_list', host='localhost')
    cursor = connection.cursor()
    cursor.execute(sql_delete)
    connection.commit()
    file = open("task_list.txt", "r")
    tasks = file.read().splitlines()
    file.close()
    sql_insert = "INSERT INTO tasks(todo, urgent) VALUES (%s, %s)"
    for t in tasks:
        cursor.execute(sql_insert, (t, True,))
    connection.commit()
    cursor.close()
    connection.close()


def add_task(task, urgent):
    sql = "INSERT INTO tasks(todo, urgent) VALUES (%s, %s)"
    connection = pymysql.connect(user='root', password='root', database='task_list', host='localhost')
    cursor = connection.cursor()
    cursor.execute(sql, (task, urgent, ))
    connection.commit()
    cursor.close()
    connection.close()


def get_all_tasks():
    sql = "SELECT * FROM tasks"
    connection = pymysql.connect(user='root', password='root', database='task_list', host='localhost')
    cursor = connection.cursor()
    cursor.execute(sql)
    tasks = cursor.fetchall()
    cursor.close()
    connection.close()
    return tasks


def remove_task(id_task):
    sql = "DELETE FROM tasks WHERE id_task=(%s)"
    connection = pymysql.connect(user='root', password='root', database='task_list', host='localhost')
    cursor = connection.cursor()
    cursor.execute(sql, (id_task, ))
    connection.commit()
    cursor.close()
    connection.close()


def get_task(id_task):
    sql = "SELECT * FROM tasks WHERE id_task=(%s)"
    connection = pymysql.connect(user='root', password='root', database='task_list', host='localhost')
    cursor = connection.cursor()
    cursor.execute(sql, (id_task,))
    task = cursor.fetchone()
    cursor.close()
    connection.close()
    return task


def update_task(id_task, todo, urgent):
    sql = "UPDATE tasks SET todo = (%s), urgent = (%s) WHERE id_task = (%s)"
    connection = pymysql.connect(user='root', password='root', database='task_list', host='localhost')
    cursor = connection.cursor()
    cursor.execute(sql, (todo, urgent, id_task,))
    connection.commit()
    cursor.close()
    connection.close()


if __name__ == '__main__':
    print(get_all_tasks())
    remove_task("book summer holidays")
    print(get_all_tasks())
    add_task("book summer holidays")
    print(get_all_tasks())