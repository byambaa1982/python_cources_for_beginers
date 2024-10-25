from flask import Flask, render_template, request

import pandas as pd
import sqlite3


app = Flask(__name__)

@app.route('/second')
def hello_world():
    return render_template('index.html', message='Hello, World!')

@app.route('/form', methods=['GET', 'POST'])
def render_form():
    message = ''
    if request.method == 'POST':
        text = request.form.get('text')
        if request.form['submit_button'] == 'Lowercase':
            message = text.lower()
        elif request.form['submit_button'] == 'Capital':
            message = text.upper()
        elif request.form['submit_button'] == 'Byamba':
            message = "Hi Byamba"
    return render_template('form.html', message=message)

@app.route('/')
def about():
    conn = sqlite3.connect('titanic.sqlite')
    # Read the 'titanic' table into a pandas DataFrame
    df = pd.read_sql('SELECT Name, Age FROM titanic', conn)
    name = df["Name"][0]
    age = df["Age"][0]
    print(name, age)
    return render_template('about.html',
                            jinja_title = name,
                            jinja_about = age
                            )

if __name__ == '__main__':
    app.run(debug=True)
