from classes.factories.dual_prompt_type_factory import DualPromptTypeFactory
from classes.factories.global_prompt_type_factory import GlobalPromptTypeFactory
from classes.factories.prompt_type_factory_inteface import PromptTypeFactoryInterface
from classes.string_constants import DUAL_PARTSOFCLASS_PROMPT_TYPE, DUAL_WHOLECLASS_PROMPT_TYPE, FEWSHOT_OPENAI_PARTSOFCLASS_PROMPT_TYPE, FEWSHOT_OPENAI_WHOLECLASS_PROMPT_TYPE, FEWSHOT_PARTSOFCLASS_PROMPT_TYPE, FEWSHOT_WHOLECLASS_PROMPT_TYPE, GLOBAL_PROMPT_TYPE


class SystemAbstractFactory:
    def __init__(self, prompt_type, raw_class, class_name):
        self.prompt_type = prompt_type
        self.raw_class = raw_class
        self.class_name = class_name

    def create(self) -> PromptTypeFactoryInterface:
        if self.prompt_type == GLOBAL_PROMPT_TYPE:
            return GlobalPromptTypeFactory(self.prompt_type, self.raw_class, self.class_name)
        elif self.prompt_type == FEWSHOT_WHOLECLASS_PROMPT_TYPE:
            return GlobalPromptTypeFactory(self.prompt_type, self.raw_class, self.class_name)
        elif self.prompt_type == FEWSHOT_PARTSOFCLASS_PROMPT_TYPE:
            return GlobalPromptTypeFactory(self.prompt_type, self.raw_class, self.class_name)
        elif self.prompt_type == FEWSHOT_OPENAI_WHOLECLASS_PROMPT_TYPE:
            return GlobalPromptTypeFactory(self.prompt_type, self.raw_class, self.class_name)
        elif self.prompt_type == FEWSHOT_OPENAI_PARTSOFCLASS_PROMPT_TYPE:
            return GlobalPromptTypeFactory(self.prompt_type, self.raw_class, self.class_name)
        elif self.prompt_type == DUAL_WHOLECLASS_PROMPT_TYPE:
            return DualPromptTypeFactory(self.prompt_type, self.raw_class, self.class_name)
        elif self.prompt_type == DUAL_PARTSOFCLASS_PROMPT_TYPE:
            return DualPromptTypeFactory(self.prompt_type, self.raw_class, self.class_name)
    
        else:
            raise Exception("Invalid prompt type: " + self.prompt_type + "\n")
