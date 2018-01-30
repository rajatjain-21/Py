from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'filter_mongo'
app.config['MONGO_URI'] = 'mongodb://rajat:rajatrishav@ds119585.mlab.com:19585/filter_mongo'

mongo = PyMongo(app)

@app.route('/add')
def add():
    numbers = mongo.db.numbers  #creates a collection named users in the database if it's not already there.
    numbers.insert({'name': 'Rajat', 'number':1})
    numbers.insert({'name': 'Subham', 'number':2})
    numbers.insert({'name': 'Aman', 'number':3})
    numbers.insert({'name': 'Dewang', 'number':4})
    numbers.insert({'name': 'Sunidhi', 'number':5})
    # data = [{'name':'Rajjo','language':'Ruby','date':str(datetime.datetime.now().date())},
    #         {'name': 'Vignesh', 'language': 'C', 'date': str(datetime.datetime.now().date())},
    #         {'name': 'Vibhor', 'language': 'Javascript', 'date': str(datetime.datetime.now().date())}
    #         ]
    # user.insert_many(data)
    return 'Added User!'

@app.route('/')
def index():
    numbers = mongo.db.numbers
    results = numbers.find()
    output = ''
    for r in results:
        output+= r['name']+' - '+str(r['number'])+'<br>'
    return output

if __name__==('__main__'):
    app.run(debug=True)