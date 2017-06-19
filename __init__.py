from flask import Flask,request,render_template
app = Flask(__name__)
@app.route('/')
@app.route('/<user>')
def index(user=None):
    return render_template("user.html",user=user)

@app.route('/profile/<username>')
def profile(username):
    return render_template("profile.html",username=username)
    
@app.route('/display/<int:id>')
def display(id):
    return 'hey there %s' %id

if __name__ == "__main__":
    app.run(debug=True)
