import json
import re

# Function to extract and load dictionaries
def extract_dictionaries(file_path):
    dictionaries = []
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            # Use regex to find JSON-like dictionaries
            matches = re.findall(r'\{.*?\}', content, re.DOTALL)
            for match in matches:
                try:
                    # Attempt to parse JSON to validate it's a dictionary
                    dictionaries.append(json.loads(match))
                except json.JSONDecodeError:
                    continue
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    return dictionaries

# Example usage
input_file = "input.txt"
extracted_dicts = extract_dictionaries(input_file)
print("Extracted Dictionaries:")
for d in extracted_dicts:
    print(json.dumps(d, indent=4))
