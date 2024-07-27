from datetime import datetime
import re
import json
import subprocess
import random

def get_current_time_formatted():
    current_time = datetime.now()
    formatted_time = current_time.strftime("%m/%d/%y")
    return formatted_time


def clean_json(json_str):
    original = json_str
    attempt_count = 20  # Number of attempts to fix JSON
    attempt = 0

    while attempt < attempt_count:
        attempt += 1
        try:
            # Check and remove markdown for JSON
            if re.match(r'```json\s*', json_str) and re.search(r'```\s*$', json_str):
                json_str = re.sub(r'```json\s*', '', json_str)  # Remove starting markdown ```json
                json_str = re.sub(r'```\s*$', '', json_str)     # Remove ending markdown ```

            # Fix escaping characters for JSON
            json_str = re.sub(r'(?<!\\)\\', r'\\\\', json_str)  # Fix single backslashes
            json_str = re.sub(r'\\(?!["\\/bfnrtu])', r'\\\\', json_str)  # Fix other escape sequences

            # Attempt to parse the JSON to verify if it's valid
            json_obj = json.loads(json_str)
            json_str = json.dumps(json_obj, indent=4)
            return {"status": "success", "cleaned_json": json_str}

        except json.JSONDecodeError as e:
            if attempt == attempt_count:
                return {"status": "error", "error_message": str(e), "original": original}

            try:
                # "Expecting , delimiter: line 34 column 54 (char 1158)"
                # position of unexpected character after '"'
                unexp = int(re.findall(r'\(char (\d+)\)', str(e))[0])
                # position of unescaped '"' before that
                unesc = json_str.rfind(r'"', 0, unexp)
                json_str = json_str[:unesc] + r'\"' + json_str[unesc+1:]
                # position of corresponding closing '"' (+2 for inserted '\')
                closg = json_str.find(r'"', unesc + 2)
                json_str = json_str[:closg] + r'\"' + json_str[closg+1:]
            except Exception as inner_e:
                return {"status": "error", "error_message": str(inner_e), "original": original}

    return {"status": "error", "error_message": "Reached maximum attempts", "original": original}

# Remove all empty spaces to make things easier below
def remove_spaces(json_str):
    json_str = json_str.replace('" :', '":').replace(': "', ':"').replace('"\n', '"').replace('" ,', '",').replace(', "', ',"')
    # First remove the " from where it is supposed to be.
    json_str = re.sub(r'\\"', '"', json_str)
    json_str = re.sub(r'{"', '{`', json_str)
    json_str = re.sub(r'"}', '`}', json_str)
    json_str = re.sub(r'":"', '`:`', json_str)
    json_str = re.sub(r'":\[', '`:[', json_str)
    json_str = re.sub(r'":\{', '`:{', json_str)
    json_str = re.sub(r'":([0-9]+)', '`:\\1', json_str)
    json_str = re.sub(r'":(null|true|false)', '`:\\1', json_str)
    json_str = re.sub(r'","', '`,`', json_str)
    json_str = re.sub(r'",\[', '`,[', json_str)
    json_str = re.sub(r'",\{', '`,{', json_str)
    json_str = re.sub(r',"', ',`', json_str)
    json_str = re.sub(r'\["', '[`', json_str)
    json_str = re.sub(r'"\]', '`]', json_str)
    # Backslash all double quotes (")
    json_str = re.sub(r'"', '\\"', json_str)
    # Put back all the " where it is supposed to be.
    json_str = re.sub(r'\`', '\"', json_str)
    return json_str

# Combine both functions
def combined_clean_json(json_str):
    cleaned_str = clean_json(json_str)
    if cleaned_str["status"] == "success":
        cleaned_str["cleaned_json"] = remove_spaces(cleaned_str["cleaned_json"])
    return cleaned_st

def return_original_error(original):
    try:
        json_obj = json.loads(original)
        json_str = json.dumps(json_obj, indent=4)
        return {"status": "success", "cleaned_json": original}
    except json.JSONDecodeError as e:
        return {"status": "error", "error_message": str(e)}


def split_messages(messages, max_length):
    """
    Splits the messages into chunks that fit within the maximum token length.

    Args:
        messages (list): List of messages.
        max_length (int): Maximum length of tokens.

    Returns:
        list: List of message chunks.
    """
    chunks = []
    current_chunk = []
    current_length = 0

    for message in messages:
        message_length = len(message['content'].split())
        if current_length + message_length > max_length:
            chunks.append(current_chunk)
            current_chunk = []
            current_length = 0

        current_chunk.append(message)
        current_length += message_length

    if current_chunk:
        chunks.append(current_chunk)

    return chunks

def get_available_simulator_details():
    try:
        # Run the xcrun command to get a list of simulators in JSON format
        result = subprocess.run(
            ["xcrun", "simctl", "list", "devices", "--json"],
            capture_output=True,
            text=True,
            check=True
        )

        # Parse the JSON output
        devices = json.loads(result.stdout)

        # Extract detailed information of the available iOS simulators
        available_simulator_details = []
        for device_type in devices['devices']:
            # Filter for iOS simulators only
            if 'iOS' in device_type:
                for device in devices['devices'][device_type]:
                    if device.get('isAvailable', False):
                        details = {
                            'name': device.get('name', 'Unknown'),
                            'state': device.get('state', 'Unknown'),
                            'udid': device.get('udid', 'Unknown'),
                            'device_type': device_type
                        }
                        available_simulator_details.append(details)

        return available_simulator_details

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while fetching the simulator details: {e}")
        return []

def get_preferred_simulator_uuid():
    available_simulators = get_available_simulator_details()

    # Filter for booted simulators
    booted_simulators = [sim for sim in available_simulators if sim['state'] == 'Booted']

    if booted_simulators:
        chosen = random.choice(booted_simulators)
        print(f"Using: {chosen}")
        udid = chosen['udid']
        return udid

    # If no simulators are booted, filter for shutdown simulators in the iPhone range
    shutdown_iphones = [sim for sim in available_simulators if sim['state'] == 'Shutdown' and 'iPhone' in sim['name']]

    if shutdown_iphones:
        chosen = random.choice(shutdown_iphones)
        print(f"Using: {chosen}")
        udid = chosen['udid']
        return udid

    return None
