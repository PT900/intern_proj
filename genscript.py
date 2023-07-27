# Necessary library to formatting JSON request
import json
import random

# Function to save file as file_name and fufill content inside text file
def save_to_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)

# Function to random the t[100000-999999] for reality
def generate_random_t1_inf():
    return f"t{random.randint(100000, 999999):6}.inf"

# Function to format JSON into expect result
def format_json(json_input):
    formatted_json = json.dumps(json_input, indent=4).replace('\n', '\\r\\n\n\t')

    return formatted_json

# Function to edit the JSON request from input into LRE web_rest command
def edit_request_with_input(url, json_input, headers):
    # Format the JSON input with proper indentation
    formatted_json = format_json(json_input)

    # Generate random t1.inf
    t_inf = generate_random_t1_inf()

    request_string = (f'web_rest("POST: {url}",\n'
                        f'\t"URL={url}",\n'
                        f'\t"Method=POST",\n'
                        f'\t"EncType=raw",\n'
                        f'\t"Snapshot={t_inf}",\n'
                        f'\t"Body={formatted_json}",\n'
                        f'\tHEADERS,\n'
                        f'\t{headers}')

    # updated_request_string = request_string.replace("my_url", url)

    return request_string

# Default part
if __name__ == "__main__":
    # Input url
    input_url = input("Input request url: ")
    # Input JSON request as Multi-line content
    input_json = ''
    print("Input request JSON: ")
    while True:
        line = input()
        if not line:
            break
        input_json += line + '\n'

    # Escape double quotes in the JSON input
    # input_json = escape_quotes(input_json)

    # Remove newline at the end of JSON input
    input_json = input_json.rstrip()

    # Format the JSON input with proper indentation
    try:
        paresd_json = json.loads(input_json)
    except json.JSONDecodeError:
        print("Error: Invalid JSON format. Please provide valid JSON input.")
    else:
        input_headers = '''"Name=Content-Type", "Value=application/json", ENDHEADER,\n\tLAST);'''
        updated_request_string = edit_request_with_input(input_url, paresd_json, input_headers)

        if updated_request_string:
            save_to_file("output.txt", updated_request_string)
            print("Request has been saved to 'output.txt'.")

