from classes.prompt.json_prompt import JsonPrompt
from classes.prompt.templates import SYSTEM_PROMPT_PROP_LIST, SYSTEM_PROMPT_REPOK_AND_PROP, CLASS_EXAMPLE_1, TEXT_PROP_LIST_EXAMPLE_1, CODE_SINGLE_PROP_EXAMPLE_1, CLASS_EXAMPLE_2, TEXT_PROP_LIST_EXAMPLE_2, CODE_SINGLE_PROP_EXAMPLE_2, TEXT_SINGLE_PROP_EXAMPLE_1, TEXT_SINGLE_PROP_EXAMPLE_2
from classes.class_format.whole_class_format import WholeClassFormat

class DualPropertiesWholeClassPrompt(JsonPrompt):
    def __init__(self, raw_class, class_name):
        super().__init__(raw_class, class_name)
        self.class_format = WholeClassFormat(raw_class, class_name)
        self.class_text = self.class_format.get_formatted_class()

        self.add_system_message(SYSTEM_PROMPT_PROP_LIST)
        
        self.add_user_message(CLASS_EXAMPLE_1)
        self.add_assistant_message(TEXT_PROP_LIST_EXAMPLE_1)
        
        self.add_user_message(CLASS_EXAMPLE_2)
        self.add_assistant_message(TEXT_PROP_LIST_EXAMPLE_2)

        self.add_user_message(self.class_text)

class DualRepOkFewShotCoTWholeClassPrompt(JsonPrompt):
    def __init__(self, classwithprop):

        self.data = {"messages":[]}
        self.add_role_message("system", SYSTEM_PROMPT_REPOK_AND_PROP)
        
        self.add_user_message(CLASS_EXAMPLE_1 + TEXT_SINGLE_PROP_EXAMPLE_1)
        self.add_assistant_message(CODE_SINGLE_PROP_EXAMPLE_1)

        self.add_user_message(CLASS_EXAMPLE_2 + TEXT_SINGLE_PROP_EXAMPLE_2)
        self.add_assistant_message(CODE_SINGLE_PROP_EXAMPLE_2)

        self.add_user_message(classwithprop)