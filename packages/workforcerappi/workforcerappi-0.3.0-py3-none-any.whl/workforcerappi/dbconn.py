import os
import json
import sys
import snowflake.connector
from tkinter import Tk, filedialog, messagebox
import logging

logging.basicConfig(level=logging.DEBUG, filename="wfm_gui.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")

def get_project_settings(default_filepath="settings.json"):
    """
    Function to import settings from settings.json.
    Prompts the user to select the file if it does not exist at the default location.
    :param default_filepath: default path to settings.json
    :return: settings as a dictionary object
    """
    if os.path.exists(default_filepath):
        filepath = default_filepath
    else:
        # If settings.json is not found, prompt the user to select the file
        root = Tk()
        root.withdraw()  # Hide the root window
        messagebox.showinfo("Settings File", "Please select your settings.json file")
        filepath = filedialog.askopenfilename(title="Select settings.json file", filetypes=[("JSON files", "*.json")])
        
        if not filepath:
            raise ImportError("settings.json file not provided. Application will exit.")
    
    if not os.path.exists(filepath):
        raise ImportError(f"settings.json does not exist at provided location: {filepath}")

    try:
        with open(filepath, "r") as f:
            project_settings = json.load(f)
        return project_settings
    except Exception as e:
        logging.error(f"Error reading settings.json: {e}")
        raise ImportError(f"Error reading settings.json: {e}")


def snowflake_connection(project_settings=None, AUTO_COMMIT=True):
    if project_settings is None:
        project_settings = get_project_settings()
    
    conn = snowflake.connector.connect(
        user=project_settings["snowflake"]["user"],
        password=project_settings["snowflake"]["password"],
        account=project_settings["snowflake"]["account"],
        authenticator=project_settings["snowflake"]["authenticator"],
        database=project_settings["snowflake"]["database"],
        autocommit=AUTO_COMMIT
    )
    return conn



# Function to disconnect the database connection and clear cache
def disconnect_and_clear_cache(conn):
    cur = conn.cursor()
    cur.close()
    # Disconnect the database connection
    conn.close()
