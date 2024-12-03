from chatgpt import answer_me
import json
import re


# Function to extract and load dictionaries
def extract_dictionaries(input_string):
    try:
        # Regex pattern to extract dictionaries starting with "type"
        pattern = r"\{\s*\"type\".*?\}"
        # Find all matches using re.DOTALL to handle multiline strings
        matches = re.findall(pattern, input_string, re.DOTALL)
        
        if not matches:
            raise ValueError("No valid dictionaries found in the input string.")
        
        # Parse each match as JSON
        parsed_dictionaries = [json.loads(match) for match in matches]
        return parsed_dictionaries

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


# Function to append data to a JSON file
def append_to_json_file(file_path, data):
    try:
        # Load existing data if the file exists
        try:
            with open(file_path, "r") as file:
                existing_data = json.load(file)
        except FileNotFoundError:
            existing_data = []

        # Append new data to the existing data
        if isinstance(data, list):
            existing_data.extend(data)
        else:
            existing_data.append(data)

        # Save the updated data back to the file
        with open(file_path, "w") as file:
            json.dump(existing_data, file, indent=4)
        print(f"Data successfully saved to {file_path}")
    except Exception as e:
        print(f"Error saving data to JSON file: {e}")


# Function to interact with ChatGPT and get tasks
def get_task_from_chatgpt(prompt, json_file="output.json"):
    input_string = answer_me(prompt)  # Replace with your actual API call
    
    # Append the input string to input.txt for logging
    try:
        with open("input.txt", "a") as file:
            file.write(input_string + "\n")
    except Exception as e:
        print(f"Error writing to input.txt: {e}")
    
    # Extract and load dictionaries
    output = extract_dictionaries(input_string)
    
    # Append the output to the JSON file
    append_to_json_file(json_file, output)
    
    # Print and return the output
    for task in output:
        print(task)
    return output
