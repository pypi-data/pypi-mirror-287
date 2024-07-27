import json
import logging
from typing import Dict
from web3 import Web3

class CoreSettings:
    
    DEFAULT_SETTINGS = {
        "address": "", # User address, only need for transactions
        "private_key": "", # Private key, save only to file if you know what you doing, only need for swap transactions, approve, etc
        "RPC": "https://bsc-dataseed1.binance.org/", # RPC to connect web3 make sure chain is supported
        "GWEI_OFFSET": 0, #Estimate gas cost and add offset
        "MaxTXFeeBNB": 0.001, #save you for massive Gas cost 
        "Slippage": 3, # Max Slippage you can accept
        "timeout": 60 # Timeout for waiting web3 requests
    }

    def __init__(self, settings_file_path: str = "Settings.json", saveSetting: bool = False):
        self.saveSetting = saveSetting
        self.settings_file_path = settings_file_path
        self.settings = self.DEFAULT_SETTINGS.copy()
        self.load_settings()

    def reinit_settings(self):
        self.settings = self.DEFAULT_SETTINGS.copy()
        self.load_settings()


    def load_settings(self):
        try:
            with open(self.settings_file_path, "r") as f:
                user_settings = json.load(f, indent=4)
            self.settings.update(user_settings)
        except Exception as e:
            if self.saveSetting:
                logging.info("Settings file not found, creating with default settings.")
                self.save_settings_to_file()

    def save_settings_to_file(self):
        """Save current settings to the JSON file."""
        try:
            print(self.settings_file_path)
            with open(self.settings_file_path, "w") as f:
                json.dump(self.settings, f, indent=4)
            logging.info(f"Settings saved to {self.settings_file_path}")
        except Exception as e:
            logging.error(f"Failed to save settings: {e}")

    def change_settings(self, key: str, new_value):
        """Change a specific setting and save to file if required."""
        if key in self.settings:
            self.settings[key] = new_value
            if self.saveSetting:
                self.save_settings_to_file()
        else:
            logging.error(f"Setting key '{key}' not found in settings.")

