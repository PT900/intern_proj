import regex as re
import json

def find_json_in_file(file_path):
    json_strings = []

    with open(file_path, 'r') as file:
        text = file.read()

        # Regex to find JSON objects
        json_pattern = r'\{(?:[^{}]|(?R))*\}'

        matches = re.findall(json_pattern, text, flags=re.DOTALL)

        # for match in matches:
        #     try:
        #         json_obj = json.loads(match)
        #         json_strings.append(json_obj)
        #     except json.JSONDecodeError:
        #         pass

        json_strings.extend(matches)

    return json_strings

file_path = r'C:\Users\peat2\kbtg\test_json.txt'
json_strings = find_json_in_file(file_path)

for idx, json_str in enumerate(json_strings, start=1):
    print(f"JSON Object {idx}:\n{json_str}\n")

print(f"Total JSON objects found: {len(json_strings)}")
