import sqlite3
conn = sqlite3.connect("transcripts.db")
c = conn.cursor()
c.execute("select * from users")
for item in c.fetchall():
    print(item)

conn.commit()
conn.close()
