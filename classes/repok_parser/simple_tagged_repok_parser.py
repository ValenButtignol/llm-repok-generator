from classes.repok_parser.repok_parser_interface import RepOkParserInterface
from classes.string_constants import REPOK_TAG, BEGIN_CODE_SNIPPET, END_CODE_SNIPPET, REPOK_CLASS_PREFIX, REPOK_CLASS_SUFFIX, TAB

class SimpleTaggedRepOkParser(RepOkParserInterface):

    def __init__(self):
        super().__init__()

    def parse(self) -> str:
        repOk = self._parse_repOk()
        repOk_class = self._build_repOk_class(repOk)
        return repOk_class
    
    def _parse_repOk(self):
        start = self.repOk_completion.index(REPOK_TAG + BEGIN_CODE_SNIPPET) + len(REPOK_TAG + BEGIN_CODE_SNIPPET)
        end = self.repOk_completion.index(END_CODE_SNIPPET, start)
        return self.repOk_completion[start:end]

    def _build_repOk_class(self, repOk_text : str) -> str:
        code_snippet = REPOK_CLASS_PREFIX
        for line in repOk_text.split("\n"):
            code_snippet += TAB + line + "\n"
        
        code_snippet += REPOK_CLASS_SUFFIX

        return code_snippet