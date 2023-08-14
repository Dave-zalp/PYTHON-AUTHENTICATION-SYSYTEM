import sqlite3
import time
import hashlib
import re


connection = sqlite3.connect('test.db')
cursor = connection.cursor()

#cursor.execute('CREATE TABLE users (name TEXT, email TEXT, password TEXT )')
time.sleep(3)


class register:
    def __init__(self,name,email,password):
         self.name = name
         self.email = email
         self.password = password

    def hash_password(self):
        hash = hashlib.md5(self.password.encode('utf-8'))
        final_hash = hash.hexdigest()
        return final_hash

    def validate_email(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if re.fullmatch(regex,self.email):
            print('email confirmed')
            return self.email
        else:
            print('Invalid Email')
            exit()

    def store_details(self):
        print("REGISTERATION FORM")
        new_email = self.validate_email()
        new_pass = self.hash_password()
        cursor.execute(f"INSERT INTO users VALUES ({self.name}, {new_email}, {new_email})")
        connection.commit()
        connection.close()
        print("USER SUCCESSFULLY REGISTERED !!!!!!!!!!")

name = input('Enter your name: ')
email = input('Enter your email: ')
password = input('Enter your password: ')

user = register(name, email, password)



# cursor.execute("INSERT INTO user VALUES ('david', 24, 'road', 'active', '45')")
#
#
# #rows = cursor.execute("SELECT name, age, address, status, height FROM user").fetchall()
# #print(rows)
#
# name = 'david'
#
# row1 = cursor.execute(f"SELECT * FROM user WHERE name = '{name}'").fetchall()
# print(row1)
#
#
# connection.commit()
# connection.close()
