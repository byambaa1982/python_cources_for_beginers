from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', message='Hello, World!')

@app.route('/form', methods=['GET', 'POST'])
def render_form():
    if request.method == 'POST':
        text = request.form.get('text')
        return render_template('index.html', message=text.lower())
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
