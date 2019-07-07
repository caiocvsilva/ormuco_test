from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse

from text_insights import get_text_insights


app = Flask(__name__)
api = Api(app)

class Text_insights(Resource):
    def get(self, search_string):
        """
        Receives the GET XXXX and calls the function to search the keyword received
        
        Params:
        - search_string: String with the search term to be used
        
        Returns:
        - Json contaning the results found
        """
        result = get_text_insights(search_string)
        return result

api.add_resource(Text_insights, "/search/<string:search_string>")

if __name__ == '__main__':
     app.run(host='0.0.0.0')