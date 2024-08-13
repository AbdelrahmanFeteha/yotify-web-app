import ytmusicapi
import os
from credentials import headers

# Define the path to the browser.json file
file_path = 'browser.json'

# Check if the file exists and delete it if it does
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"{file_path} has been deleted. Creating new file...") 
else:
    print(f"{file_path} does not exist. Creating new file...")

try:
    ytmusicapi.setup(filepath="browser.json", headers_raw=headers)
    print ("json file created successfully!")
except Exception as e:
    exit(f"An error occurred while creating the json file: {e}")

ytmusic = ytmusicapi.YTMusic("browser.json")
account_info = ytmusic.get_account_info()