import sqlite3 as s3

try:
    conn = s3.connect("database.db")

    try:
        c = conn.cursor()
    except:
        print('Erro na conexão com a database. Tente novamente depois')

except:
    print('Erro na conexão com a database. Tente novamente depois')

else:
    c.fetchall()