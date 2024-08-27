from classes.prompt.prompt_interface import PromptInterface

class FilePrompt(PromptInterface):
    def __init__(self, filename):
        self.filename="prompts/default_prompts/" + filename
    
    def get_text(self) -> str:
        file = open(self.filename, "r")
        prompt = file.read()
        return prompt
    