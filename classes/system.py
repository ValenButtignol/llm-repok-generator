from classes.input_parser import InputParser
from classes.model import Model
from classes.prompt.dual_properties_partsofclass_prompt import DualRepOkFewShotCoTPartsOfClassPrompt
from classes.prompt.dual_properties_wholeclass_prompt import DualRepOkFewShotCoTWholeClassPrompt

class System:
    def __init__(self):
        self.parser = InputParser()
        self.model = None
        self.temperature = 0.1
        self.max_tokens = 2000
        self.n_ctx = 4096

    def initialize(self):
        self.parser.parse()
        self.model = Model(
            self.parser.model_path, 
            self.temperature, 
            self.max_tokens, 
            self.n_ctx, 
            self.parser.prompt
        )

    def execute(self):
        completion = self.model.create_chat_completion()
        self._write_output(repr(self.model))
        self._write_output(completion)

        if self.parser.prompt_type in ["dual-w", "dual-p"]:
            self._handle_dual_prompts(completion)
        elif self.parser.prompt_type in ["fs-cot-w", "fs-cot-p"]:
            self._handle_few_shot_cot_prompts(completion)

    def _handle_dual_prompts(self, completion):
        properties = self._catch_properties(completion)
        classwithoutprop = self.parser.prompt.classtext

        for prop in properties:
            classwithprop = classwithoutprop + prop

            if self.parser.prompt_type == "dual-w":
                completion = self._run_model_with_dual_wholeclass(classwithprop)
            elif self.parser.prompt_type == "dual-p":
                completion = self._run_model_with_dual_partsofclass(classwithprop)

            self._write_output(repr(self.model))
            self._write_output(completion)

    def _handle_few_shot_cot_prompts(self, completion):
        self.parser.prompt.add_remaining_prompts(completion)
        completion = self.model.create_chat_completion()
        self._write_output(repr(self.model))
        self._write_output(completion)

    def _run_model_with_dual_wholeclass(self, classwithprop):
        prompt = DualRepOkFewShotCoTWholeClassPrompt(classwithprop)
        model = Model(self.parser.model_path, self.temperature, self.max_tokens, self.n_ctx, prompt)
        return model.create_chat_completion()

    def _run_model_with_dual_partsofclass(self, classwithprop):
        prompt = DualRepOkFewShotCoTPartsOfClassPrompt(classwithprop)
        model = Model(self.parser.model_path, self.temperature, self.max_tokens, self.n_ctx, prompt)
        return model.create_chat_completion()

    def _catch_properties(self, completion):
        lines = []
        for line in completion.splitlines():
            if "-" in line:
                lines.append("\n[Property]\n" + line)
        return lines

    def _write_output(self, data):
        self.parser.output_manager.write(data)
