from classes.factories.prompt_type_factory_inteface import PromptTypeFactoryInterface
from classes.model_executor.dual_partsofclass_model_executor import DualPartsOfClassModelExecutor
from classes.model_executor.dual_wholeclass_model_executor import DualWholeClassModelExecutor
from classes.output_manager.file_output_manager import FileOutputManager
from classes.prompt.dual_properties_partsofclass_prompt import DualPropertiesPartsOfClassPrompt
from classes.prompt.dual_properties_wholeclass_prompt import DualPropertiesWholeClassPrompt
from classes.repok_parser.dual_prop_repok_parser import DualPropRepOkParser
from classes.string_constants import DUAL_PARTSOFCLASS_PROMPT_TYPE, DUAL_WHOLECLASS_PROMPT_TYPE


class DualPromptTypeFactory(PromptTypeFactoryInterface):
    def __init__(self, prompt_type, raw_class, class_name):
        self.prompt_type = prompt_type
        self.raw_class = raw_class
        self.class_name = class_name

    def create_output_manager(self):
        return FileOutputManager()

    def create_prompt(self):
        if self.prompt_type == DUAL_WHOLECLASS_PROMPT_TYPE:
            return DualPropertiesWholeClassPrompt(self.raw_class, self.class_name)
        elif self.prompt_type == DUAL_PARTSOFCLASS_PROMPT_TYPE:
            return DualPropertiesPartsOfClassPrompt(self.raw_class, self.class_name)

    def create_repok_parser(self):
        return DualPropRepOkParser()
    
    def create_model_executor(self):
        if self.prompt_type == DUAL_WHOLECLASS_PROMPT_TYPE:
            return DualWholeClassModelExecutor()
        elif self.prompt_type == DUAL_PARTSOFCLASS_PROMPT_TYPE:
            return DualPartsOfClassModelExecutor()