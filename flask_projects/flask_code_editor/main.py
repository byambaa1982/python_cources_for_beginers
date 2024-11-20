from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_code', methods=['POST'])
def submit_code():
    code = request.form.get('code')  # Get the submitted code
    result = execute_code(code)  # Run the code and get the result
    # Prepare the response
    response = {"student_code": code, "result": result}
    return render_template('index.html', code=code, response=response)

def execute_code(code):
    try:
        exec_globals = {}
        exec(code, exec_globals)  # Execute the user's code
        return exec_globals.get('result', 'Code executed successfully!')
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)

