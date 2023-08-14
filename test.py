import sqlite3
import time
import hashlib

cur = sqlite3.connect('test.db')

curr = cur.cursor()

row = curr.execute("select * from users").fetchall()
print(row)

cur.commit()
cur.close()
