from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>Hello — Day 1 完成</h1><p>Flask 项目已启动。</p>"

@app.route("/about")
def about():
    return "<h1>关于这个项目</h1><p>个人任务管理系统，我在用 Flask 学习后端。</p>"


if __name__ == "__main__":
    app.run(debug=True)

