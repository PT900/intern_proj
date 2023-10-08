import json
import regex as re
import random

# Setup request file path here
file_path = r'C:\Users\peat2\kbtg\test_json.txt'

# Function to save file as file_name and fufill content inside text file
def save_to_file(file_name, content, default_head, default_tail):
    with open(file_name, 'w') as file:
        file.write(default_head)
        file.write(content)
        file.write(default_tail)

# Function to random the t[100000-999999] for realistically
def generate_random_t1_inf():
    return f"t{random.randint(100000, 999999):6}.inf"

# Function to format JSON into expect result
def format_json(json_input):
    # JSON format
    formatted_json = json.dumps(json_input, indent=0, ensure_ascii=False)
    # Replace the tabs with spaces to remove tabbing
    formatted_json = formatted_json.replace('\t', '')
    # Add \r\n to eol before newline
    formatted_json = formatted_json.replace('\n', '\\r\\n\n')
    # Escape double quotes
    formatted_json = formatted_json.replace('"', r'\"')
    # Add double quotes to first and last except the first line
    lines = formatted_json.splitlines()

    formatted_json = lines[0] + '"\n'
    formatted_json += '\n'.join(f'\t\t"{line}"' for line in lines)

    return formatted_json

# Function to edit the JSON request from input into VUGen web_rest command
def edit_request_with_input(json_input):
    # Format the JSON input with proper indentation
    formatted_json = format_json(json_input)

    # Generate random t1.inf
    t_inf = generate_random_t1_inf()

    request_string = ('\tweb_rest("POST: {URL}",\n'
                        '\t\t"URL={URL}",\n'
                        '\t\t"Method=POST",\n'
                        '\t\t"EncType=raw",\n'
                        f'\t\t"Snapshot={t_inf}",\n'
                        f'\t\t"Body={formatted_json},\n'
                        '\t\tHEADERS,\n'
                        '\t\t"Name=Content-Type", "Value=application/json", ENDHEADER,\n'
                        '\t\tLAST);')

    return request_string

# Function to find json request in .txt file
def find_json_in_txt_file(file_path):
    json_strings = []

    with open(file_path, 'r') as file:
        text = file.read()

        # Regex to find JSON objects
        json_pattern = r'\{(?:[^{}]|(?R))*\}'

        matches = re.findall(json_pattern, text, flags=re.DOTALL)
        json_strings.extend(matches)

    return json_strings

# Default part
if __name__ == "__main__":
    json_strings = find_json_in_txt_file(file_path)

    for i, json_str in enumerate(json_strings):
        # Default head of Action file
        default_head_string = (f'Action{i + 1}()\n'
                                '{\n'
                                '\tweb_set_max_html_param_len("100000");\n\n'
                                '\tweb_set_sockets_option("SSL_VERSION", "AUTO");\n\n'
                                f'\tlr_start_transaction("Transaction_Name_{i + 1}");\n\n'
                                '\t// Status Code\n'
                                '\tweb_reg_save_param_ex(\n'
                                '\t\t"ParamName=statusCode",\n'
                                '\t\t"LB=\\"responseHeader\\":{\\"status\\":\\"",\n'
                                '\t\t"RB=\\"",\n'
                                '\t\t"Ordinal=1",\n'
                                '\t\tSEARCH_FILTERS,\n'
                                '\t\tLAST);\n\n')

        default_tail_string = ('\n\n\t// lr_convert_string_encoding(lr_eval_string("{jsonMessage_6}"),LR_ENC_UTF8,LR_ENC_SYSTEM_LOCALE,"ResponseDataUTF8");\n\n'
                                '\tif ((strcmp(lr_eval_string("S"),lr_eval_string("{statusCode}"))) == 0) {\n\n'
                                f'\t\tlr_end_transaction("Transaction_Name_{i + 1}", LR_PASS);\n\n'
                                '\t} else {\n\n'
                                f'\t\tlr_error_message("Transaction_Name_{i + 1} Error Descripstion %s", '
                                'lr_eval_string("{jsonMessage_2}")\n'
                                f'\t\tlr_end_transaction("Transaction_Name_{i + 1}", LR_FAIL);\n\n'
                                '\t\tlr_exit(LR_EXIT_ITERATION_AND_CONTINUE, LR_AUTO);\n\n'
                                '\t}\n\n'
                                '\treturn 0;\n'
                                '}')

        # Format the JSON input with proper indentation
        try:
            paresd_json = json.loads(json_str)
        except json.JSONDecodeError:
            print("Error: Invalid JSON format. Please provide valid JSON input.")
            continue

        # Edit json from text file into VUGen web_rest format
        updated_request_string = edit_request_with_input(paresd_json)

        if updated_request_string:
            save_to_file(f"Action{i + 1}.txt", updated_request_string, default_head_string, default_tail_string)
            print(f"Request for JSON {i + 1} has been saved to 'Action{i + 1}.txt'.")
