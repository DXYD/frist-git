import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()
sql = "select * from company"
data = c.execute(sql)
for i in data:
    print(i)
    print(i[1])
    print(i[2])