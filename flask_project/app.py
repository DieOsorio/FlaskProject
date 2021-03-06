from flask import Flask, request, render_template, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=["GET", "POST"])
def index():
  if session.get("notes") is None:
    session["notes"] = []
  if request.method == "POST":
    note = request.form.get("note")
    session["notes"].append(note)

  return render_template("index.html", notes=session["notes"])

@app.route("/hello", methods=["POST"])
def hello():
  name = request.form.get("name")
  return render_template("hello.html", name=name)

@app.route("/frontend")
def frontend():
  return render_template("frontend.html")

@app.route("/backend")
def backend():
  return render_template("backend.html")

if __name__ == '__main__':
    app.run(debug=True)