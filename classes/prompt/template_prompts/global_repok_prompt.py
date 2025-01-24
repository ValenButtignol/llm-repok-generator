from classes.prompt.json_prompt import JsonPrompt
from classes.prompt.template_prompts.templates import SYSTEM_PROMPT_REPOK, USER_PROMPT_REPOK
from classes.class_format.whole_class_format import WholeClassFormat

class GlobalRepOkPrompt(JsonPrompt):
    def __init__(self, raw_class):
        self.class_format = WholeClassFormat(raw_class)
        self.class_text = self.class_format.get_formatted_class()

        self.data = {"messages":[]}
        self.add_role_message("system", SYSTEM_PROMPT_REPOK)
        self.add_user_message(USER_PROMPT_REPOK + self.class_text)
