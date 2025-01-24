from classes.prompt.json_prompt import JsonPrompt
from classes.prompt.templates import SYSTEM_PROMPT_REPOK, USER_PROMPT_REPOK, PARTS_OF_CLASS_1, REPOK_EXAMPLE_1, PARTS_OF_CLASS_2, REPOK_EXAMPLE_2
from classes.class_format.parts_of_class_format import PartsOfClassFormat

class GlobalRepOkFewShotPartsOfClassPrompt(JsonPrompt):
    def __init__(self, raw_class, class_name):
        super().__init__(raw_class, class_name)
        self.class_format = PartsOfClassFormat(raw_class, class_name)
        self.class_text = self.class_format.get_formatted_class()

        self.add_system_message(SYSTEM_PROMPT_REPOK)
        self.add_user_message(USER_PROMPT_REPOK + PARTS_OF_CLASS_1)
        self.add_assistant_message(REPOK_EXAMPLE_1)
        self.add_user_message(USER_PROMPT_REPOK + PARTS_OF_CLASS_2)
        self.add_assistant_message(REPOK_EXAMPLE_2)
        self.add_user_message(USER_PROMPT_REPOK + self.class_text)
