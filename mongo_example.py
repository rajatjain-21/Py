from flask import Flask
from flask_pymongo import PyMongo
import datetime

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'connect_to_mongo'
app.config['MONGO_URI'] = 'mongodb://rajat:rajatrishav@ds119078.mlab.com:19078/connect_to_mongo'

mongo = PyMongo(app)

@app.route('/add')
def add():
    user = mongo.db.users  #creates a collection named users in the database if it's not already there.
    user.insert({'name': 'Rajat', 'language':'Python'})
    user.insert({'name': 'Subham', 'language': 'C#'})
    user.insert({'name': 'Aman', 'language': 'C++'})
    user.insert({'name': 'Dewang', 'language': 'Python'})
    user.insert({'name': 'Sunidhi', 'language': 'Perl'})
    # data = [{'name':'Rajjo','language':'Ruby','date':str(datetime.datetime.now().date())},
    #         {'name': 'Vignesh', 'language': 'C', 'date': str(datetime.datetime.now().date())},
    #         {'name': 'Vibhor', 'language': 'Javascript', 'date': str(datetime.datetime.now().date())}
    #         ]
    # user.insert_many(data)
    return 'Added User!'

@app.route('/find')
def find():
    user = mongo.db.users
    dewang = user.find_one({'name':'Dewang'})
    return 'You found '+ dewang['name']+'. His favourite language is '+dewang['language']+'.'

@app.route('/update')
def update():
    user = mongo.db.users
    rajat = user.find_one({'name':'Rajat'})
    rajat['language'] = 'Go'
    user.save(rajat)
    return 'User updated!'

@app.route('/delete')
def delete():
    user = mongo.db.users
    sunidhi = user.find_one({'name':'Sunidhi'})
    user.remove(sunidhi)
    return 'User deleted!'

@app.route('/view')
def view():
    user = mongo.db.users
    str = "";
    for i in user.find():
        str+=i['name']+" is expert in "+i['language']+"<br>"
    return str


if __name__=='__main__':
    app.run(debug=True)









