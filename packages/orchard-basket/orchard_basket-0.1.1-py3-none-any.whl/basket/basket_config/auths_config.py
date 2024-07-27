import os
from typing import List, Dict, Optional
import yaml

class AuthMaaS:
    def __init__(self, name: str, api_key: str):
        self.name = name
        self.api_key = api_key

    def to_dict(self) -> Dict[str, str]:
        return {"name": self.name, "api_key": self.api_key}

    @staticmethod
    def from_dict(data: Dict[str, str]) -> 'AuthMaaS':
        return AuthMaaS(name=data["name"], api_key=data["api_key"])

class AuthsConfig:

    def __init__(self):
        home_dir = os.path.expanduser("~")
        self.config_dir = os.path.join(home_dir, ".config")
        self.file_path = os.path.join(self.config_dir, "basket_auths.yaml")
        self.create_file_if_not_exists()
    
        self.data: Dict[str, Optional[str]] = {
            "current_maas": "",
            "current_model": "",
            "auths": []
        }
        self.read_yaml()

    def create_file_if_not_exists(self) -> None: 
        # Check if the file exists
        if not os.path.exists(self.file_path):
            # Define the content for the YAML file
            content = {
                "current_maas": "FreeModel",
                "current_model": "arbitrary_model",
                "auths": [{"name": "FreeModel", "api_key": "arbitrary_api_key"}]
            }

            # Ensure the config directory exists
            os.makedirs(self.config_dir, exist_ok=True)

            # Write the content to the file
            with open(self.file_path, 'w') as file:
                yaml.dump(content, file)

            print(f"Checked for {self.file_path}, and created if it didn't exist.")

    def reload(self) -> None:
        self.read_yaml()

    def read_yaml(self) -> None:
        try:
            with open(self.file_path, 'r') as file:
                loaded_data = yaml.safe_load(file)
                self.data["current_maas"] = loaded_data.get("current_maas", "")
                self.data["current_model"] = loaded_data.get("current_model", "")
                self.data["auths"] = [AuthMaaS.from_dict(auth) for auth in loaded_data.get("auths", [])]
        except FileNotFoundError:
            pass
        except yaml.YAMLError as exc:
            print(f"Error reading YAML file: {exc}")

    def write_yaml(self) -> None:
        try:
            with open(self.file_path, 'w') as file:
                yaml.dump({
                    "current_maas": self.data["current_maas"],
                    "current_model": self.data["current_model"],
                    "auths": [auth.to_dict() for auth in self.data["auths"]]
                }, file)
        except yaml.YAMLError as exc:
            print(f"Error writing YAML file: {exc}")

    def add_auth(self, name: str, api_key: str) -> None:
        if isinstance(self.data["auths"], list):
            self.data["auths"].append(AuthMaaS(name, api_key))
        else:
            self.data["auths"] = [AuthMaaS(name, api_key)]
        self.write_yaml()

    def get_auth(self, name: str) -> Optional[AuthMaaS]:
        if isinstance(self.data["auths"], list):
            for auth in self.data["auths"]:
                if auth.name.lower() == name.lower():
                    return auth
        return None

    def remove_auth(self, name: str) -> bool:
        if isinstance(self.data["auths"], list):
            for auth in self.data["auths"]:
                if auth.name.lower() == name.lower():
                    self.data["auths"].remove(auth)

                    self.write_yaml()
                    return True
        
        return False

    def get_current_maas(self) -> str:
        return self.data["current_maas"]
    
    def update_current_maas(self, maas: str) -> None:
        self.data["current_maas"] = maas
        self.write_yaml()

    def get_current_model(self) -> str:
        return self.data["current_model"]

    def update_current_model(self, model: str) -> None:
        self.data["current_model"] = model
        self.write_yaml()


