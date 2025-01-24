from classes.prompt.json_prompt import JsonPrompt
from classes.prompt.templates import SYSTEM_PROMPT_REPOK, USER_PROMPT_REPOK
from classes.class_format.whole_class_format import WholeClassFormat

class GlobalRepOkPrompt(JsonPrompt):
    def __init__(self, raw_class, class_name):
        super().__init__(raw_class, class_name)
        self.class_format = WholeClassFormat(raw_class, class_name)
        self.class_text = self.class_format.get_formatted_class()

        self.add_system_message(SYSTEM_PROMPT_REPOK)
        self.add_user_message(USER_PROMPT_REPOK + self.class_text)
