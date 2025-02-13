from classes.factories.prompt_type_factory_inteface import PromptTypeFactoryInterface
from classes.model_executor.simple_model_executor import SimpleModelExecutor
from classes.output_manager.file_output_manager import FileOutputManager
from classes.prompt.global_repok_fewshot_partsofclass_prompt import GlobalRepOkFewShotPartsOfClassPrompt
from classes.prompt.global_repok_fewshot_wholeclass_prompt import GlobalRepOkFewShotWholeClassPrompt
from classes.prompt.global_repok_prompt import GlobalRepOkPrompt
from classes.repok_parser.simple_tagged_repok_parser import SimpleTaggedRepOkParser
from classes.repok_parser.simple_untagged_repok_parser import SimpleUntaggedRepOkParser
from classes.string_constants import FEWSHOT_OPENAI_WHOLECLASS_PROMPT_TYPE, FEWSHOT_PARTSOFCLASS_PROMPT_TYPE, FEWSHOT_WHOLECLASS_PROMPT_TYPE, GLOBAL_PROMPT_TYPE

class GlobalPromptTypeFactory(PromptTypeFactoryInterface):
    def __init__(self, prompt_type, raw_class, class_name):
        self.prompt_type = prompt_type
        self.raw_class = raw_class
        self.class_name = class_name

    def create_output_manager(self):
        return FileOutputManager()

    def create_prompt(self):
        if self.prompt_type == GLOBAL_PROMPT_TYPE:
            return GlobalRepOkPrompt(self.raw_class, self.class_name)
        elif self.prompt_type == FEWSHOT_WHOLECLASS_PROMPT_TYPE:
            return GlobalRepOkFewShotWholeClassPrompt(self.raw_class, self.class_name)
        elif self.prompt_type == FEWSHOT_PARTSOFCLASS_PROMPT_TYPE:
            return GlobalRepOkFewShotPartsOfClassPrompt(self.raw_class, self.class_name)
        elif self.prompt_type == FEWSHOT_OPENAI_WHOLECLASS_PROMPT_TYPE:
            return GlobalRepOkPrompt(self.raw_class, self.class_name)

    def create_repok_parser(self):
        return SimpleUntaggedRepOkParser()
        
    def create_model_executor(self):
        return SimpleModelExecutor()