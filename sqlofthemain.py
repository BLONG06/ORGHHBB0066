import sqlite3 as s3


conn = s3.connect("maindb.db")
c = conn.cursor()
c.fetchall()