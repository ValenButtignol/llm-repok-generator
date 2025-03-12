from classes.class_format.class_format_interface import ClassFormatInterface
from classes.string_constants import BEGIN_CODE_SNIPPET, END_CODE_SNIPPET

class WholeClassFormat(ClassFormatInterface): 
    def __init__(self, raw_class: str, class_name: str):
        self.raw_class = raw_class
        self.class_name = class_name
        self.formatted_class = ""

    def get_formatted_class(self) -> str:
        self.formatted_class += BEGIN_CODE_SNIPPET + "\n" + self.raw_class + "\n" + END_CODE_SNIPPET 
        return self.formatted_class