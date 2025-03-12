from classes.factories.dual_prompt_type_factory import DualPromptTypeFactory
from classes.factories.simple_prompt_type_factory import SimplePromptTypeFactory
from classes.factories.prompt_type_factory_inteface import PromptTypeFactoryInterface
from classes.string_constants import USER_BASIC_REPOK_PT, SYSTEM_BASIC_REPOK_PT, USER_HINTS_REPOK_PT, SYSTEM_HINTS_REPOK_PT, USER_FS_REPOK_PT, USER_ASSISTANT_FS_REPOK_PT, USER_HINTS_USER_FS_REPOK_PT, USER_HINTS_USER_ASSISTANT_FS_REPOK_PT, SYSTEM_HINTS_USER_FS_REPOK_PT, SYSTEM_HINTS_USER_ASSISTANT_FS_REPOK_PT, USER_BASIC_PROPS_PT, SYSTEM_BASIC_PROPS_PT, USER_HINTS_PROPS_PT, SYSTEM_HINTS_PROPS_PT, USER_FS_PROPS_PT, USER_ASSISTANT_FS_PROPS_PT, USER_HINTS_USER_FS_PROPS_PT, USER_HINTS_USER_ASSISTANT_FS_PROPS_PT, SYSTEM_HINTS_USER_FS_PROPS_PT, SYSTEM_HINTS_USER_ASSISTANT_FS_PROPS_PT

class SystemAbstractFactory:
    def __init__(self, prompt_type, raw_class, class_name):
        self.prompt_type = prompt_type
        self.raw_class = raw_class
        self.class_name = class_name

    def create(self) -> PromptTypeFactoryInterface:
        if self.prompt_type == USER_BASIC_REPOK_PT:
            return SimplePromptTypeFactory(self.prompt_type, self.raw_class, self.class_name) 
        elif self.prompt_type == SYSTEM_BASIC_REPOK_PT:
            return SimplePromptTypeFactory(self.prompt_type, self.raw_class, self.class_name) 
        elif self.prompt_type == USER_HINTS_REPOK_PT:
            return SimplePromptTypeFactory(self.prompt_type, self.raw_class, self.class_name) 
        elif self.prompt_type == SYSTEM_HINTS_REPOK_PT:
            return SimplePromptTypeFactory(self.prompt_type, self.raw_class, self.class_name) 
        elif self.prompt_type == USER_FS_REPOK_PT:
            return SimplePromptTypeFactory(self.prompt_type, self.raw_class, self.class_name) 
        elif self.prompt_type == USER_ASSISTANT_FS_REPOK_PT:
            return SimplePromptTypeFactory(self.prompt_type, self.raw_class, self.class_name) 
        elif self.prompt_type == USER_HINTS_USER_FS_REPOK_PT:
            return SimplePromptTypeFactory(self.prompt_type, self.raw_class, self.class_name) 
        elif self.prompt_type == USER_HINTS_USER_ASSISTANT_FS_REPOK_PT:
            return SimplePromptTypeFactory(self.prompt_type, self.raw_class, self.class_name) 
        elif self.prompt_type == SYSTEM_HINTS_USER_FS_REPOK_PT:
            return SimplePromptTypeFactory(self.prompt_type, self.raw_class, self.class_name) 
        elif self.prompt_type == SYSTEM_HINTS_USER_ASSISTANT_FS_REPOK_PT:
            return SimplePromptTypeFactory(self.prompt_type, self.raw_class, self.class_name) 
        elif self.prompt_type == USER_BASIC_PROPS_PT:
            return DualPromptTypeFactory(self.prompt_type, self.raw_class, self.class_name) 
        elif self.prompt_type == SYSTEM_BASIC_PROPS_PT:
            return DualPromptTypeFactory(self.prompt_type, self.raw_class, self.class_name) 
        elif self.prompt_type == USER_HINTS_PROPS_PT:
            return DualPromptTypeFactory(self.prompt_type, self.raw_class, self.class_name) 
        elif self.prompt_type == SYSTEM_HINTS_PROPS_PT:
            return DualPromptTypeFactory(self.prompt_type, self.raw_class, self.class_name) 
        elif self.prompt_type == USER_FS_PROPS_PT:
            return DualPromptTypeFactory(self.prompt_type, self.raw_class, self.class_name) 
        elif self.prompt_type == USER_ASSISTANT_FS_PROPS_PT:
            return DualPromptTypeFactory(self.prompt_type, self.raw_class, self.class_name) 
        elif self.prompt_type == USER_HINTS_USER_FS_PROPS_PT:
            return DualPromptTypeFactory(self.prompt_type, self.raw_class, self.class_name) 
        elif self.prompt_type == USER_HINTS_USER_ASSISTANT_FS_PROPS_PT:
            return DualPromptTypeFactory(self.prompt_type, self.raw_class, self.class_name) 
        elif self.prompt_type == SYSTEM_HINTS_USER_FS_PROPS_PT:
            return DualPromptTypeFactory(self.prompt_type, self.raw_class, self.class_name) 
        elif self.prompt_type == SYSTEM_HINTS_USER_ASSISTANT_FS_PROPS_PT:
            return DualPromptTypeFactory(self.prompt_type, self.raw_class, self.class_name) 
        else:
            raise Exception("Invalid prompt type: " + self.prompt_type + "\n")
