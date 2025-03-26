
from classes.class_format.whole_class_format import WholeClassFormat
from classes.prompt.json_prompt import JsonPrompt
from classes.prompt.props_prompts.code_prompt import CodePrompt
from classes.prompt.templates import REPOK_BASIC_PROMPT, REPOK_END_OF_PROMPT, REPOK_USER_TASK, SPEC_END_OF_PROMPT, SPEC_HINTS_PROMPT, SPEC_USER_TASK, SYSTEM_PROMPT, SYSTEM_PROMPT_SPEC


class SpecPrompt(JsonPrompt):
    def __init__(self, raw_class, class_name):
        super().__init__(raw_class, class_name)
        self.class_format = WholeClassFormat(raw_class, class_name)
        self.class_text = self.class_format.get_formatted_class()

        self.add_system_message(SYSTEM_PROMPT_SPEC + SPEC_HINTS_PROMPT)
        self.add_user_message(SPEC_USER_TASK(class_name) + self.class_text + SPEC_END_OF_PROMPT)

class RepOKSpecPrompt(CodePrompt):
    def __init__(self, raw_class, class_name):
        super().__init__(raw_class, class_name)

    def template(self):
        self.add_system_message(SYSTEM_PROMPT + REPOK_BASIC_PROMPT)
        self.add_user_message(REPOK_USER_TASK(self.class_name) + self.classwithprop + REPOK_END_OF_PROMPT)

    def add_spec(self, spec):
        spec = self.filter_spec(spec)
        self.classwithprop = self.raw_class + "\n" + "### Specification\n" + spec + "\n"


class RepOKSpecOnlyPrompt(CodePrompt):
    def __init__(self, raw_class, class_name):
        super().__init__(raw_class, class_name)

    def template(self):
        self.add_system_message(SYSTEM_PROMPT + REPOK_BASIC_PROMPT)
        self.add_user_message(REPOK_USER_TASK(self.class_name) + self.classwithprop + REPOK_END_OF_PROMPT)

    def add_spec(self, spec):
        spec = self.filter_spec(spec)
        self.classwithprop = "\n" + "### Specification\n" + spec + "\n"