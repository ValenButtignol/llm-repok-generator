from classes.prompt.json_prompt import JsonPrompt
from classes.prompt.templates import SYSTEM_PROMPT, REPOK_BASIC_PROMPT, REPOK_END_OF_PROMPT, REPOK_USER_TASK, REPOK_HINTS_PROMPT
from classes.class_format.whole_class_format import WholeClassFormat 

class RepOKUserHintsPrompt(JsonPrompt):
    def __init__(self, raw_class, class_name):
        super().__init__(raw_class, class_name)
        self.class_format = WholeClassFormat(raw_class, class_name)
        self.class_text = self.class_format.get_formatted_class()

        self.add_system_message(SYSTEM_PROMPT)
        self.add_user_message(REPOK_BASIC_PROMPT + REPOK_HINTS_PROMPT + REPOK_USER_TASK(class_name) + self.class_text + REPOK_END_OF_PROMPT)
