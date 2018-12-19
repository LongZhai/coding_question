from flask import Flask
from flask_restful import Resource, Api
import search
app = Flask(__name__)
api = Api(app)


class SearchFunc(Resource):
    def get(self, search_input):
        return search.search_fun(search_input), 200


api.add_resource(SearchFunc, '/api/search/<string:search_input>')
# app.register_error_handler(400, handle_bad_request)


@app.route('/')
def home():
    return "search API"


if __name__ == '__main__':
    app.run(debug=True)
