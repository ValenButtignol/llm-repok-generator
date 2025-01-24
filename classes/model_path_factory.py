class ModelPathFactory:
    def __init__(self):
        pass

    def create(self, model_name):
        folder = "models/"
    
        if model_name == "Llama3.1":
            return folder + "meta-llama-3.1-8b-instruct.Q6_K_L.gguf"
        elif model_name == "Distill-Llama":
            return folder + ""
        elif model_name == "Qwen2.5.1-Coder":
            return folder + ""
        elif model_name == "Distill-Qwen-7b":
            return folder + ""
        elif model_name == "Distill-Qwen-14b":
            return folder + ""

        else:
            raise Exception("Invalid model name: " + model_name + "\n")