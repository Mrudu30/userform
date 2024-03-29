import ast
import pymysql as p

class Database:

    # connect to database
    def connect(self):
       return p.connect(host="localhost",database="forms",user="root",password="",charset = "utf8mb4")

    # check email availability
    def email_available(self,email):
        conn = Database.connect(self)
        cursor = conn.cursor()

        try:
            cursor.execute('SELECT * FROM user WHERE email=%s',(email,))
            cursor.fetchall()
            return False
        except:
            return True
        finally:
            conn.close()

    # create user
    def create_user(self,data,list_hobbies,email):
        con = Database.connect(self)
        cursor = con.cursor()

        if Database.email_available(self,email=email) == True:
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
        else:
            message = 'Email Already Taken'
            print(message)
            con.close()
            return False

    # read user values
    def readuser(self,fname,id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            if fname is None:
                if id is None:
                    cursor.execute('SELECT * FROM user order by id asc')
                else:
                    cursor.execute('SELECT * FROM user WHERE id=%s',(id))
            else:
                cursor.execute('SELECT * FROM user WHERE f_name LIKE %s ORDER BY id ASC', ('%' + fname + '%',))
            return cursor.fetchall()
        except:
            con.rollback()
            return False
        finally:
            con.close()

    # sort function
    def sort(self,order):
        con = Database.connect(self)
        cursor = con.cursor()
        resp = order
        # resp = ast.literal_eval(order)
        att = resp[0]
        ord = resp[1].upper()
        try:
            # print(f'SELECT * FROM user ORDER BY {att} {ord}')
            print(att,ord)
            query=f'SELECT * FROM user ORDER BY {att} {ord}'
            cursor.execute(query)
            print(f'SELECT * FROM user ORDER BY {att} {ord}')
            print('query executed')
            return cursor.fetchall()
        except:
            con.rollback()
            return f'Not done'
        finally:
            con.close()

    # update user values
    def updateUser(self,id,data,list_hobbies,email):
        con = Database.connect(self)
        cursor = con.cursor()
        # print(data)
        # print(data['hobbies'])
        if Database.email_available(self,email=email) == True:
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
        else:
            message = 'Email Already Taken'
            print(message)
            con.close()
            return False

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