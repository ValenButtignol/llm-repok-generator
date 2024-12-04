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
        
    def add_assistant_message(self, message):
        self.add_role_message("assistant", message)
        
    def add_user_message(self, message):
        self.add_role_message("user", message)

    def add_user_message_from_json(self, filename):
        prompt = JsonPrompt(filename)
        self.add_user_message(prompt.get_text())
