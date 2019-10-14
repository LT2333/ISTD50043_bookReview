import mysql.connector as db


DATABASE="accounts_info"

class SQL_User_db:
    def __init__(self):
        self.conn=db.connect(host="localhost",user="root",password="19650531",db=DATABASE)

    def describe(self):
        cursor=self.conn.cursor()
        cursor.execute("desc accounts")
        res=cursor.fetchall()
        return res

    def add_user(self,username,password):
        cursor=self.conn.cursor()
        cursor.execute("""INSERT INTO accounts(username,password) VALUES(%(username)s,%(password)s);""",{"username":username,"password":password})
        self.conn.commit()
        cursor.execute("select * from accounts")
        res=cursor.fetchall()
        return res

    # Added an encrypted function to protect the password
    def get_password(self,username):
        cursor=self.conn.cursor()
        cursor.execute("select MD5(password) from accounts where username = 'test2'")
        res=cursor.fetchall()
        return res[0][0]


# print(SQL_User_db().describe())

# print(SQL_User_db().add_user('test4','lalalala'))

# print(SQL_User_db().get_password('test4')) 