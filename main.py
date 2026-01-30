from flask import Flask
'''

Instance of the Flask application. 
which will be your WSGI (Web Server Gateway Interface) application.

'''

##WSGI Application

app=Flask(__name__)

@app.route("/") 
def welcome():
    return "<html><H1>Welcome to Flask Application</H1></html>"

@app.route("/index") 
def index():
    return "Welcome to the index page."


if __name__=="__main__":
    app.run(debug=True)     ## debug=True will help to auto reload the server on code changes


