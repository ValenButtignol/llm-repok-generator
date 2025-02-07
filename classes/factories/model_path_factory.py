from classes.string_constants import MODELS_FOLDER, LLAMA_NAME, DISTILL_LLAMA_NAME, QWEN_NAME, DISTILL_QWEN_7B_NAME, DISTILL_QWEN_14B_NAME, LLAMA, DISTILL_LLAMA, QWEN, DISTILL_QWEN_7B, DISTILL_QWEN_14B

class ModelPathFactory:
    def __init__(self, model_name):
        self.model_name = model_name
        pass

    def create(self):
        if self.model_name == LLAMA:
            return MODELS_FOLDER + LLAMA_NAME 
        elif self.model_name == DISTILL_LLAMA:
            return MODELS_FOLDER + DISTILL_LLAMA_NAME
        elif self.model_name == QWEN:
            return MODELS_FOLDER + QWEN_NAME 
        elif self.model_name == DISTILL_QWEN_7B:
            return MODELS_FOLDER + DISTILL_QWEN_7B_NAME
        elif self.model_name == DISTILL_QWEN_14B:
            return MODELS_FOLDER + DISTILL_QWEN_14B_NAME

        else:
            raise Exception("Invalid model name: " + self.model_name + "\n")