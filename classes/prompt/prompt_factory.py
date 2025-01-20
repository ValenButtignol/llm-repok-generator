from classes.prompt.prompt_interface import PromptInterface
from classes.prompt.file_prompt import FilePrompt
from classes.prompt.json_prompt import JsonPrompt
from classes.prompt.plain_text_prompt import PlainTextPrompt
from classes.prompt.template_prompts.global_repok_prompt import GlobalRepOkPrompt
from classes.prompt.template_prompts.global_repok_fewshot_wholeclass_prompt import GlobalRepOkFewShotWholeClassPrompt
from classes.prompt.template_prompts.global_repok_fewshot_partsofclass_prompt import GlobalRepOkFewShotPartsOfClassPrompt
from classes.prompt.template_prompts.global_repok_fewshot_cot_wholeclass_prompt import GlobalRepOkFewShotCoTWholeClassPrompt
from classes.prompt.template_prompts.global_repok_fewshot_cot_partsofclass_prompt import GlobalRepOkFewShotCoTPartsOfClassPrompt
from classes.prompt.template_prompts.dual_properties_wholeclass_prompt import DualPropertiesWholeClassPrompt
from classes.prompt.template_prompts.dual_properties_partsofclass_prompt import DualPropertiesPartsOfClassPrompt

class PromptFactory:
    def __init__(self):
        pass
    
    def create(self, prompt_type, prompt_container) -> PromptInterface:
        if prompt_type == "text":
            return PlainTextPrompt(prompt_container)
        elif prompt_type == "file":
            return FilePrompt(prompt_container)
        elif prompt_type == "json":
            return JsonPrompt(prompt_container) 
        elif prompt_type == "global":
            return GlobalRepOkPrompt(prompt_container)
        elif prompt_type == "fs-w":
            return GlobalRepOkFewShotWholeClassPrompt(prompt_container)
        elif prompt_type == "fs-p":
            return GlobalRepOkFewShotPartsOfClassPrompt(prompt_container)
        elif prompt_type == "fs-cot-w":
            return GlobalRepOkFewShotCoTWholeClassPrompt(prompt_container)
        elif prompt_type == "fs-cot-p":
            return GlobalRepOkFewShotCoTPartsOfClassPrompt(prompt_container)
        elif prompt_type == "dual-w":
            return DualPropertiesWholeClassPrompt(prompt_container)
        elif prompt_type == "dual-p":
            return DualPropertiesPartsOfClassPrompt(prompt_container)
    
        else:
            raise Exception("Invalid prompt type: " + prompt_type + "\n")
