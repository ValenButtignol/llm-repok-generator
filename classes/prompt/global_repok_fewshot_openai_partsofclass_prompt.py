from classes.class_format.parts_of_class_format import PartsOfClassFormat
from classes.prompt.json_prompt import JsonPrompt
from classes.prompt.templates import PARTS_OF_CLASS_1, PARTS_OF_CLASS_2, REPOK_EXAMPLE_1, REPOK_EXAMPLE_2, SYSTEM_PROMPT_SIMPLE, USER_PROMPT_OPENAI

class GlobalRepOkFewShotOpenAIPartsOfClassPrompt(JsonPrompt):
    def __init__(self, raw_class, class_name):
        super().__init__(raw_class, class_name)
        self.class_format = PartsOfClassFormat(raw_class, class_name)
        self.class_text = self.add_openai_format(self.class_format.get_formatted_class())

        self.add_system_message(SYSTEM_PROMPT_SIMPLE)

        class1 = self.add_openai_format(PARTS_OF_CLASS_1)
        print("\n")
        print(class1)
        print("\n")
        self.add_user_message(USER_PROMPT_OPENAI + class1)
        repok1 = self.add_openai_format(REPOK_EXAMPLE_1)
        print(repok1)
        print("\n")
        self.add_assistant_message(repok1)

        class2 = self.add_openai_format(PARTS_OF_CLASS_2)
        self.add_user_message(USER_PROMPT_OPENAI + class2)
        repok2 = self.add_openai_format(REPOK_EXAMPLE_2)
        self.add_assistant_message(repok2)

        self.add_user_message(USER_PROMPT_OPENAI + self.class_text)


    def add_openai_format(self, text):
        result = ""
        for line in text.split("\n"):
            if self.is_title(line):
                result += self.add_title_format(line)
            else:
                result += self.add_line_format(line)
        return result

    def add_line_format(self, line):
        return "#" + line + "\n"
    
    def add_title_format(self, title):
        return "### " + title + "\n"
    
    def is_title(self, line):
        return line.startswith("[") and line.endswith("]")