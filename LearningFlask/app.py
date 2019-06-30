from flask import (Flask, request, send_from_directory,
                   render_template,redirect, url_for)
import MySQLdb

app = Flask(__name__)
'''
flask define route: path, string, int, float, uuid
'''
@app.route('/')
def hello_world():

    return 'Hello World!'

#这是一个如何把一个html展示出来的函数
@app.route('/templates/<name>')#这个是给路径使用的
def hello_Keng(name = None):
    return render_template("keng.html", user = name)#抓取这个页面展示到前端。

#这个功能实现的是如何进行页面跳转
@app.route("/redirect")
def redirect_test():
    name = "Mr.wang"
    #return redirect("/templates/{}".format(name))#像这样直接跳转没有问题，但是还有一种方式。
    return redirect(url_for("hello_world"))

#捕捉404，然后返回一个好看点的页面提示
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

@app.route("/static/<path:path>")
def send_file(path):
    return send_from_directory("download", path)

DATABASE = {
    'host':'localhost',#如果是远程数据库，此处为远程数据库的IP地址
    'database':'pythontestsql',#这个地方是选择一个数据库进行连接
    'user':'root',
    'password':'123456',
    'charset':'utf8'
} #基本信息建立好以后呢，我们进行连接'
db = MySQLdb.connect(**DATABASE)
@app.route("/db/<name>")
def hello_db(name):
    cursor = db.cursor()
    sql = "select * from studentinfo"
    cursor.execute(sql)
    result = cursor.fetchall()
    return render_template("user_list.html", studentinfo = result, User = name)


if __name__ == '__main__':
    app.run()
