from flask import Flask, request

app = Flask(__name__)


# 主页面
@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'


# 登录页面
@app.route('/signIn', methods=['GET'])
def signIn_page():
    return '''<form action="/signIn" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''


# 登录接口请求
@app.route('/signIn', methods=['POST'])
def signin():
    if request.form['username'] == 'admin' and request.form['password'] == '123':
        return '<h3>Hello admin</h3>'
    return '<h3>Bad username or password</h3>'


if __name__ == '__main__':
    app.run()
