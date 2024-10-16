from classes.prompt.prompt_interface import PromptInterface
from classes.prompt.file_prompt import FilePrompt
from classes.prompt.json_prompt import JsonPrompt
from classes.prompt.plain_text_prompt import PlainTextPrompt

class PromptFactory:
    def __init__(self):
        pass
    
    def create(self, prompt_type, prompt_container) -> PromptInterface:
        if prompt_type == "text":
            return PlainTextPrompt(prompt_container)
        elif prompt_type == "file":
            return FilePrompt(prompt_container)
        elif prompt_type == "json":
            return JsonPrompt(prompt_container) 
        else:
            raise Exception("Invalid prompt type: " + prompt_type + "\n")