import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='vayrynen2024',
    autocommit=True
)


def iso_code_to_name(iso_code):
    sql = f"SELECT name FROM country WHERE iso_country = '{iso_code}'"
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    return result[0]


def amount_of_airports_by_type_in_country(airport_type, iso_code):
    sql = f"SELECT type FROM airport WHERE iso_country = '{iso_code}' AND type = '{airport_type}'"
    cursor = conn.cursor()
    cursor.execute(sql)
    cursor.fetchall()
    return f"{airport_type}: {cursor.rowcount}"


def types_of_airport(list1):
    sql = 'SELECT DISTINCT type from airport'
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for types1 in result:
        list1.append(types1[0])


def iso_codes(list1):
    sql = 'SELECT DISTINCT iso_country from country'
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for types1 in result:
        list1.append(types1[0])


def list_amount_of_airports_by_type(code1):
    a = []
    types_of_airport(a)
    print(f"\nAmount of airports by type in {iso_code_to_name(code1)}:")
    for types in a:
        print(amount_of_airports_by_type_in_country(types, code1))


codes = []
iso_codes(codes)
code = ""

while code not in codes:
    code = input("ISO-code: ").upper()

list_amount_of_airports_by_type(code)
