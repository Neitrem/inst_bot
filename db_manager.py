import sqlite3


# create db
def create_table():
    conn = sqlite3.connect("person.db")

    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS emails(
                id INT PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                email TEXT,
                password TEXT,
                login TEXT,
                user_agent TEXT,
                proxy TEXT,
                login_inst TEXT,
                birthday TEXT,
                is_inst_created TEXT);""")
    conn.commit()


# insert person info into db
def set_person(person):
    conn = sqlite3.connect("person.db")

    cur = conn.cursor()

    cur.execute("""SELECT COUNT(*) FROM emails""")

    current_id = list(cur)[0][0] + 1

    new_email = (current_id, person['first_name'], person['last_name'], person['email'],
            person['password'], person['login'], person['ua'], person['proxy'], person['login_inst'],
                 str(person['birthday'][0]) + '.' + str(person['birthday'][1]) + '.' + str(person['birthday'][2]), '0')

    cur.execute("""INSERT INTO emails VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""", new_email)

    conn.commit()


# get person info from db
def get_person(pers_id):
    conn = sqlite3.connect("person.db")

    cur = conn.cursor()

    cur.execute("""SELECT * FROM emails WHERE id = (?);""", (str(pers_id),))

    info = list(cur)[0]

    person = {
        'id': info[0],
        'first_name': info[1],
        'last_name': info[2],
        'email': info[3],
        'password': info[4],
        'login': info[5],
        'ua': info[6],
        'proxy': info[7],
        'login_inst': info[8],
        'birthday': info[9].split('.'),
        'is_inst_created': info[10]
    }

    return person


# change any values
def change_value(value_name, new_value, pers_id):
    conn = sqlite3.connect("person.db")

    cur = conn.cursor()

    cur.execute(f"""UPDATE emails SET {value_name} = ? WHERE id = ?;""", (new_value, pers_id))

    conn.commit()
