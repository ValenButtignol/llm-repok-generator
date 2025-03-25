from classes.model import Model
from classes.model_executor.model_executor_interface import ModelExecutorInterface
from classes.string_constants import PROPERTY_TAG

class DualModelExecutor(ModelExecutorInterface):

    def __init__(self, dual_prompt):
        super().__init__()
        self.dual_prompt = dual_prompt

    def execute(self, model):
        prop_completion = model.create_chat_completion()
        self.write_completion(prop_completion)
        props = self._parse_properties(prop_completion)
        prop_methods = []

        for prop in props:
            self.dual_prompt.clean_prompt_data()
            self.dual_prompt.add_property_to_class(prop)
            self.dual_prompt.template()
            model2 = Model(model.model_path, model.temperature, model.max_tokens, model.n_ctx, self.dual_prompt)
            prop_method_completion = model2.create_chat_completion()
            self.write_completion(prop_method_completion)
            prop_methods.append(prop_method_completion)

        return prop_methods

    def _parse_properties(self, props_output:str) -> list[str]:
        lines = []
        for line in props_output.splitlines():
            if line.startswith("-"):
                lines.append(line)
        return lines
    