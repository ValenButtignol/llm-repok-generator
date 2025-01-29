from classes.repok_parser.repok_parser_interface import RepOkParserInterface
from classes.string_constants import END_CODE_SNIPPET, PROPERTY_TAG, BEGIN_CODE_SNIPPET, PROPERTY_METHOD_NAME, PROP_CLASS_PREFIX, CLASS_SUFFIX, TAB

class DualPropRepOkParser(RepOkParserInterface):

    def __init__(self):
        super().__init__()

    def parse(self) -> str:
        code_properties = self._parse_code_properties()
        self._enumerate_properties(code_properties)
        return self._build_properties_class(code_properties)
    
    def _parse_code_properties(self):
        properties = []
        lines = self.repOk_completion.splitlines()
        inside_property = False
        current_property = ""

        for line in lines:
            if line.strip() == PROPERTY_TAG:
                inside_property = True
            elif inside_property and line.strip() == BEGIN_CODE_SNIPPET:
                continue
            elif inside_property and line.strip() == END_CODE_SNIPPET:
                properties.append(current_property)
                inside_property = False
                current_property = ""
            elif inside_property:
                current_property += TAB + line + "\n"

        return properties

    def _enumerate_properties(self, code_properties : list):
        for i, prop in enumerate(code_properties):
            enumerated_prop = prop.replace(PROPERTY_METHOD_NAME, PROPERTY_METHOD_NAME + str(i+1))
            code_properties[i] = enumerated_prop

    def _build_properties_class(self, prop_list) -> str:
        prop_class = PROP_CLASS_PREFIX
        for prop in prop_list:
            prop_class += prop + "\n"
        prop_class += CLASS_SUFFIX

        return prop_class
