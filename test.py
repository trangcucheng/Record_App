import sqlite3
conn = sqlite3.connect("transcripts.db")
c= conn.cursor()
c.execute("select * from users")
for i in c.fetchall():
    print(i)