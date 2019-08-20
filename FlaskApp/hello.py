from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

@app.route("/")
def index():
    return "Flask App!"

@app.route("/hello/<string:Sname>/")
def hello(Sname):
    return render_template('test.html', name=Sname)

if __name__ == "__main__":
    app.run()
    # app.run(host='0.0.0.0', port=80)


