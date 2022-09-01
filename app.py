from flask import Flask, render_template

app = Flask(__name__)
# NOTe: JINJA HAS MANY FILTERS
@app.route("/")
def home():
    name ="John"
    stuff = "<h1> <strong>HI</strong> </h1>"
    x = [1,2,3,4,5]
    return render_template('index.html', name=name, stuff=stuff, x=x)

# the <name> means it will pass a name
# local host/user/john
@app.route("/user/<name>")
def user(name):
    return render_template('user.html', user_name=name)
# CUSTOM ERROR PAGES

# INVALID URL 
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
# INTERNAL SERVER ERROR
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

if __name__ == '__main__':
    app.run(debug = True)