import requests

# API URL
url = "https://pokeapi.co/api/v2/pokemon/ditto"  # Replace with your API endpoint


# Sending GET request
response = requests.get(url)

# Check the response
if response.status_code == 200:
    print("Success!")
    print(response.json())  # Assuming the API returns JSON
else:
    print(f"Error: {response.status_code}")
    print(response.text)