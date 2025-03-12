from classes.factories.prompt_type_factory_inteface import PromptTypeFactoryInterface
from classes.model_executor.simple_model_executor import SimpleModelExecutor
from classes.output_manager.file_output_manager import FileOutputManager
from classes.prompt.repok_prompts.repok_user_basic_prompt import RepOKUserBasicPrompt
from classes.prompt.repok_prompts.repok_system_basic_prompt import RepOKSystemBasicPrompt
from classes.prompt.repok_prompts.repok_user_hints_prompt import RepOKUserHintsPrompt
from classes.prompt.repok_prompts.repok_system_hints_prompt import RepOKSystemHintsPrompt
from classes.prompt.repok_prompts.repok_user_fewshot_prompt import RepOKUserFewShotPrompt
from classes.prompt.repok_prompts.repok_user_assistant_fewshot_prompt import RepOKUserAssistantFewShotPrompt
from classes.prompt.repok_prompts.repok_user_hints_fewshot_prompt import RepOKUserHintsFewShotPrompt
from classes.prompt.repok_prompts.repok_user_hints_user_assistant_fewshot_prompt import RepOKUserHintsUserAssistantFewShotPrompt
from classes.prompt.repok_prompts.repok_system_hints_user_fewshot import RepOKSystemHintsUserFewShotPrompt
from classes.prompt.repok_prompts.repok_system_hints_user_assistant_fewshot import RepOKSystemHintsUserAssistantFewShotPrompt
from classes.string_constants import USER_BASIC_REPOK_PT, SYSTEM_BASIC_REPOK_PT, USER_HINTS_REPOK_PT, SYSTEM_HINTS_REPOK_PT, USER_FS_REPOK_PT, USER_ASSISTANT_FS_REPOK_PT, USER_HINTS_USER_FS_REPOK_PT, USER_HINTS_USER_ASSISTANT_FS_REPOK_PT, SYSTEM_HINTS_USER_FS_REPOK_PT, SYSTEM_HINTS_USER_ASSISTANT_FS_REPOK_PT

class SimplePromptTypeFactory(PromptTypeFactoryInterface):
    def __init__(self, prompt_type, raw_class, class_name):
        self.prompt_type = prompt_type
        self.raw_class = raw_class
        self.class_name = class_name

    def create_output_manager(self):
        return FileOutputManager()

    def create_prompt(self):
        if self.prompt_type == USER_BASIC_REPOK_PT:
            return RepOKUserBasicPrompt(self.raw_class, self.class_name)
        elif self.prompt_type == SYSTEM_BASIC_REPOK_PT:
            return RepOKSystemBasicPrompt(self.raw_class, self.class_name)
        elif self.prompt_type == USER_HINTS_REPOK_PT:
            return RepOKUserHintsPrompt(self.raw_class, self.class_name)
        elif self.prompt_type == SYSTEM_HINTS_REPOK_PT:
            return RepOKSystemHintsPrompt(self.raw_class, self.class_name)
        elif self.prompt_type == USER_FS_REPOK_PT:
            return RepOKUserFewShotPrompt(self.raw_class, self.class_name)
        elif self.prompt_type == USER_ASSISTANT_FS_REPOK_PT:
            return RepOKUserAssistantFewShotPrompt(self.raw_class, self.class_name)
        elif self.prompt_type == USER_HINTS_USER_FS_REPOK_PT:
            return RepOKUserHintsFewShotPrompt(self.raw_class, self.class_name)
        elif self.prompt_type == USER_HINTS_USER_ASSISTANT_FS_REPOK_PT:
            return RepOKUserHintsUserAssistantFewShotPrompt(self.raw_class, self.class_name)
        elif self.prompt_type == SYSTEM_HINTS_USER_FS_REPOK_PT:
            return RepOKSystemHintsUserFewShotPrompt(self.raw_class, self.class_name)
        elif self.prompt_type == SYSTEM_HINTS_USER_ASSISTANT_FS_REPOK_PT:
            return RepOKSystemHintsUserAssistantFewShotPrompt(self.raw_class, self.class_name)

    def create_model_executor(self):
        return SimpleModelExecutor()