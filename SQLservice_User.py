import mysql.connector as db


DATABASE="accounts_info"

class SQL_User_db:
    def __init__(self):
        self.conn=db.connect(host="localhost",user="root",password="",db=DATABASE)

    def describe(self):
        cursor=self.conn.cursor()
        cursor.execute("desc accounts")
        res=cursor.fetchall()
        return res

    def add_user(self,username,password):
        cursor=self.conn.cursor()
        try:
            cursor.execute("""INSERT INTO accounts(username,password) VALUES(%(username)s,%(password)s);""",{"username":username,"password":password})
            self.conn.commit()
        except:
            print('duplicate username')
            return False
        return True

    # Added an encrypted function to protect the password
    def get_password(self,username):
        cursor=self.conn.cursor()
        cursor.execute("select MD5(password) from accounts where username = 'test4'")
        res=cursor.fetchall()
        if res == []:
            return 'error: No such user'
        return res[0][0]


# print(SQL_User_db().describe())

# print(SQL_User_db().add_user('test5','lalalala'))

print(SQL_User_db().get_password('test4')) 