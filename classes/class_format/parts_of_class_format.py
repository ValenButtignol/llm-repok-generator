import jpype
import jpype.imports
from classes.class_format.class_format_interface import ClassFormatInterface
from classes.string_constants import TOOLS_FOLDER, JAVAPARSER_JAR, CLASS_SIGNATURE, CLASS_METHODS, CLASS_ATTRS

class PartsOfClassFormat(ClassFormatInterface): 
    def __init__(self, raw_class: str, class_name: str):
        self.raw_class = raw_class
        self.class_name = class_name
        self.formatted_class = ""
        self.initialize_jvm()

    def initialize_jvm(self):
        jpype.startJVM(classpath=[TOOLS_FOLDER + JAVAPARSER_JAR])
        from com.github.javaparser import JavaParser

        parser = JavaParser()
        parseResult = parser.parse(self.raw_class)
        if not parseResult.isSuccessful():
            raise Exception(f"Fail to parse class {self.class_name}")
        
        self.compilation_unit = parseResult.getResult().get()

    def get_formatted_class(self) -> str:
        class_declaration = self.compilation_unit.getClassByName(self.class_name).get()
        self._parse_class_declaration(class_declaration)
        self._parse_class_attributes(class_declaration)
        self._parse_class_methods(class_declaration)
        return self.formatted_class
    
    def _parse_class_declaration(self, class_declaration):
        self.formatted_class += CLASS_SIGNATURE
        self.formatted_class += f"{self.fix_format(class_declaration.getModifiers())}{class_declaration.getName()} \n"

    def _parse_class_attributes(self, class_declaration):
        self.formatted_class += CLASS_ATTRS
        for field in class_declaration.getFields():
           for var in field.getVariables():
                self.formatted_class += f"{self.fix_format(field.getModifiers())}{var.getType()} {var.getName()} \n"

    def _parse_class_methods(self, class_declaration):
        self.formatted_class += CLASS_METHODS
        for method in class_declaration.getMethods():
            self.formatted_class += f"{self.fix_format(method.getModifiers())}{method.getType()} {method.getName()}({self.fix_format(method.getParameters(), True)})"
            if method.getBody().isPresent():
                self.formatted_class += str(method.getBody().get()) + "\n"
            else:
                self.formatted_class += ";\n"

    def fix_format(self, list_of_words, are_parameters=False):
        result = ''.join([str(word) for word in list_of_words]).strip()
        if not are_parameters:
            result += " " 
        return result