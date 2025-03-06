from classes.prompt.json_prompt import JsonPrompt
from classes.prompt.templates import CODE_PROP_BASIC_PROMPT, CODE_PROP_END_OF_PROMPT, CODE_PROP_USER_TASK, SYSTEM_PROMPT, TEXT_PROP_BASIC_PROMPT, TEXT_PROP_END_OF_PROMPT, TEXT_PROP_USER_TASK
from classes.class_format.whole_class_format import WholeClassFormat 

class TextPropsUserBasicPrompt(JsonPrompt):
    def __init__(self, raw_class, class_name):
        super().__init__(raw_class, class_name)
        self.class_format = WholeClassFormat(raw_class, class_name)
        self.class_text = self.class_format.get_formatted_class()

        self.add_system_message(SYSTEM_PROMPT)
        self.add_user_message(TEXT_PROP_BASIC_PROMPT + TEXT_PROP_USER_TASK(class_name) + self.class_text + TEXT_PROP_END_OF_PROMPT)

class CodePropUserBasicPrompt(JsonPrompt):
    def __init__(self, classwithprop, class_name):
        super().__init__()

        self.add_system_message(SYSTEM_PROMPT)
        self.add_user_message(CODE_PROP_BASIC_PROMPT + CODE_PROP_USER_TASK(class_name) + classwithprop + CODE_PROP_END_OF_PROMPT)