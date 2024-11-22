import requests 


# API URL
url = "https://dog.ceo/api/breeds/image/random"  # Replace with your API endpoint


# Sending GET request
response = requests.get(url)

# Check the response
if response.status_code == 200:
    print("Success!")
    r = response.json()
    print(r)