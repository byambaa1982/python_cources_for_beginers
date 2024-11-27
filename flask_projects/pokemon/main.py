from flask import Flask, render_template, request
import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Fetch list of Pokémon names
def fetch_pokemon_names():
    url = "https://pokeapi.co/api/v2/pokemon?limit=1000"  # Fetch 1000 Pokémon names
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return [pokemon['name'] for pokemon in data['results']]
    else:
        return []

# Fetch Pokémon sprite URL
def fetch_pokemon_sprite(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    if response.status_code == 200:
        raw_data = response.json()
        return raw_data['sprites']['front_default']
    else:
        return None

# Save sprite image locally for rendering
def save_sprite_image(sprite_url, filename):
    response = requests.get(sprite_url)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        image.save(filename)
        return True
    return False

@app.route("/", methods=["GET", "POST"])
def index():
    pokemon_names = fetch_pokemon_names()
    selected_pokemon = None
    sprite_path = None

    if request.method == "POST":
        selected_pokemon = request.form.get("pokemon_name")
        sprite_url = fetch_pokemon_sprite(selected_pokemon)
        if sprite_url:
            sprite_path = f"static/{selected_pokemon}.png"
            save_sprite_image(sprite_url, sprite_path)
        else:
            sprite_path = None

    return render_template("index.html", pokemon_names=pokemon_names, selected_pokemon=selected_pokemon, sprite_path=sprite_path)

if __name__ == "__main__":
    # Ensure the static directory exists for saving images
    os.makedirs("static", exist_ok=True)
    app.run(debug=True)
