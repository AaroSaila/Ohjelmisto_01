import json
from flask import Flask, request, Response

app = Flask(__name__)


@app.route('/')
def get_root():
    return "Moro"


# Example query: http://localhost:3000/kukkuu?name=Matti&age=25
@app.route('/kukkuu')
def get_kukkuu():
    # print(request.args)
    name = request.args.get("name")
    age = request.args.get("age")
    return f"Kukkuu {name} {age}"


# Example query: http://localhost:3000/kukkuu/Matti/25
@app.route('/kukkuu/<name>/<age>')
def get_kukkuu_v2(name, age):
    # print(request.args)
    return f"Kukkuu {name} {age}"


# Example query: http://localhost:3000/multiply/5
# Example response in json: '{input_num: 25, result: 25}'
# input_num must be between 0-100
@app.route('/multiply/<num>')
def multiply(num):
    # TODO: refactor code: create response object and return it only once
    try:
        num = int(num)
    except ValueError:
        response_data = {"msg": "Input is not an integer", "input_num": num}
        # convert python dictionary to json format "manually"
        response_data = json.dumps(response_data)
        # setting up a status code for response, needs Response object to be created
        response = Response(response=response_data, status=400, mimetype='application/json')
        return response
    if 0 < num < 100:
        result = num * num
        response_data = {"msg": "Calculation Done", "input_num": num, "result": result}
        return response_data
    else:
        response_data = {"msg": "Input out of bounds", "input_num": num}
        # convert python dictionary to json format "manually"
        response_data = json.dumps(response_data)
        # setting up a status code for response, needs Response object to be created
        response = Response(response=response_data, status=400, mimetype='application/json')
        return response


@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status": "404",
        "teksti": "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
