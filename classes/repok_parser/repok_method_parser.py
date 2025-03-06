from classes.repok_parser.repok_parser_interface import RepOkParserInterface
from classes.string_constants import CLOSE_REASONING_TAG, OPEN_REASONING_TAG, REPOK_CLASS_FILENAME, BEGIN_CODE_SNIPPET, END_CODE_SNIPPET, REPOK_CLASS_PREFIX, CLASS_SUFFIX, TAB

class RepOkMethodParser(RepOkParserInterface):

    def __init__(self):
        super().__init__()

    def parse(self) -> str:
        repOk = self._parse_repOk()
        return self._build_repOk_classes(repOk)
    
    def _parse_repOk(self):
        method = ""
        lines = self.repOk_completion.splitlines()
        inside_reasoning = False
        inside_method = False

        for line in lines:
            if line.strip() == OPEN_REASONING_TAG:
                inside_reasoning = True
            elif line.strip == CLOSE_REASONING_TAG:
                inside_reasoning = False
            elif not inside_reasoning and line.strip() == BEGIN_CODE_SNIPPET:
                inside_method = True
                continue
            elif not inside_reasoning and line.strip() == END_CODE_SNIPPET:
                inside_method = False
            elif inside_method:
                method += line + "\n"
        
        return method


    def _build_repOk_classes(self, repOk_text : str) -> str:
        class_number = 1
        code_snippet = REPOK_CLASS_PREFIX(class_number)
        for line in repOk_text.split("\n"):
            code_snippet += TAB + line + "\n"
        
        code_snippet += CLASS_SUFFIX
        return [(code_snippet, REPOK_CLASS_FILENAME(class_number))]