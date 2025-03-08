import sqlite3

con = sqlite3.connect(":memory:")

cur = con.cursor()

cur.execute("select sqlite_version();")
sqlite = cur.fetchone()
print(sqlite[0])
con.close()