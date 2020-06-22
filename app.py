from Tools.scripts.make_ctype import method
from flask import Flask, render_template, redirect,request,sessions
from flask import request
import sqlite3
import time

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login', methods=['GET', 'POST'])
def login():  # 视图函数
    datalist = []
    if request.method == 'GET':  # 请求方式是get
        return render_template('login.html')  # 返回模板
    elif request.method == 'POST':
        username = request.form.get('username')  # form取post方式参数
        password = request.form.get('password')  # getlist取一键多值类型的参数

    conn = sqlite3.connect('test.db')

    c = conn.cursor()
    sql = "select * from company"
    data = c.execute(sql)
    for i in data:
        if username == str(i[1]) :
            if password == str(i[2]):
                return redirect('https://lirundong.top')
            else:
                return "密码错误"
    else:
        return "账号错误"
        # data = c.execute(sql)
        # for i in data:
        #     datalist.append(i)
        #     for abc in datalist:
        #             if username == abc[1] and password == abc[2]:
        #                 return redirect('https://lirundong.top/')
        #             else:
        #                 return "您所输入的账号或密码错误,请重新输入"
        # return "账号：%s 密码：%s " % (username, password)
    c.close()
    conn.close()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':  # 请求方式是get
        return render_template('register.html')  # 返回模板
    elif request.method == 'POST':
        username = request.form.get('username')  # form取post方式参数
        password = request.form.get('password')  # getlist取一键多值类型的参数

    i = int(time.time())


    conn = sqlite3.connect('test.db')

    c = conn.cursor()
    sql = '''
        insert into company(id,username,password)
        values ('%d' ,'%s','%s')
    '''%(i,username,password)
    c.execute(sql)
    conn.commit()
    conn.close()

    return "%s您好，已成功注册,您的密码为%s"%(username,password)

if __name__ == '__main__':
    app.run()
