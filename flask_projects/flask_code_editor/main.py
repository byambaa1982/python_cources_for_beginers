from flask import Flask, render_template, request
import markdown
import io
import sys

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    code = None
    markdown_code = None
    if request.method == "POST":
        code = request.form.get("code")
        result = execute_code_with_output(code)
        markdown_code = markdown.markdown(f"```python\n{code}\n```", extensions=["fenced_code"])
        print(result[1])
    return render_template("index.html", code=code, result=result, markdown_code=markdown_code)

def execute_code_with_output(code):
    """Execute Python code and capture both result and printed output."""
    try:
        exec_globals = {}
        output_buffer = io.StringIO()  # Redirect stdout
        sys.stdout = output_buffer
        exec(code, exec_globals)
        sys.stdout = sys.__stdout__  # Restore original stdout
        output = output_buffer.getvalue()  # Capture printed output
        result = exec_globals.get('result', 'Code executed successfully!')
        return result, output
    except Exception as e:
        sys.stdout = sys.__stdout__  # Restore stdout in case of an error
        return f"Error: {str(e)}", None

if __name__ == "__main__":
    app.run(debug=True)
