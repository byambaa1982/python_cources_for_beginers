from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Add your own profile details here
    profile = {
        "name": "Your Name",
        "bio": "Aspiring Developer passionate about coding and creating awesome projects.",
        "profile_pic": "images/profile.png",
        "github": "https://github.com/yourgithub",
        "projects": [
            {"name": "Project 1", "link": "https://yourprojectlink1.com"},
            {"name": "Project 2", "link": "https://yourprojectlink2.com"},
            {"name": "Project 3", "link": "https://yourprojectlink3.com"}
        ]
    }
    return render_template("index.html", profile=profile)

if __name__ == "__main__":
    app.run(debug=True)
