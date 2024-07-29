#!/usr/bin/env python3

#!/data/data/com.termux/files/usr/bin/python
import argparse
import base64
import json
import os,sys
from datetime import datetime
import subprocess
import prompt_toolkit
from prompt_toolkit import prompt

# Determine the home directory and create ~/.termux/ if it doesn't exist
home_directory = os.path.expanduser("~")
key_dir = os.path.join(home_directory, ".keyguard")
if not os.path.exists(key_dir):
    os.makedirs(key_dir)

# Load existing keys from the file or initialize an empty dictionary
api_keys_path = os.path.join(key_dir, 'api_keys.json')
try:
    with open(api_keys_path, 'r') as file:
        api_keys = json.load(file)
except FileNotFoundError:
    api_keys = {}

def die(message):
    red = "\033[31m"
    reset = "\033[0m"
    print(f"[{red}warning{reset}] {message}")

def info(message):
    green = "\033[32m"
    r = "\033[0m"
    print(f"[{green}INFO{r}] {message}")

def text_(text):
    try:
     while True:
       user_input = prompt(text)
       if user_input == "":
             continue
       return user_input
    except KeyboardInterrupt:
       die("User canceled the progress")
       sys.exit(1)

def encrypt_key(key):
    return base64.b64encode(key.encode()).decode()

def decrypt_key(encoded_key):
    return base64.b64decode(encoded_key).decode()

def store_key(service, key, description):
    if service not in api_keys:
        api_keys[service] = []
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    api_keys[service].append({"key": encrypt_key(key), "description": description, "date": now})

# Modify the modify_key function to include the date

def modify_key(service, index, new_key, new_description):
    if service in api_keys and 0 <= index < len(api_keys[service]):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        api_keys[service][index] = {"key": encrypt_key(new_key), "description": new_description, "date": now}
        info("Key modified successfully.")
        save_keys_to_file()
    else:
        die("Invalid index or service not found.")

def transfer_key(source_service, destination_service, index):
    if source_service in api_keys and 0 <= index < len(api_keys[source_service]):
        key_info = api_keys[source_service].pop(index)
        key_info['date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if destination_service not in api_keys:
            api_keys[destination_service] = []
        api_keys[destination_service].append(key_info)
        info("Key transferred successfully.")
        save_keys_to_file()
    else:
        die("Invalid index or service not found.")

def display_keys(service):
    if service in api_keys:
        for i, key_info in enumerate(api_keys[service]):
            print(f"{i + 1}: {decrypt_key(key_info['key'])} - {key_info['description']}")
    else:
        die("Service not found.")

def save_keys_to_file():
    with open(api_keys_path, 'w') as file:
        json.dump(api_keys, file,indent=2)

def add_new_service():
    service = text_("Enter the name of the new service: ")
    return service

def list_services():
    info("Existing services:")
    if not api_keys:
       die("First Add api's, and then it display..")
       sys.exit(1)
    else:
       for i, service in enumerate(api_keys.keys()):
           print(f"{i + 1}. {service}")

def main():
    parser = argparse.ArgumentParser(description='Manage API keys.')
    parser.add_argument('--ser', help='Specify the service for which you want to add or view keys.')
    parser.add_argument('--add', action='store_true', help='Add a new API key for the specified service.')
    parser.add_argument('--modify', type=int, help='Modify an existing API key for the specified service (provide index).')
    args = parser.parse_args()

    if args.add:
        list_services()
        service_index = int(text_("Select a service by entering its number or enter 0 to create a new service: "))

        if service_index == 0:
            service = add_new_service()
        else:
            service = list(api_keys.keys())[service_index - 1]

        key = text_(f"Enter the API key for {service}: ")
        description = text_("Enter a description for this key: ")
        store_key(service, key, description)
        info("Key added successfully.")
        info("Please upgrade program to get newest feature...")
        save_keys_to_file()


    elif args.modify:
        list_services()
        service_index = int(text_("Select a service by entering its number: "))

        selected_service = list(api_keys.keys())[service_index - 1]
        display_keys(selected_service)

        modify_choice = text_(f"What do you want to do with {selected_service}? (modify(1)/transfer(2)): ")
        index = int(text_("Enter the index of the key you want to modify/transfer: ")) - 1

        if modify_choice == '1':
            new_key = text_(f"Enter the new API key for {selected_service}: ")
            new_description = text_(f"Enter a new description for {selected_service}: ")
            modify_key(selected_service, index, new_key, new_description)
        elif modify_choice == '2':
            list_services()
            destination_service_index = int(text_("Select a destination service by entering its number: "))
            destination_service = list(api_keys.keys())[destination_service_index - 1]
            transfer_key(selected_service, destination_service, index)
        else:
            die("Invalid choice.")


    else:
        list_services()
        service_index = int(text_("Select a service by entering its number: "))
        try:
            selected_service = list(api_keys.keys())[service_index - 1]
        except IndexError:
             die("Invalid Selection..")

        display_keys(selected_service)

if __name__ == "__main__":
    main() 
