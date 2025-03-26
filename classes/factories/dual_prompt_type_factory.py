from classes.factories.prompt_type_factory_inteface import PromptTypeFactoryInterface
from classes.model_executor.dual_model_executor import DualModelExecutor
from classes.model_executor.only_spec_executor import OnlySpecExecutor
from classes.output_manager.file_output_manager import FileOutputManager
from classes.prompt.props_prompts.props_user_basic_prompt import CodePropUserBasicPrompt, TextPropsUserBasicPrompt
from classes.prompt.props_prompts.props_system_basic_prompt import CodePropSystemBasicPrompt, TextPropsSystemBasicPrompt
from classes.prompt.props_prompts.props_user_hints_prompt import CodePropUserHintsPrompt, TextPropsUserHintsPrompt
from classes.prompt.props_prompts.props_system_hints_prompt import CodePropSystemHintsPrompt, TextPropsSystemHintsPrompt
from classes.prompt.props_prompts.props_user_fewshot_prompt import CodePropUserFewShotPrompt, TextPropsUserFewShotPrompt
from classes.prompt.props_prompts.props_user_assistant_fewshot_prompt import CodePropUserAssistantFewShotPrompt, TextPropsUserAssistantFewShotPrompt
from classes.prompt.props_prompts.props_user_hints_fewshot_prompt import CodePropUserHintsFewShotPrompt, TextPropsUserHintsFewShotPrompt
from classes.prompt.props_prompts.props_user_hints_user_assistant_fewshot_prompt import CodePropUserHintsUserAssistantFewShotPrompt, TextPropsUserHintsUserAssistantFewShotPrompt
from classes.prompt.props_prompts.props_system_hints_user_fewshot import CodePropSystemHintsUserFewShotPrompt, TextPropsSystemHintsUserFewShotPrompt
from classes.prompt.props_prompts.props_system_hints_user_assistant_fewshot import CodePropSystemHintsUserAssistantFewShotPrompt, TextPropsSystemHintsUserAssistantFewShotPrompt
from classes.prompt.props_prompts.spec_fewshot_prompt import RepOKSpecFewShotPrompt, RepOKSpecOnlyFewShotPrompt, SpecFewShotPrompt
from classes.prompt.props_prompts.spec_prompt import RepOKSpecOnlyPrompt, RepOKSpecPrompt, SpecPrompt
from classes.string_constants import USER_BASIC_PROPS_PT, SYSTEM_BASIC_PROPS_PT, USER_HINTS_PROPS_PT, SYSTEM_HINTS_PROPS_PT, USER_FS_PROPS_PT, USER_ASSISTANT_FS_PROPS_PT, USER_HINTS_USER_FS_PROPS_PT, USER_HINTS_USER_ASSISTANT_FS_PROPS_PT, SYSTEM_HINTS_USER_FS_PROPS_PT, SYSTEM_HINTS_USER_ASSISTANT_FS_PROPS_PT


class DualPromptTypeFactory(PromptTypeFactoryInterface):
    def __init__(self, prompt_type, raw_class, class_name):
        self.prompt_type = prompt_type
        self.raw_class = raw_class
        self.class_name = class_name
        self.dual_prompt = None

    def create_output_manager(self):
        return FileOutputManager()

    def create_prompt(self):
        if self.prompt_type == USER_BASIC_PROPS_PT:
            self.dual_prompt = CodePropUserBasicPrompt(self.raw_class, self.class_name)
            return TextPropsUserBasicPrompt(self.raw_class, self.class_name)
        elif self.prompt_type == SYSTEM_BASIC_PROPS_PT:
            self.dual_prompt = CodePropSystemBasicPrompt(self.raw_class, self.class_name)
            return TextPropsSystemBasicPrompt(self.raw_class, self.class_name)
        elif self.prompt_type == USER_HINTS_PROPS_PT:
            self.dual_prompt = CodePropUserHintsPrompt(self.raw_class, self.class_name)
            return TextPropsUserHintsPrompt(self.raw_class, self.class_name)
        elif self.prompt_type == SYSTEM_HINTS_PROPS_PT:
            self.dual_prompt = CodePropSystemHintsPrompt(self.raw_class, self.class_name)
            return TextPropsSystemHintsPrompt(self.raw_class, self.class_name)
        elif self.prompt_type == USER_FS_PROPS_PT:
            self.dual_prompt = CodePropUserFewShotPrompt(self.raw_class, self.class_name)
            return TextPropsUserFewShotPrompt(self.raw_class, self.class_name)
        elif self.prompt_type == USER_ASSISTANT_FS_PROPS_PT:
            self.dual_prompt = CodePropUserAssistantFewShotPrompt(self.raw_class, self.class_name)
            return TextPropsUserAssistantFewShotPrompt(self.raw_class, self.class_name)
        elif self.prompt_type == USER_HINTS_USER_FS_PROPS_PT:
            self.dual_prompt = CodePropUserHintsFewShotPrompt(self.raw_class, self.class_name)
            return TextPropsUserHintsFewShotPrompt(self.raw_class, self.class_name)
        elif self.prompt_type == USER_HINTS_USER_ASSISTANT_FS_PROPS_PT:
            self.dual_prompt = CodePropUserHintsUserAssistantFewShotPrompt(self.raw_class, self.class_name)
            return TextPropsUserHintsUserAssistantFewShotPrompt(self.raw_class, self.class_name)
        elif self.prompt_type == SYSTEM_HINTS_USER_FS_PROPS_PT:
            self.dual_prompt = CodePropSystemHintsUserFewShotPrompt(self.raw_class, self.class_name)
            return TextPropsSystemHintsUserFewShotPrompt(self.raw_class, self.class_name)
        elif self.prompt_type == SYSTEM_HINTS_USER_ASSISTANT_FS_PROPS_PT:
            self.dual_prompt = CodePropSystemHintsUserAssistantFewShotPrompt(self.raw_class, self.class_name)
            return TextPropsSystemHintsUserAssistantFewShotPrompt(self.raw_class, self.class_name)
        elif self.prompt_type == "spec":
            self.dual_prompt = RepOKSpecPrompt(self.raw_class, self.class_name)
            return SpecPrompt(self.raw_class, self.class_name)
        elif self.prompt_type == "spec-only":
            self.dual_prompt = RepOKSpecOnlyPrompt(self.raw_class, self.class_name)
            return SpecPrompt(self.raw_class, self.class_name)
        elif self.prompt_type == "spec-fs":
            self.dual_prompt = RepOKSpecFewShotPrompt(self.raw_class, self.class_name)
            return SpecFewShotPrompt(self.raw_class, self.class_name)
        elif self.prompt_type == "spec-only-fs":
            self.dual_prompt = RepOKSpecOnlyFewShotPrompt(self.raw_class, self.class_name)
            return SpecFewShotPrompt(self.raw_class, self.class_name)

    def create_model_executor(self):
        if self.prompt_type in ["spec", "spec-only", "spec-fs", "spec-only-fs"]:
            return OnlySpecExecutor(self.dual_prompt)
        return DualModelExecutor(self.dual_prompt)