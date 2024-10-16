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