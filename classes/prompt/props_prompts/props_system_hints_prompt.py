from classes.prompt.json_prompt import JsonPrompt
from classes.prompt.templates import SYSTEM_PROMPT, TEXT_PROP_BASIC_PROMPT, TEXT_PROP_END_OF_PROMPT, TEXT_PROP_HINTS_PROMPT, TEXT_PROP_USER_TASK, CODE_PROP_BASIC_PROMPT, CODE_PROP_HINTS_PROMPT, CODE_PROP_USER_TASK, CODE_PROP_END_OF_PROMPT
from classes.class_format.whole_class_format import WholeClassFormat 

class TextPropsSystemHintsPrompt(JsonPrompt):
    def __init__(self, raw_class, class_name):
        super().__init__(raw_class, class_name)
        self.class_format = WholeClassFormat(raw_class, class_name)
        self.class_text = self.class_format.get_formatted_class()

        self.add_system_message(SYSTEM_PROMPT + TEXT_PROP_BASIC_PROMPT + TEXT_PROP_HINTS_PROMPT)
        self.add_user_message(TEXT_PROP_USER_TASK(class_name) + self.class_text + TEXT_PROP_END_OF_PROMPT)

class CodePropSystemHintsPrompt(JsonPrompt):
    def __init__(self, classwithprop, class_name):
        super().__init__()

        self.add_system_message(SYSTEM_PROMPT + CODE_PROP_BASIC_PROMPT + CODE_PROP_HINTS_PROMPT)
        self.add_user_message(CODE_PROP_USER_TASK(class_name) + classwithprop + CODE_PROP_END_OF_PROMPT)
