import mysql.connector
from geopy import distance

conn = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='vayrynen2024',
    autocommit=True
)


def airport_coordinates(ident):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{ident}'"
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    return result


def airport_distance(airport3, airport4):
    airport3 = airport_coordinates(airport3)
    airport4 = airport_coordinates(airport4)
    distance1 = distance.distance(airport3, airport4).km
    return distance1


def icao_codes(list1):
    sql = 'SELECT DISTINCT ident from airport'
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for types1 in result:
        list1.append(types1[0])


icaos = []
icao_codes(icaos)


airport1 = input("ICAO of 1. airport: ").upper()
while airport1 not in icaos:
    airport1 = input("Invalid ICAO-code. Enter ICAO of 1. airport: ").upper()
airport2 = input("ICAO of 2. airport: ").upper()
while airport2 not in icaos:
    airport2 = input("Invalid ICAO-code. Enter ICAO of 2. airport: ").upper()

print(f"The distance between {airport1} and {airport2} is:\n {(airport_distance(airport1, airport2)):.0f} km")
