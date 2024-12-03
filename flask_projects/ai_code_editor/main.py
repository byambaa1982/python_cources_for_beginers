from flask import Flask, render_template, request
import io
import sys
import os
import json

app = Flask(__name__)

# Filepath for the JSON file
JSON_FILE = "output.json"

def read_latest_task(file_path):
    """
    Read the latest task from the JSON file.
    """
    try:
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                tasks = json.load(file)
                if tasks:
                    return tasks[-1]  # Return the latest task
        return None  # If the file doesn't exist or is empty
    except Exception as e:
        print(f"Error reading the JSON file: {e}")
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    """
    Main route to display the latest task instructions and execute the submitted code.
    """
    result = None
    output = None
    instruction = None  # Initially set to None

    # Handle actions based on button clicked
    if request.method == "POST":
        action = request.form.get("action")  # Action to determine button clicked
        code = request.form.get("code")  # Get the submitted code

        if action == "show_task":
            # Read and display the task from the JSON file
            instruction = read_latest_task(JSON_FILE)

        elif action == "run_code":
            # Execute the submitted code and get the result/output
            result, output = execute_code_with_output(code)

    return render_template(
        "index.html",
        instruction=instruction,
        result=result,
        output=output,
        code=request.form.get("code", ""),  # Preserve user code input
    )

def execute_code_with_output(code):
    """
    Execute Python code and capture both the returned result and printed output.
    """
    try:
        exec_globals = {}
        output_buffer = io.StringIO()  # Redirect stdout
        sys.stdout = output_buffer
        exec(code, exec_globals)  # Execute the code
        sys.stdout = sys.__stdout__  # Restore original stdout
        output = output_buffer.getvalue()  # Get printed output
        result = exec_globals.get("result", "Code executed successfully!")  # Capture 'result'
        return result, output
    except Exception as e:
        sys.stdout = sys.__stdout__  # Restore stdout in case of an error
        return f"Error: {str(e)}", None


if __name__ == "__main__":
    app.run(debug=True)
