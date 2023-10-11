
# Hello World App

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello World<h1>"

# Create a function which returns a String This is the second page and assigna URL route the second function with a decorator @app.route)'/second').
def second():
     return "<h2>This is the second page</h2>"
 
 #   Create a funtion third which returns a string This is the subpage of third page and assign a URL route the second function with a decorator @app.route('third/subthird').
 
@app.route('third/subthird')
def third():
     return "This is the subpage of third page"
 
# Create a dynamic URL which takes id number dynamicaly and return with a message which show id of page.
@app.route("/forth/<string:id>")
def forth(id):
    if id.isdigit():
        return f"The id of this page is {id}"
    else: 
        return f("Not a valid page {id}")

 

 # Run flask app
app.run(debug=False)






