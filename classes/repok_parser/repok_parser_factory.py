from classes.repok_parser.dual_prop_repok_parser import DualPropRepOkParser
from classes.repok_parser.simple_tagged_repok_parser import SimpleTaggedRepOkParser
from classes.repok_parser.simple_untagged_repok_parser import SimpleUntaggedRepOkParser

class RepOkParserFactory:
    def create(self, prompt_type):
        if prompt_type == "global":
            return SimpleUntaggedRepOkParser()
        elif prompt_type == "fs-w":
            return SimpleTaggedRepOkParser()
        elif prompt_type == "fs-p":
            return SimpleTaggedRepOkParser()
        elif prompt_type == "dual-w":
            return DualPropRepOkParser()
        elif prompt_type == "dual-p":
            return DualPropRepOkParser()
    
        else:
            raise Exception("Invalid prompt type: " + prompt_type + "\n")