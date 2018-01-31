import bcrypt as bcrypt
from flask import Flask,render_template,url_for,request,session,redirect
from flask_pymongo import PyMongo
import datetime
import bcrypt

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'mongo_login'
app.config['MONGO_URI'] = 'mongodb://rajat:rajatrishav@ds119585.mlab.com:19585/mongo_login'

mongo = PyMongo(app)

@app.route('/')
def index():
    if 'username' in session:
        return render_template('logged.html',name=session['username'])
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name':request.form['username']})
    if login_user:
        if bcrypt.hashpw(request.form['password'].encode('utf-8'),login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        return 'Wrong password!'
    return 'Wrong username!'

@app.route('/register', methods=['POST','GET'])
def register():
    if request.method=='POST':
        users = mongo.db.users
        existing_user = users.find_one({'name':request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'),bcrypt.gensalt())
            users.insert({'name':request.form['username'],'password':hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))

        return 'This username already exists! Try again with a different username.'
    return render_template('register.html')

@app.route('/logout',methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('index'))


if __name__==('__main__'):
    app.secret_key='mysecret'
    app.run(debug=True)
