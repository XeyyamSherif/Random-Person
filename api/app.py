from flask import Flask, request
import psycopg2

app = Flask(__name__)

def connect_to_db():
    db = psycopg2.connect(user='admin', password= 'admin', host = 'db', 
        port=5432, database='random_user')
    return db



@app.route("/all", methods=['GET'])
def view():
    cur = connect_to_db().cursor()
    cur.execute('SELECT "name.first", "name.last", "dob.age", email, phone, "index"  FROM persons')
    result = cur.fetchall()
    print('niye?')
    return {
        'result':result
    }

@app.route('/delete/<int:id>/')
def delete_person(id):
    print(id)
    db = connect_to_db()

    cur = db.cursor()
    cur.execute("DELETE FROM persons WHERE index = '"+ str(id) +"' ")
    db.commit()
    return {
        "message":"deleted"
    }

@app.route('/person/<int:id>/')
def get_one_entity(id):
    db = connect_to_db()
    cur = db.cursor()
    cur.execute(f'SELECT "name.first", "name.last", "dob.age", email, phone, "index"  FROM persons where index={id}')
    person_spec = cur.fetchall()


    return {
        "data": person_spec
    }



if __name__ == "__main__":
    app.run(debug=True)