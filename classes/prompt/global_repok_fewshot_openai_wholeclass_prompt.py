from classes.class_format.whole_class_format import WholeClassFormat
from classes.prompt.json_prompt import JsonPrompt
from classes.prompt.templates import CLASS_EXAMPLE_1, CLASS_EXAMPLE_2, REPOK_EXAMPLE_1, REPOK_EXAMPLE_2, SYSTEM_PROMPT_SIMPLE, USER_PROMPT_OPENAI

class GlobalRepOkFewShotOpenAIWholeClassPrompt(JsonPrompt):
    def __init__(self, raw_class, class_name):
        super().__init__(raw_class, class_name)
        self.class_format = WholeClassFormat(raw_class, class_name)
        self.class_text = self.class_format.get_formatted_class().replace("[Class]", "### Class:")

        self.add_system_message(SYSTEM_PROMPT_SIMPLE)
        class1 = CLASS_EXAMPLE_1.replace("[Class]", "### Class:")
        self.add_user_message(USER_PROMPT_OPENAI + class1)
        repok1 = REPOK_EXAMPLE_1.replace("[repOk]", "### repOk:")
        self.add_assistant_message(repok1)

        class2 = CLASS_EXAMPLE_2.replace("[Class]", "### Class:")
        self.add_user_message(USER_PROMPT_OPENAI + class2)
        repok2 = REPOK_EXAMPLE_2.replace("[repOk]", "### repOk:")
        self.add_assistant_message(repok2)

        self.add_user_message(USER_PROMPT_OPENAI + self.class_text)
