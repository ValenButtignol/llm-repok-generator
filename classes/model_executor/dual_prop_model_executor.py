from classes.model import Model
from classes.model_executor.model_executor_interface import ModelExecutorInterface

class DualPropModelExecutor(ModelExecutorInterface):

    def __init__(self):
        self.dual_prompt = None

    def execute(self, model):
        prop_completion = model.create_chat_completion()
        props = self._parse_properties(prop_completion)

        prop_methods = ""
        for prop in props:
            classwithprop = model.prompt.classtext + prop
            self._instance_dual_prompt(classwithprop)
            model = Model(model.model_path, model.temperature, model.max_tokens, model.n_ctx, self.dual_prompt)
            prop_method_completion = model.create_chat_completion()
            prop_methods += prop_method_completion + "\n"   #TODO: Test if the string is correctly builded

        return prop_methods

    def _parse_properties(self, props_output:str) -> list[str]:
        lines = []
        for line in props_output.splitlines():
            if "-" in line:
                lines.append("\n[Property]\n" + line)
        return lines 
    
    def _instance_dual_prompt(self, classwithprop):
        pass