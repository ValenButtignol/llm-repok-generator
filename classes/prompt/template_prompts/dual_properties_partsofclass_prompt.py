from classes.prompt.json_prompt import JsonPrompt
from classes.prompt.template_prompts.templates import SYSTEM_PROMPT_PROP_LIST, SYSTEM_PROMPT_REPOK_AND_PROP, PARTS_OF_CLASS_1, TEXT_PROP_LIST_EXAMPLE_1, CODE_SINGLE_PROP_EXAMPLE_1, PARTS_OF_CLASS_2, TEXT_PROP_LIST_EXAMPLE_2, CODE_SINGLE_PROP_EXAMPLE_2

class DualPropertiesPartsOfClassPrompt(JsonPrompt):
    def __init__(self, classfile):
        with open(classfile, "r") as file:
            self.classtext = file.read()

        self.data = {"messages":[]}
        self.add_role_message("system", SYSTEM_PROMPT_PROP_LIST)
        
        self.add_user_message(PARTS_OF_CLASS_1)
        self.add_assistant_message(TEXT_PROP_LIST_EXAMPLE_1)
        
        self.add_user_message(PARTS_OF_CLASS_2)
        self.add_assistant_message(TEXT_PROP_LIST_EXAMPLE_2)

        self.add_user_message(self.classtext)

class DualRepOkFewShotCoTPartsOfClassPrompt(JsonPrompt):
    def __init__(self, classwithprop):

        self.data = {"messages":[]}
        self.add_role_message("system", SYSTEM_PROMPT_REPOK_AND_PROP)
        
        self.add_user_message(PARTS_OF_CLASS_1 + TEXT_PROP_LIST_EXAMPLE_1)
        self.add_assistant_message(CODE_SINGLE_PROP_EXAMPLE_1)

        self.add_user_message(PARTS_OF_CLASS_2 + TEXT_PROP_LIST_EXAMPLE_2)
        self.add_assistant_message(CODE_SINGLE_PROP_EXAMPLE_2)

        self.add_user_message(classwithprop)