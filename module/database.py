import pymysql as p

class Database:

    # connect to database
    def connect(self):
       return p.connect(host="localhost",database="forms",user="root",password="",charset = "utf8mb4")

    # create user
    def create_user(self,data,list_hobbies):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            list_hobbies_str=','.join(list_hobbies)
            # print(data)
            cursor.execute(
                'INSERT INTO user(f_name,l_name,email,mobno,gender,hobbies,country,address) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)',
                (data['fname'],data['lname'],data['email'],data['mobno'],data['gender'],list_hobbies_str,data['country'],data['addr'])
                )
            # print(
            #     'INSERT INTO user(f_name,l_name,email,mobno,gender,hobbies,country,address) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)',
            #     (data['fname'],data['lname'],data['email'],data['mobno'],data['gender'],data['hobbies'],data['country'],data['addr'])
            #     )
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    # read user values
    def readuser(self,id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            if id==None:
                cursor.execute('SELECT * FROM user')
            else:
                cursor.execute('SELECT * FROM user WHERE id=%s',(id,))
            return cursor.fetchall()
        except:
            con.rollback()
            return False
        finally:
            con.close()

    # update user values
    def updateUser(self,id,data,list_hobbies):
        con = Database.connect(self)
        cursor = con.cursor()
        # print(data)
        # print(data['hobbies'])

        try:
            list_hobbies_str=','.join(list_hobbies)
            # print('data reached here in try')
            # print(data)
            cursor.execute('UPDATE user set f_name=%s,l_name=%s,email=%s,mobno=%s,gender=%s,hobbies=%s,country=%s,address=%s WHERE id=%s',
                           (data['fname'],data['lname'],data['email'],data['mobno'],data['gender'],list_hobbies_str,data['country'],data['addr'],id))
            con.commit()
            return True
        except:
            # print('data in except')
            con.rollback()
            return False
        finally:
            con.close()

    # delete user
    def deleteUser(self,id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute('DELETE FROM user WHERE id=%s',(id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()