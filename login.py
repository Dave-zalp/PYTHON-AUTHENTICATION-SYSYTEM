import sqlite3
import getpass

print('Login to your account to access your data')

name = input('Enter your name: ')
password = input("Enter your password: ")

connetion = sqlite3.connect('test.db')

cursor = connetion.cursor()

cursor.execute(f"SELECT * FROM user where name = '{name}'")

if cursor.fetchone() is not None:

    print(f'welcome {name}')
else:
    print('login failed')
    connetion.close()


connetion.commit()
