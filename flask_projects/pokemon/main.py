from flask import Flask, render_template, request, Response
import requests

app = Flask(__name__)

# Fetch list of Pokémon names
def fetch_pokemon_names():
    url = "https://pokeapi.co/api/v2/pokemon?limit=1000"
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

@app.route("/", methods=["GET", "POST"])
def index():
    pokemon_names = fetch_pokemon_names()
    selected_pokemon = None
    sprite_url = None

    if request.method == "POST":
        selected_pokemon = request.form.get("pokemon_name")
        sprite_url = fetch_pokemon_sprite(selected_pokemon)

    return render_template(
        "index.html",
        pokemon_names=pokemon_names,
        selected_pokemon=selected_pokemon,
        sprite_url=sprite_url,
    )

@app.route("/sprite/<pokemon_name>")
def sprite(pokemon_name):
    sprite_url = fetch_pokemon_sprite(pokemon_name)
    if sprite_url:
        response = requests.get(sprite_url)
        if response.status_code == 200:
            return Response(response.content, mimetype="image/png")
    return "Sprite not found", 404

if __name__ == "__main__":
    app.run(debug=True)
