from sqlalchemy import create_engine
import time


db_name = 'random_user'
db_user = 'admin'
db_pass = 'admin'
db_host = 'db'
db_port = '5432'


def connect():
    db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
    db = create_engine(db_string)
    try:
        db.execute('DELETE FROM persons')
    except:
        print("Table doesnt exist yet")
    return db

