from classes.prompt.json_prompt import JsonPrompt
from classes.string_constants import PROPERTY_TAG


class CodePrompt(JsonPrompt):
    def __init__(self, raw_class, class_name):
        super().__init__()
        self.raw_class = raw_class
        self.class_name = class_name
        self.classwithprop = ""

    def add_property_to_class(self, prop):
        self.classwithprop = self.raw_class + "\n" + PROPERTY_TAG + prop + "\n"

    def template(self):
        raise NotImplementedError