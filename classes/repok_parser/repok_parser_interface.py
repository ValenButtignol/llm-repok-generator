class RepOkParserInterface:

    def set_repOk_completion(self, repOk_completion : str):
        self.repOk_completion = repOk_completion

    def parse(self) -> str:
        raise NotImplementedError
    