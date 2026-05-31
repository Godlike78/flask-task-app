from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>Hello — Day 1 完成</h1><p>Flask 项目已启动。</p>"


if __name__ == "__main__":
    app.run(debug=True)
