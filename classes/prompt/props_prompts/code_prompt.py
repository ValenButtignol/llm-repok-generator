from classes.prompt.json_prompt import JsonPrompt
from classes.string_constants import CLOSE_REASONING_TAG, OPEN_REASONING_TAG, PROPERTY_TAG


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
    
    def add_spec(self):
        raise NotImplementedError

    def filter_spec(self, spec):
        result = ""
        reasoning = False
        lines = spec.splitlines()
        for line in lines:
            stripped = line.strip()
            if stripped == OPEN_REASONING_TAG:
                reasoning = True
            elif stripped == CLOSE_REASONING_TAG:
                reasoning = False
            elif not reasoning:
                result += line + "\n"
        
        return result