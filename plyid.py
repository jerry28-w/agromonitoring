import requests

# Replace 'YOUR_API_KEY' with your actual Agromonitoring API key
API_KEY = '8e616fc17b0fd551dffd01410cde668d'

# Construct the API request URL
url = 'http://api.agromonitoring.com/agro/1.0/polygons'

# Set up the headers
headers = {
    'Content-Type': 'application/json',
}

# Define the GeoJSON code for the region around Ganeshpur road
geo_json = {
   "name": "Ganeshpur Road Area",
   "geo_json": {
      "type": "Feature",
      "properties": {},
      "geometry": {
         "type": "Polygon",
         "coordinates": [
            [
                [74.479, 15.873],
                [74.493, 15.873],
                [74.493, 15.859],
                [74.479, 15.859],
                [74.479, 15.873]
            ]
         ]
      }
   }
}


# Send the API request
response = requests.post(url, json=geo_json, headers=headers, params={'appid': API_KEY})

# Check if the request was successful (status code 201)
if response.status_code == 201:
    # Parse JSON response
    data = response.json()
    # Extract the polyid of the created polygon
    poly_id = data['id']
    print("Polygon created successfully. PolyID:", poly_id)
else:
    # Print error information
    print('Error:', response.status_code)
    print(response.content)
