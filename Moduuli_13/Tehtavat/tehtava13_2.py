import json
import mysql.connector
from flask import Flask, Response

app = Flask(__name__)

mydb = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='vayrynen2024',
    database='flight_game'
)

my_cursor = mydb.cursor()


class AirportNotFound(Exception):
    """Raised when no airport can be found in database"""
    pass


# returns tuple (**IDENT**, **NAME**, **MUNICIPALITY**)
def get_airport_from_db(icao):
    sql = f"SELECT ident, name, municipality FROM airport WHERE ident=%s"
    my_cursor.execute(sql, (icao, ))
    result = my_cursor.fetchone()
    if result:
        return result
    else:
        raise AirportNotFound


@app.route('/kenttä/<input_airport>')
def get_airport(input_airport):
    try:
        airport = get_airport_from_db(input_airport)
        response_data = json.dumps({"ICAO": airport[0], "Name": airport[1], "Municipality": airport[2]})
        code = 200

    except AirportNotFound:
        code = 404
        response_data = json.dumps({"ERROR": "Airport not Found", "Code": code})

    except ValueError:
        code = 400
        response_data = json.dumps({"ERROR": "Invalid Input", "Code": code})

    response = Response(response=response_data, status=code, mimetype="application/json")
    return response


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000, use_reloader=True)
