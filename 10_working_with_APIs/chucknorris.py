import requests

# API URL
url = "https://dog.ceo/api/breeds/image/random"

# Sending GET request
response = requests.get(url)

# Check the response
if response.status_code == 200:
    print("Success!")
    r = response.json()  # Parse the JSON response
    print(r)
    
    # Extract the image URL
    image_url = r.get("message")  # The "message" key contains the image URL
    
    if image_url:
        # Download the image
        image_response = requests.get(image_url, stream=True)
        
        if image_response.status_code == 200:
            # Save the image to a file
            with open("random_dog_image.png", "wb") as file:
                for chunk in image_response.iter_content(1024):
                    file.write(chunk)
            print("Image saved as random_dog_image.png")
        else:
            print("Failed to download the image.")
    else:
        print("No image URL found in the response.")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
