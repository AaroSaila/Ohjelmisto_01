import mysql.connector

connection = mysql.connector.connect(
    host='localhost',  # localhost = 127.0.0.1
    port=3306,
    database='flight_game',
    user='root',
    password='vayrynen2024',
    autocommit=True
)
"""
cursor = connection.cursor()
cursor.execute("SELECT name, ident FROM airport WHERE iso_country = 'FI'")
result = cursor.fetchall()
print(cursor.rowcount)  # tulosrivien määrä
print(result)  # koko tulosjoukko listana
for airport in result:  # ident: yksi tulosjoukon rivi monikkona
    print(f"ICAO: {airport[1]}, nimi: {airport[0]}")
"""


def get_country_by_iso_code(iso_code):
    cursor = connection.cursor()
    sql = f"SELECT iso_country, name FROM country WHERE iso_country = '{iso_code}'"
    cursor.execute(sql)
    result = cursor.fetchone()  # hakee vain ensimmäisen tulosrivin
    if result:
        return result[1]
    else:
        return "No results"


country = get_country_by_iso_code("FI")
print(country)
country = get_country_by_iso_code(input("Syötä maakoodi: "))
print(country)
