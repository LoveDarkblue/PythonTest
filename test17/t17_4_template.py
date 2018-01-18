from flask import Flask, request, render_template

app = Flask(__name__)


# 主页面
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')  # 直接返回home.html页面


# 登录页面
@app.route('/signIn', methods=['GET'])
def signIn_page():
    return render_template('signForm.html')  # 直接返回signForm.html页面


# 登录接口请求
@app.route('/signIn', methods=['POST'])
def signin():
    username_ = request.form['username']
    password_ = request.form['password']
    if username_ == 'admin' and password_ == '123':
        return render_template('sign_ok.html', username=username_)  # 返回sign_ok.html页面并带一个username参数
    return render_template('signForm.html', username=username_,
                           message='Bad Username or password')  # 返回signForm.html页面并带一个username参数和message参数


if __name__ == '__main__':
    app.run()
