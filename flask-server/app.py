from flask import Flask, request
from flask_restful import Api, Resource
import pymongo
from pymongo import MongoClient
import json 
from bson import json_util
from flask_cors import CORS, cross_origin

app = Flask(__name__) # this is the common convention for initilizing the flask app with __name__, dont know why
api = Api(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
cluster = MongoClient("mongodb+srv://secretuser:secret@cluster0.fewua.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["learning"]
collection = db["learning"]

##################
class Hello(Resource):
    def get(self):
        results = collection.find({})
    # this is cursor object

    #iterate over to get a list of dicts
        result = [doc for doc in results]

    #serialize to json string
        result_json_string = json.dumps(result,default=json_util.default)

        return json.loads(result_json_string)


class Create(Resource):
    def post(self, value, countId):
        collection.insert_one({"_id": countId, "value": value})

class incValue(Resource):
    def put(self, countId):
        collection.update_one({"_id": countId}, {"$inc": {"value": 1}})

class decValue(Resource):
    def put(self, countId):
        collection.update_one({"_id": countId}, {"$inc": {"value": -1}})

api.add_resource(Hello, "/api/hello")
api.add_resource(Create, "/api/hello/<int:value>/<int:countId>") # the actual api call here with which method when at which url
api.add_resource(incValue, "/api/hello/inc/<int:countId>")
api.add_resource(decValue, "/api/hello/dec/<int:countId>")

@app.route("/")
def hello_world():
    return "hello world"

############# end of controllers and routes##########################

######## run the server################
# debug = true only when youre developing, not in production
# the way to start running the server is this way, dont know why.
if __name__ == "__main__": 
    app.run(host="0.0.0.0", debug=True) 
