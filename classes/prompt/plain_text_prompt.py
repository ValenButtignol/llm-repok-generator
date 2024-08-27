from classes.prompt.prompt_interface import PromptInterface

class PlainTextPrompt(PromptInterface):
    def __init__(self, text):
        self.text=text
        
    def get_text(self) -> str:
        return self.text