from classes.prompt.json_prompt import JsonPrompt
from classes.prompt.global_repok_prompt import GlobalRepOkPrompt
from classes.prompt.global_repok_fewshot_wholeclass_prompt import GlobalRepOkFewShotWholeClassPrompt
from classes.prompt.global_repok_fewshot_partsofclass_prompt import GlobalRepOkFewShotPartsOfClassPrompt
from classes.prompt.dual_properties_wholeclass_prompt import DualPropertiesWholeClassPrompt
from classes.prompt.dual_properties_partsofclass_prompt import DualPropertiesPartsOfClassPrompt
from classes.string_constants import GLOBAL_PROMPT_TYPE, FEWSHOT_WHOLECLASS_PROMPT_TYPE, FEWSHOT_PARTSOFCLASS_PROMPT_TYPE, DUAL_WHOLECLASS_PROMPT_TYPE, DUAL_PARTSOFCLASS_PROMPT_TYPE

class PromptFactory:
    def __init__(self):
        pass
    
    def create(self, prompt_type, raw_class, class_name) -> JsonPrompt:
        if prompt_type == GLOBAL_PROMPT_TYPE:
            return GlobalRepOkPrompt(raw_class, class_name)
        elif prompt_type == FEWSHOT_WHOLECLASS_PROMPT_TYPE:
            return GlobalRepOkFewShotWholeClassPrompt(raw_class, class_name)
        elif prompt_type == FEWSHOT_PARTSOFCLASS_PROMPT_TYPE:
            return GlobalRepOkFewShotPartsOfClassPrompt(raw_class, class_name)
        elif prompt_type == DUAL_WHOLECLASS_PROMPT_TYPE:
            return DualPropertiesWholeClassPrompt(raw_class, class_name)
        elif prompt_type == DUAL_PARTSOFCLASS_PROMPT_TYPE:
            return DualPropertiesPartsOfClassPrompt(raw_class, class_name)
    
        else:
            raise Exception("Invalid prompt type: " + prompt_type + "\n")
