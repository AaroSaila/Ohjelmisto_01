API_key = "404f93a3ca1a1e108fa623b09646cb76"
zip_code = "01390"
country_code = "FI"
request = (f"https://api.openweathermap.org/data/2.5/weather?zip={zip_code},{country_code}&appid={API_key}"
           f"&lang=fi&units=metric")
print(request)