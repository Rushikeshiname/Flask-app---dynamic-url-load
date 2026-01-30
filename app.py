from flask import Flask, render_template, request , url_for , redirect

"""
Instance of the Flask application.
which will be your WSGI (Web Server Gateway Interface) application.
"""

# WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the Flask application!"

@app.route("/index", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        return f"Hello, {name}!"
    return render_template("form.html")

@app.route("/success/<int:score>")
def success(score):
    res = ""
    if score >= 50:
        res = "You have passed the exam!"
    else:
        res = "You have failed the exam."
    return render_template("result.html", results=res)

@app.route("/successres/<int:score>")
def successres(score):
    res = ""
    if score >= 50:
        res = "You have passed the exam!"
    else:
        res = "You have failed the exam."

    exp={'score':score, 'result':res}
    return render_template("result1.html", results=exp)


@app.route("/successif/<int:score>")
def successif(score):
    return render_template("result.html", results=score)


@app.route("/fail/<int:score>")
def fail(score):

    return render_template("result.html", results=score)


@app.route("/submit", methods=["POST"])
def submit():
    science = float(request.form["science"])
    maths = float(request.form["maths"])
    computer = float(request.form["computer"])
    ds = float(request.form["ds"])

    total_score = (science + maths + computer + ds) / 4

    return redirect(url_for("successres", score=int(total_score)))

if __name__ == "__main__":
    app.run(debug=True)
