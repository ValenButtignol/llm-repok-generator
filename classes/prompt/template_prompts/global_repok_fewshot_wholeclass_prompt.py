from classes.prompt.json_prompt import JsonPrompt
from classes.prompt.template_prompts.templates import SYSTEM_PROMPT_REPOK, USER_PROMPT_REPOK, CLASS_EXAMPLE_1, REPOK_EXAMPLE_1, CLASS_EXAMPLE_2, REPOK_EXAMPLE_2

class GlobalRepOkFewShotWholeClassPrompt(JsonPrompt):
    def __init__(self, classtext):
        self.classtext = classtext

        self.data = {"messages":[]}
        self.add_role_message("system", SYSTEM_PROMPT_REPOK)
        self.add_user_message(USER_PROMPT_REPOK + CLASS_EXAMPLE_1)
        self.add_assistant_message(REPOK_EXAMPLE_1)
        self.add_user_message(USER_PROMPT_REPOK + CLASS_EXAMPLE_2)
        self.add_assistant_message(REPOK_EXAMPLE_2)
        self.add_user_message(USER_PROMPT_REPOK + self.classtext)
