from classes.model import Model
from classes.model_executor.model_executor_interface import ModelExecutorInterface
from classes.string_constants import PROPERTY_TAG

class OnlySpecExecutor(ModelExecutorInterface):

    def __init__(self, dual_prompt):
        super().__init__()
        self.dual_prompt = dual_prompt

    def execute(self, model):
        spec_completion = model.create_chat_completion()
        self.write_completion(spec_completion)
        self.dual_prompt.clean_prompt_data()
        self.dual_prompt.add_spec(spec_completion)
        self.dual_prompt.template()

        model2 = Model(model.model_path, model.temperature, model.max_tokens, model.n_ctx, self.dual_prompt)
        repok_completion = model2.create_chat_completion()
        self.write_completion(repok_completion)

        return [repok_completion]