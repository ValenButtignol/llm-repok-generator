from classes.prompt.json_prompt import JsonPrompt
from classes.prompt.global_repok_prompt import GlobalRepOkPrompt
from classes.prompt.global_repok_fewshot_wholeclass_prompt import GlobalRepOkFewShotWholeClassPrompt
from classes.prompt.global_repok_fewshot_partsofclass_prompt import GlobalRepOkFewShotPartsOfClassPrompt
from classes.prompt.dual_properties_wholeclass_prompt import DualPropertiesWholeClassPrompt
from classes.prompt.dual_properties_partsofclass_prompt import DualPropertiesPartsOfClassPrompt

class PromptFactory:
    def __init__(self):
        pass
    
    def create(self, prompt_type, raw_class, class_name) -> JsonPrompt:
        if prompt_type == "global":
            return GlobalRepOkPrompt(raw_class, class_name)
        elif prompt_type == "fs-w":
            return GlobalRepOkFewShotWholeClassPrompt(raw_class, class_name)
        elif prompt_type == "fs-p":
            return GlobalRepOkFewShotPartsOfClassPrompt(raw_class, class_name)
        elif prompt_type == "dual-w":
            return DualPropertiesWholeClassPrompt(raw_class, class_name)
        elif prompt_type == "dual-p":
            return DualPropertiesPartsOfClassPrompt(raw_class, class_name)
    
        else:
            raise Exception("Invalid prompt type: " + prompt_type + "\n")
