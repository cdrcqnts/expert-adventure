from flask import Flask
from pymongo import MongoClient
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")  # //db complies to db folder
db = client['test-database']
userNum = db['user-num']

userNum.insert({
    'visits': 0
})

# posts = db.posts
# post = {"author": "Mike",
#         "text": "My first blog post!",
#         "tags": ["mongodb", "python", "pymongo"],
#         "date": datetime.datetime.utcnow()}
# post_id = posts.insert_one(post).inserted_id


class Visit(Resource):
    def get(self):
        prev_num = userNum.find({})[0]['visits']
        new_num = prev_num + 1

        userNum.update({}, {'$set': {'visits': new_num}})
        return str("Hello user " + str(new_num))


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')
api.add_resource(Visit, '/visit')

if __name__ == '__main__':
    app.run(debug=True)
