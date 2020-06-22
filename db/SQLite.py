import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()

# sql = '''
#     create table company
#         (id int primary key not null ,
#         username text not null ,
#         password int  not null );
# '''

# sql ='''
#     insert into company(id,username,password)
#     values (1,'zhangsan',123)
# '''

sql0 ='''
    insert into company(id,username,password)
    values (2,'lisi',123)
'''

# c.execute(sql)
c.execute(sql0)
conn.commit()
conn.close()

