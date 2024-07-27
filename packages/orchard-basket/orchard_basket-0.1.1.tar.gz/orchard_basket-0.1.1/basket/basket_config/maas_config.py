import os
import yaml
from typing import List, Dict, Optional

# Define the knowd MaaS configuration
MAAS_CONFIG = {
    'maas': [
        {'name': 'FreeModel', 'url': 'http://topic-land.com:10000/v1'},
        {'name': 'OpenAI', 'url': 'https://api.openai.com/v1'},
        {'name': 'SiliconFlow', 'url': 'https://api.siliconflow.cn/v1'},
        {'name': 'DashScope', 'url': 'https://dashscope.aliyuncs.com/compatible-mode/v1'},
        {'name': 'OpenRouter', 'url': 'https://openrouter.ai/api/v1'},
        {'name': 'DeepSeek', 'url': 'https://api.deepseek.com/v1'},
        {'name': 'MoonShot', 'url': 'https://api.moonshot.cn/v1'},
        {'name': 'ZhiPu', 'url': 'https://open.bigmodel.cn/api/paas/v4/'},
        {'name': 'Lime', 'url': 'http://127.0.0.1:10000/v1'}
    ]
}

class MaaSProvider:
    def __init__(self, name: str, url: str, models: Optional[List[str]] = None):
        self.name: str = name
        self.url: str = url
        self.models: List[str] = models or []

class MaaSConfig:
    def __init__(self):
        home_dir = os.path.expanduser("~")
        self.config_dir = os.path.join(home_dir, ".config")
        self.file_path = os.path.join(self.config_dir, "basket_maas.yaml")
        self.create_file_if_not_exists()

        self.providers: List[MaaSProvider] = []
        self._load_config(self.file_path)

    def create_file_if_not_exists(self) -> None: 
        # Check if the file exists
        if not os.path.exists(self.file_path):
            
            # Ensure the config directory exists
            os.makedirs(self.config_dir, exist_ok=True)

            # Write the content to the file
            with open(self.file_path, 'w') as file:
                yaml.dump(MAAS_CONFIG, file)

            print(f"Checked for {self.file_path}, and created if it didn't exist.")

    def _load_config(self, yaml_file: str) -> None:
        with open(yaml_file, 'r') as file:
            config = yaml.safe_load(file)
        
        maas_list = config.get('maas', [])
        current_provider = None

        for item in maas_list:
            if isinstance(item, dict) and 'name' in item:
                if current_provider:
                    self.providers.append(current_provider)
                current_provider = MaaSProvider(item['name'], item['url'])
            elif isinstance(item, str) and current_provider:
                current_provider.models.append(item)

        if current_provider:
            self.providers.append(current_provider)

    def get_provider(self, name: str) -> Optional[MaaSProvider]:
        for provider in self.providers:
            if provider.name.lower() == name.lower():
                return provider
        return None

    def list_providers(self) -> List[str]:
        return [provider.name for provider in self.providers]

    def get_provider_url(self, name: str) -> Optional[str]:
        provider = self.get_provider(name)
        return provider.url if provider else None

    def get_provider_models(self, name: str) -> Optional[List[str]]:
        provider = self.get_provider(name)
        return provider.models if provider else None

    def list_maas_names(self) -> List[str]:
        return [provider.name for provider in self.providers]
