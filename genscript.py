import json
import sys

def save_to_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)

def edit_request_with_input(url, json_input, headers):
    request_string = ('web_rest("POST: my_url",\n'
                        '\t"URL=my_url",\n'
                        '\t"Method=POST",\n'
                        '\t"EncType=raw",\n'
                        '\t"Snapshot=t1.inf",\n'
                        f'\t"Body={json_input}\n\tHEADERS,",\n'
                        f'\t{headers});')

    updated_request_string = request_string.replace("my_url", url)

    return updated_request_string

if __name__ == "__main__":
    # Sample input URL, JSON request, and headers
    input_url = input("Input request url: ")
    input_json = input("Input request JSON: ")

    # Format the JSON input with proper indentation
    try:
        paresd_json = json.loads(input_json)
        formatted_json = json.dumps(paresd_json, indent=4, separators=(',', ': '))
    except json.JSONDecodeError:
        print("Error: Invalid JSON format. Please provide valid JSON input.")
    else:
        input_headers = '''"Name=Content-Type", "Value=application/json", ENDHEADER,\n\tLAST);'''

        updated_request_string = edit_request_with_input(input_url, input_json, input_headers)

        if updated_request_string:
            # print("Updated Request String:")
            # print(updated_request_string)

            save_to_file("output.txt", updated_request_string)
            print("Request has been saved to 'output.txt'.")

