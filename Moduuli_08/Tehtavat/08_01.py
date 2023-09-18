import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='vayrynen2024',
    autocommit=True
)


def get_airport_name_and_municipality_by_icao_code(icao):
    sql = f"SELECT name, municipality FROM airport WHERE ident = '{icao}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    # print(result)
    if cursor.rowcount > 0:
        return f"Lentokentän {icao} nimi on {result[0]}, ja sen sijaintikunta on {result[1]}."
    else:
        return "Virheellinen ICAO-koodi."


code = input("Anna ICAO-koodi: ")
print(get_airport_name_and_municipality_by_icao_code(code))
