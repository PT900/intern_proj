import regex as re
import json

def find_json_in_file(file_path):
    json_objects = []

    with open(file_path, 'r') as file:
        text = file.read()

        # Regex to find JSON objects
        json_pattern = r'\{(?:[^{}]|(?R))*\}'

        matches = re.findall(json_pattern, text, flags=re.DOTALL)

        for match in matches:
            try:
                json_obj = json.loads(match)
                json_objects.append(json_obj)
            except json.JSONDecodeError:
                pass

    return json_objects

file_path = r'C:\Users\peat2\kbtg\test_json.txt'
json_objects = find_json_in_file(file_path)

for idx, obj in enumerate(json_objects, start=1):
    print(f"JSON Object {idx}:\n{json.dumps(obj, indent=4)}\n")

print(f"Total JSON objects found: {len(json_objects)}")
