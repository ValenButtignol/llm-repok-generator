from classes.prompt.json_prompt import JsonPrompt
from classes.prompt.props_prompts.code_prompt import CodePrompt
from classes.prompt.templates import SYSTEM_PROMPT, TEXT_PROP_BASIC_PROMPT, TEXT_PROP_END_OF_PROMPT, TEXT_PROP_USER_TASK, CODE_PROP_BASIC_PROMPT, CODE_PROP_USER_TASK, CODE_PROP_END_OF_PROMPT
from classes.class_format.whole_class_format import WholeClassFormat 

class TextPropsSystemBasicPrompt(JsonPrompt):
    def __init__(self, raw_class, class_name):
        super().__init__(raw_class, class_name)
        self.class_format = WholeClassFormat(raw_class, class_name)
        self.class_text = self.class_format.get_formatted_class()

        self.add_system_message(SYSTEM_PROMPT + TEXT_PROP_BASIC_PROMPT)
        self.add_user_message(TEXT_PROP_USER_TASK(class_name) + self.class_text + TEXT_PROP_END_OF_PROMPT)

class CodePropSystemBasicPrompt(CodePrompt):
    def __init__(self, raw_class, class_name):
        super().__init__(raw_class, class_name)

    def template(self):
        self.add_system_message(SYSTEM_PROMPT + CODE_PROP_BASIC_PROMPT)
        self.add_user_message(CODE_PROP_USER_TASK(self.class_name) + self.classwithprop + CODE_PROP_END_OF_PROMPT)
