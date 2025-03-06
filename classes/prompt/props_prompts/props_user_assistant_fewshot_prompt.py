from classes.prompt.json_prompt import JsonPrompt
from classes.prompt.templates import CLASS_EXAMPLE_1, CLASS_EXAMPLE_2, CLASS_NAME_EXAMPLE_1, CLASS_NAME_EXAMPLE_2, CODE_PROP_BASIC_PROMPT, CODE_PROP_END_OF_PROMPT, CODE_PROP_USER_TASK, CODE_SINGLE_PROP_EXAMPLE_1, CODE_SINGLE_PROP_EXAMPLE_2, REPOK_BASIC_PROMPT, SYSTEM_PROMPT, TEXT_PROP_END_OF_PROMPT, TEXT_PROP_LIST_EXAMPLE_1, TEXT_PROP_LIST_EXAMPLE_2, TEXT_PROP_USER_TASK, TEXT_SINGLE_PROP_EXAMPLE_1, TEXT_SINGLE_PROP_EXAMPLE_2
from classes.class_format.whole_class_format import WholeClassFormat 

class TextPropsUserAssistantFewShotPrompt(JsonPrompt):
    def __init__(self, raw_class, class_name):
        super().__init__(raw_class, class_name)
        self.class_format = WholeClassFormat(raw_class, class_name)
        self.class_text = self.class_format.get_formatted_class()

        self.add_system_message(SYSTEM_PROMPT)

        user_prompt = REPOK_BASIC_PROMPT
        user_prompt = TEXT_PROP_USER_TASK(CLASS_NAME_EXAMPLE_1)
        user_prompt += CLASS_EXAMPLE_1
        user_prompt += TEXT_PROP_END_OF_PROMPT
        self.add_user_message(user_prompt)
        self.add_assistant_message(TEXT_PROP_LIST_EXAMPLE_1)

        user_prompt = TEXT_PROP_USER_TASK(CLASS_NAME_EXAMPLE_2)
        user_prompt += CLASS_EXAMPLE_2
        user_prompt += TEXT_PROP_END_OF_PROMPT
        self.add_user_message(user_prompt)
        self.add_assistant_message(TEXT_PROP_LIST_EXAMPLE_2)

        user_prompt = TEXT_PROP_USER_TASK(class_name)
        user_prompt += self.class_text
        user_prompt += TEXT_PROP_END_OF_PROMPT
        self.add_user_message(user_prompt)

class CodePropUserAssistantFewShotPrompt(JsonPrompt):
    def __init__(self, classwithprop, class_name):
        super().__init__()

        self.add_system_message(SYSTEM_PROMPT)
        
        user_prompt = CODE_PROP_BASIC_PROMPT
        user_prompt += CODE_PROP_USER_TASK(CLASS_NAME_EXAMPLE_1)
        user_prompt += CLASS_EXAMPLE_1
        user_prompt += TEXT_SINGLE_PROP_EXAMPLE_1
        user_prompt += CODE_PROP_END_OF_PROMPT
        self.add_user_message(user_prompt)
        self.add_assistant_message(CODE_SINGLE_PROP_EXAMPLE_1)

        user_prompt = CODE_PROP_USER_TASK(CLASS_NAME_EXAMPLE_2)
        user_prompt += CLASS_EXAMPLE_2
        user_prompt += TEXT_SINGLE_PROP_EXAMPLE_2
        user_prompt += CODE_PROP_END_OF_PROMPT
        self.add_user_message(user_prompt)
        self.add_assistant_message(CODE_SINGLE_PROP_EXAMPLE_2)

        user_prompt = CODE_PROP_USER_TASK(class_name)
        user_prompt += classwithprop
        user_prompt += CODE_PROP_END_OF_PROMPT
        self.add_user_message(user_prompt)
