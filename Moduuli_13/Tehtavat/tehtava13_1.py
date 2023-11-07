import json
from flask import Flask, Response

app = Flask(__name__)


def is_prime(num):
    if num <= 1:
        return False
    else:
        for x in range(2, num):
            if num % x == 0:
                return False
    return True


@app.route('/alkuluku/<input_num>')
def get_prime(input_num):
    try:
        input_num = int(input_num)
        isprime = is_prime(input_num)
        response_data = json.dumps({"Number": input_num, "isPrime": isprime})
        code = 200

    except ValueError:
        code = 400
        response_data = json.dumps({"Error": "ValueError", "Error Code": code})

    response = Response(response=response_data, status=code, mimetype="application/json")
    return response


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000, use_reloader=True)
