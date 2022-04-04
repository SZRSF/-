import psycopg2
from flask import Flask

app = Flask(__name__)

# 通过connect方法，创建连接对象 conn
# 这里连接的是本地的数据库


def connect_db():
    connect = psycopg2.connect(
        database="postgresdb", user="postgres", password="123456", host="5432", port="5432")
    print('postgreSQL数据库“db_test”连接成功!')
    return connect


@app.route("/init_db")
def init_db():
    cursor.execute('''CREATE TABLE COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')


print("Table created successfully")


conn = connect_db()
cur = conn.cursor()


def close_db():
    cur.close()
    conn.close()


@app.route("/")
def hello_world():
    return 'Hello,Docker!'


@app.route('/insert')
def insert():
    cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )");
    cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");
    cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");
    cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");
    conn.commit()
    print("Records created successfully")
    conn.commit()
    conn.close()


@app.route('/show')
def show():
    cur.execute("SELECT id, name, address, salary  from COMPANY")
    rows = cur.fetchall()
    for row in rows:
        print("ID = ", row[0])
        print ("NAME = ", row[1])
        print ("ADDRESS = ", row[2])
        print ("SALARY = ", row[3], "\n")
        print ("Operation done successfully")
    conn.close()




if __name__=='__main__':
    app.run("0.0.0.0")