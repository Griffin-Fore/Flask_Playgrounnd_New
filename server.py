from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def hello_world():
    return render_template("index.html", count=3,color="blue")

@app.route('/play/<int:x>')
def success(x):
    return render_template("index.html", count=x, color="blue")

@app.route('/play/<int:x>/<string:color>')
def hello(x,color):
    return render_template("index.html", count=x, color=color)

if __name__=="__main__":
    app.run(debug=True)