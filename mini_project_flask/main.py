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
@app.route('/posts', methods=['GET', 'POST'])
def submit_post():
    message = ""
    if request.method == 'POST':
        title = request.form['title']
        post_content = request.form['post']
        post_type = request.form['type']

        conn = sqlite3.connect('titanic.sqlite')
        cursor = conn.cursor()

        # Ensure the post table exists (you might want to modify or remove this part)
        cursor.execute('''CREATE TABLE IF NOT EXISTS post (id INTEGER PRIMARY KEY, title TEXT, post TEXT, type TEXT)''')

        # Insert the submitted form data into the post table
        cursor.execute("INSERT INTO post (title, post, type) VALUES (?, ?, ?)", (title, post_content, post_type))
        conn.commit()
        conn.close()

        message = "Post submitted successfully!"

    return render_template('form.html', message=message)

@app.route('/blogs')
def show_blogs():
    conn = sqlite3.connect('titanic.sqlite')
    cursor = conn.cursor()

    # Fetch all posts from the database
    cursor.execute("SELECT title, post, type FROM post")
    posts = cursor.fetchall()
    conn.close()

    # Format posts for rendering
    formatted_posts = [{"title": row[0], "content": row[1], "type": row[2]} for row in posts]

    return render_template('blog.html', posts=formatted_posts)

if __name__ == '__main__':
    app.run(debug=True)
