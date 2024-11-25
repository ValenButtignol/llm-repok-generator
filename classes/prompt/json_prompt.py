from classes.prompt.prompt_interface import PromptInterface
import json

class JsonPrompt(PromptInterface):
    def __init__(self, filename):
        self.filename="prompts/" + filename
    
    def get_text(self) -> str:
        with open(self.filename, "r") as file:
            data = json.load(file)
            prompt = data["messages"]
        
        return prompt
    
    def add_role_message(self, role, message):
        with open(self.filename, "r") as file:
            data = json.load(file)
            data["messages"].append({
                "role": role,
                "message": message
            })
        with open(self.filename, "w") as file:
            json.dump(data, file)