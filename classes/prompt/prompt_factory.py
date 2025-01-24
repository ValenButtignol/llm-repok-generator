from classes.prompt.json_prompt import JsonPrompt
from classes.prompt.global_repok_prompt import GlobalRepOkPrompt
from classes.prompt.global_repok_fewshot_wholeclass_prompt import GlobalRepOkFewShotWholeClassPrompt
from classes.prompt.global_repok_fewshot_partsofclass_prompt import GlobalRepOkFewShotPartsOfClassPrompt
from classes.prompt.dual_properties_wholeclass_prompt import DualPropertiesWholeClassPrompt
from classes.prompt.dual_properties_partsofclass_prompt import DualPropertiesPartsOfClassPrompt

class PromptFactory:
    def __init__(self):
        pass
    
    def create(self, prompt_type, prompt_container, class_name) -> JsonPrompt:
        if prompt_type == "global":
            return GlobalRepOkPrompt(prompt_container, class_name)
        elif prompt_type == "fs-w":
            return GlobalRepOkFewShotWholeClassPrompt(prompt_container, class_name)
        elif prompt_type == "fs-p":
            return GlobalRepOkFewShotPartsOfClassPrompt(prompt_container, class_name)
        elif prompt_type == "dual-w":
            return DualPropertiesWholeClassPrompt(prompt_container, class_name)
        elif prompt_type == "dual-p":
            return DualPropertiesPartsOfClassPrompt(prompt_container, class_name)
    
        else:
            raise Exception("Invalid prompt type: " + prompt_type + "\n")
