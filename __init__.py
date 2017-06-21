from flask import Flask,request,render_template
from content import content

con=content()
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("dashboard.html",con=con)

@app.route('/profile/<username>')
def profile(username):
    return render_template("profile.html",username=username)
    
@app.route('/display/<int:id>')
def display(id):
    return 'hey there %s' %id

if __name__ == "__main__":
    app.run(debug=True)
