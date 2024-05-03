import requests
import datetime

# Replace 'YOUR_API_KEY' with your actual Agromonitoring API key
API_KEY = '8e616fc17b0fd551dffd01410cde668d'

# Replace 'YOUR_POLY_ID' with the ID of the polygon you want to retrieve soil data for
POLY_ID = '65ec2b4664f6653b44c8ed1c'

# Construct the API request URL
url = f'http://api.agromonitoring.com/agro/1.0/soil?polyid={POLY_ID}&appid={API_KEY}'

# Send the API request
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse JSON response
    data = response.json()
    
    # Convert time of data calculation to human-readable format
    dt_readable = datetime.datetime.utcfromtimestamp(data['dt']).strftime('%Y-%m-%d %H:%M:%S')

    # Convert temperature from Kelvin to Celsius
    t10_celsius = round(data['t10'] - 273.15, 2)
    t0_celsius = round(data['t0'] - 273.15, 2)

    # Convert soil moisture from m3/m3 to percentage
    soil_moisture_percent = round(data['moisture'] * 100, 2)

    print('Soil Conditions:')
    print(f"Time of data calculation: {dt_readable} (UTC)")
    print(f"Temperature on the 10 centimeters depth: {t10_celsius} degCelsius")
    print(f"Soil moisture: {soil_moisture_percent}%")
    print(f"Surface temperature: {t0_celsius} degCelsius")

else:
    # Print error information
    print('Error:', response.status_code)
    print(response.content)
