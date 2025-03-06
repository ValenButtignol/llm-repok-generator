from classes.model import Model
from classes.model_executor.model_executor_interface import ModelExecutorInterface
from string_constants import PROPERTY_TAG

class DualPropModelExecutor(ModelExecutorInterface):

    def __init__(self):
        self.dual_prompt = None

    def execute(self, model):
        prop_completion = model.create_chat_completion()
        props = self._parse_properties(prop_completion)
        prop_methods = ""
        class_text = model.prompt.class_text

        for prop in props:
            classwithprop = class_text + PROPERTY_TAG + prop + "\n"
            self._instance_dual_prompt(classwithprop)
            model2 = Model(model.model_path, model.temperature, model.max_tokens, model.n_ctx, self.dual_prompt)
            prop_method_completion = model2.create_chat_completion()
            prop_methods += prop_method_completion + "\n"

        return prop_methods

    def _parse_properties(self, props_output:str) -> list[str]:
        lines = []
        for line in props_output.splitlines():
            if line.startswith("-"):
                lines.append(PROPERTY_TAG + line)
        return lines 
    
    def _instance_dual_prompt(self, classwithprop):
        pass