from classes.prompt.json_prompt import JsonPrompt
from classes.prompt.template_prompts.templates import SYSTEM_PROMPT_PROP_LIST, SYSTEM_PROMPT_REPOK_AND_PROP, PARTS_OF_CLASS_1, TEXT_PROP_LIST_EXAMPLE_1, TEXT_SINGLE_PROP_EXAMPLE_1, CODE_SINGLE_PROP_EXAMPLE_1, PARTS_OF_CLASS_2, TEXT_PROP_LIST_EXAMPLE_2, CODE_SINGLE_PROP_EXAMPLE_2, TEXT_SINGLE_PROP_EXAMPLE_2
from classes.class_format.parts_of_class_format import PartsOfClassFormat

class DualPropertiesPartsOfClassPrompt(JsonPrompt):
    def __init__(self, raw_class):
        self.class_format = PartsOfClassFormat(raw_class)
        self.class_text = self.class_format.get_formatted_class()

        self.data = {"messages":[]}
        self.add_role_message("system", SYSTEM_PROMPT_PROP_LIST)
        
        self.add_user_message(PARTS_OF_CLASS_1)
        self.add_assistant_message(TEXT_PROP_LIST_EXAMPLE_1)
        
        self.add_user_message(PARTS_OF_CLASS_2)
        self.add_assistant_message(TEXT_PROP_LIST_EXAMPLE_2)

        self.add_user_message(self.class_text)

class DualRepOkFewShotCoTPartsOfClassPrompt(JsonPrompt):
    def __init__(self, classwithprop):

        self.data = {"messages":[]}
        self.add_role_message("system", SYSTEM_PROMPT_REPOK_AND_PROP)
        
        self.add_user_message(PARTS_OF_CLASS_1 + TEXT_SINGLE_PROP_EXAMPLE_1)
        self.add_assistant_message(CODE_SINGLE_PROP_EXAMPLE_1)

        self.add_user_message(PARTS_OF_CLASS_2 + TEXT_SINGLE_PROP_EXAMPLE_2)
        self.add_assistant_message(CODE_SINGLE_PROP_EXAMPLE_2)

        self.add_user_message(classwithprop)