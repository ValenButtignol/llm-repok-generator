from classes.repok_parser.repok_parser_interface import RepOkParserInterface
from classes.string_constants import END_CODE_SNIPPET, OPEN_REASONING_TAG, CLOSE_REASONING_TAG, BEGIN_CODE_SNIPPET, PROPERTY_METHOD_NAME, CLASS_SUFFIX, REPOK_CLASS_FILENAME, REPOK_CLASS_PREFIX, TAB

class PropertyMethodParser(RepOkParserInterface):

    def __init__(self):
        super().__init__()

    def parse(self) -> str:
        code_properties = self._parse_code_properties()
        self._enumerate_properties(code_properties)
        return self._build_repOk_classes(code_properties)
    
    def _parse_code_properties(self):
        properties = []
        lines = self.repOk_completion.splitlines()
        inside_reasoning = False
        inside_property = False
        current_property = ""

        for line in lines:
            if line.strip() == OPEN_REASONING_TAG:
                inside_reasoning = True
            elif line.strip() == CLOSE_REASONING_TAG:
                inside_reasoning = False
            elif not inside_reasoning and line.strip() == BEGIN_CODE_SNIPPET:
                inside_property = True
                continue
            elif not inside_reasoning and line.strip() == END_CODE_SNIPPET:
                properties.append(current_property)
                current_property = ""
                inside_property = False
            elif inside_property:
                current_property += TAB + line + "\n"
        
        return properties
    def _enumerate_properties(self, code_properties : list):
        for i, prop in enumerate(code_properties):
            enumerated_prop = prop.replace(PROPERTY_METHOD_NAME, PROPERTY_METHOD_NAME + str(i+1))
            code_properties[i] = enumerated_prop    

    def _build_repOk_classes(self, prop_list) -> str:
        classes = []
        class_number = 1
        for prop in prop_list:
            prop_class = REPOK_CLASS_PREFIX(class_number) 
            prop_class += prop + "\n"
            prop_class += CLASS_SUFFIX
            classes.append((prop_class, REPOK_CLASS_FILENAME(class_number)))
            class_number += 1

        return classes
