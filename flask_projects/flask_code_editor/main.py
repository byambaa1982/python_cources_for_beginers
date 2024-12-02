from flask import Flask, render_template, request
import markdown

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    code = None
    markdown_code = None
    if request.method == "POST":
        code = request.form.get("code")
        result = execute_code(code)
        markdown_code = markdown.markdown(f"```python\n{code}\n```", extensions=["fenced_code"])
    return render_template("index.html", code=code, result=result, markdown_code=markdown_code)

def execute_code(code):
    try:
        exec_globals = {}
        exec(code, exec_globals)  # Execute the student's code
        # Extract a 'result' variable if defined in the code, or return success message
        return exec_globals.get('result', 'Code executed successfully!')
    except Exception as e:
        # Return error message in case of an exception
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
