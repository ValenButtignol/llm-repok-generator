from classes.prompt.json_prompt import JsonPrompt
from classes.prompt.templates import SYSTEM_PROMPT, REPOK_BASIC_PROMPT, REPOK_END_OF_PROMPT, REPOK_USER_TASK, REPOK_HINTS_PROMPT, CLASS_NAME_EXAMPLE_1, CLASS_NAME_EXAMPLE_2, CLASS_EXAMPLE_1, CLASS_EXAMPLE_2, REPOK_EXAMPLE_1, REPOK_EXAMPLE_2
from classes.class_format.whole_class_format import WholeClassFormat 

class RepOKSystemHintsUserFewShotPrompt(JsonPrompt):
    def __init__(self, raw_class, class_name):
        super().__init__(raw_class, class_name)
        self.class_format = WholeClassFormat(raw_class, class_name)
        self.class_text = self.class_format.get_formatted_class()

        self.add_system_message(SYSTEM_PROMPT + REPOK_BASIC_PROMPT + REPOK_HINTS_PROMPT)

        user_prompt = REPOK_USER_TASK(CLASS_NAME_EXAMPLE_1)
        user_prompt += CLASS_EXAMPLE_1
        user_prompt += REPOK_END_OF_PROMPT
        user_prompt += REPOK_EXAMPLE_1

        user_prompt += REPOK_USER_TASK(CLASS_NAME_EXAMPLE_2)
        user_prompt += CLASS_EXAMPLE_2
        user_prompt += REPOK_END_OF_PROMPT
        user_prompt += REPOK_EXAMPLE_2

        user_prompt += REPOK_USER_TASK(class_name)
        user_prompt += self.class_text
        user_prompt += REPOK_END_OF_PROMPT

        self.add_user_message(user_prompt)
