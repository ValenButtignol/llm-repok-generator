from classes.prompt.json_prompt import JsonPrompt
from classes.prompt.template_prompts.templates import SYSTEM_PROMPT_REPOK, USER_PROMPT_REPOK

class GlobalRepOkPrompt(JsonPrompt):
    def __init__(self, classfile):
        with open(classfile, "r") as file:
            self.classtext = file.read()

        self.add_role_message("system", SYSTEM_PROMPT_REPOK)
        self.add_user_message(USER_PROMPT_REPOK + self.classtext)
