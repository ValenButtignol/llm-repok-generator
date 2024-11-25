from classes.prompt.prompt_interface import PromptInterface
import json

class JsonPrompt(PromptInterface):
    def __init__(self, filename):
        self.filename="prompts/" + filename
        with open(self.filename, "r") as file:
            self.data = json.load(file)
        
    def get_text(self) -> str:
        return self.data["messages"]
        
    
    def add_role_message(self, role, message):
        self.data["messages"].append({
            "role": role,
            "content": message
        })
