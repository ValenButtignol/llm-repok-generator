class ModelPathFactory:
    def __init__(self):
        pass

    def create(self, model_name):
        folder = "models/"
        if model_name == "codellama2-13b":
            return folder + ""
        elif model_name == "codellama2-34b":
            return folder + ""
        elif model_name == "llama2chat-7b":
            return folder + "llama-2-7b-chat.Q5_K_M.gguf"
        elif model_name == "llama3-8b":
            return folder + ""
        elif model_name == "codellama3-8b":
            return folder + ""
        else:
            raise Exception("Invalid model name: " + model_name + "\n")