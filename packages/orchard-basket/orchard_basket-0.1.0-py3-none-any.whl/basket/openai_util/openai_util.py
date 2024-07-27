from openai import OpenAI

class OpenaiUtil:
    def __init__(self, base_url: str, api_key: str, model: str = "") -> list[str]:
       self.client = OpenAI(base_url=base_url, api_key=api_key)
       self.model = model
    
    """
    Function to list available models

    Return data is like [{'id': 'qwen-turbo', 'created': 1714377100, 'object': 'model', 'owned_by': 'system'}]
    Notice that DeepSeek does not return created column. OpenRouter does not return object and ownedby columns.
    
    """
    def list_available_models(self) -> list[str]:
        models = self.client.models.list()
        return models.to_dict()["data"]

    def chat_with_model(self, model: str, text: str) -> str:
        completion = self.client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": text}
            ]
        )
        #import ipdb;ipdb.set_trace()
        return completion.choices[0].message.content
    
    def chat(self, text) -> str:
        if self.model == "":
            print("Default model is not set, please set in advanced")
            return ""
        return self.chat_with_model(self.model, text)
