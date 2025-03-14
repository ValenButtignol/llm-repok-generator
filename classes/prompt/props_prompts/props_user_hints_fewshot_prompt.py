from classes.prompt.json_prompt import JsonPrompt
from classes.prompt.props_prompts.code_prompt import CodePrompt
from classes.prompt.templates import CLASS_EXAMPLE_3, CLASS_EXAMPLE_2, CLASS_NAME_EXAMPLE_3, CLASS_NAME_EXAMPLE_2, CODE_PROP_BASIC_PROMPT, CODE_PROP_END_OF_PROMPT, CODE_PROP_HINTS_PROMPT, CODE_PROP_USER_TASK, CODE_SINGLE_PROP_EXAMPLE_3, CODE_SINGLE_PROP_EXAMPLE_2, SYSTEM_PROMPT, TEXT_PROP_BASIC_PROMPT, TEXT_PROP_END_OF_PROMPT, TEXT_PROP_HINTS_PROMPT, TEXT_PROP_LIST_EXAMPLE_3, TEXT_PROP_LIST_EXAMPLE_2, TEXT_PROP_USER_TASK, TEXT_SINGLE_PROP_EXAMPLE_3, TEXT_SINGLE_PROP_EXAMPLE_2
from classes.class_format.whole_class_format import WholeClassFormat 

class TextPropsUserHintsFewShotPrompt(JsonPrompt):
    def __init__(self, raw_class, class_name):
        super().__init__(raw_class, class_name)
        self.class_format = WholeClassFormat(raw_class, class_name)
        self.class_text = self.class_format.get_formatted_class()

        self.add_system_message(SYSTEM_PROMPT)
        
        user_prompt = TEXT_PROP_BASIC_PROMPT
        user_prompt += TEXT_PROP_HINTS_PROMPT
        user_prompt += TEXT_PROP_USER_TASK(CLASS_NAME_EXAMPLE_3)
        user_prompt += CLASS_EXAMPLE_3
        user_prompt += TEXT_PROP_END_OF_PROMPT
        user_prompt += TEXT_PROP_LIST_EXAMPLE_3

        user_prompt += TEXT_PROP_USER_TASK(CLASS_NAME_EXAMPLE_2)
        user_prompt += CLASS_EXAMPLE_2
        user_prompt += TEXT_PROP_END_OF_PROMPT
        user_prompt += TEXT_PROP_LIST_EXAMPLE_2

        user_prompt += TEXT_PROP_USER_TASK(class_name)
        user_prompt += self.class_text
        user_prompt += TEXT_PROP_END_OF_PROMPT

        self.add_user_message(user_prompt)

class CodePropUserHintsFewShotPrompt(CodePrompt):
    def __init__(self, raw_class, class_name):
        super().__init__(raw_class, class_name)

    def template(self):
        self.add_system_message(SYSTEM_PROMPT)

        user_prompt = CODE_PROP_BASIC_PROMPT
        user_prompt += CODE_PROP_HINTS_PROMPT
        user_prompt += CODE_PROP_USER_TASK(CLASS_NAME_EXAMPLE_3)
        user_prompt += CLASS_EXAMPLE_3
        user_prompt += TEXT_SINGLE_PROP_EXAMPLE_3
        user_prompt += CODE_PROP_END_OF_PROMPT
        user_prompt += CODE_SINGLE_PROP_EXAMPLE_3

        user_prompt += CODE_PROP_USER_TASK(CLASS_NAME_EXAMPLE_2)
        user_prompt += CLASS_EXAMPLE_2
        user_prompt += TEXT_SINGLE_PROP_EXAMPLE_2
        user_prompt += CODE_PROP_END_OF_PROMPT
        user_prompt += CODE_SINGLE_PROP_EXAMPLE_2

        user_prompt += CODE_PROP_USER_TASK(self.class_name)
        user_prompt += self.classwithprop
        user_prompt += CODE_PROP_END_OF_PROMPT
        
        self.add_user_message(user_prompt)