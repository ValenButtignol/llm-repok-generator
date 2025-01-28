from classes.repok_parser.repok_parser_interface import RepOkParserInterface

class DualRepOkParser(RepOkParserInterface):

    def __init__(self, prompt_output: str):
        self.prompt_output = prompt_output

    def parse(self) -> str:
        raise NotImplementedError