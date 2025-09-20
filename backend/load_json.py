import json

# loads blog.json as a dictionary
def load_json_as_dict(file_path):
    try:
        with open('blog.json', 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: File not found at '{file_path}'")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{file_path}'")
        return None