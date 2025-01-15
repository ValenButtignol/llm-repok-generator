from classes.prompt.json_prompt import JsonPrompt
from classes.prompt.template_prompts.templates import SYSTEM_PROMPT_REPOK, SYSTEM_PROMPT_COT_REPOK, USER_PROMPT_PROP_LIST, USER_PROMPT_CHAIN_OF_THOUGT, PARTS_OF_CLASS_1, TEXT_PROP_LIST_EXAMPLE_1, REPOK_EXAMPLE_1, PARTS_OF_CLASS_2, TEXT_PROP_LIST_EXAMPLE_2, REPOK_EXAMPLE_2

class GlobalRepOkFewShotCoTPartsOfClassPrompt(JsonPrompt):
    def __init__(self, classfile):
        with open(classfile, "r") as file:
            self.classtext = file.read()

        self.data = {"messages":[]}
        self.add_role_message("system", SYSTEM_PROMPT_COT_REPOK)
        self.add_user_message(USER_PROMPT_PROP_LIST + PARTS_OF_CLASS_1)
        self.add_assistant_message(TEXT_PROP_LIST_EXAMPLE_1)
        self.add_user_message(USER_PROMPT_CHAIN_OF_THOUGT)
        self.add_assistant_message(REPOK_EXAMPLE_1)
        
        self.add_user_message(USER_PROMPT_PROP_LIST + PARTS_OF_CLASS_2)
        self.add_assistant_message(TEXT_PROP_LIST_EXAMPLE_2)
        self.add_user_message(USER_PROMPT_CHAIN_OF_THOUGT)
        self.add_assistant_message(REPOK_EXAMPLE_2)

        self.add_user_message(USER_PROMPT_PROP_LIST + self.classtext)

    def add_remaining_prompts(self, prop_list):
        self.add_assistant_message(prop_list)
        self.add_user_message(USER_PROMPT_CHAIN_OF_THOUGT)
