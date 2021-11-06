from flask import Flask, render_template, request, redirect, jsonify, url_for
from flask import make_response, flash
from flask import session as login_session
import pymongo

app = Flask(__name__)

'''
docker run -d  --name mongo -p 27017:27017 -v /Users/daniel.lin/Daniel/alpha/db:/data/db -e MONGO_INITDB_ROOT_USERNAME=mongoadmin -e MONGO_INITDB_ROOT_PASSWORD=secret mongo
'''

mongo_client = pymongo.MongoClient("mongodb://localhost:27017/",
                                    username='mongoadmin',
                                    password='secret')
db=mongo_client.test

user = db.user

@app.route('/user/')
def showUser():
    """Show all Users"""
    return jsonify(users)

'''
curl -X POST http://192.168.11.6:5000/user/new/ -H "content-Type: application/json" -d '{"name":"Daniel"}'
'''
@app.route('/user/new/', methods=['GET', 'POST'])
def newUser():
    """Add new User"""
    if request.method == 'POST':
        payload = request.json
        newUser = {
            'name': request.json['name']
        }
        insert_result = user.insert_one(newUser)

        Queryresult = user.find_one({'name': request.json['name']})
        return Queryresult



if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
