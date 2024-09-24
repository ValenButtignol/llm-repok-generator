class ModelPathFactory:
    def __init__(self):
        pass

    def create(self, model_name):
        folder = "models/"
        if model_name == "codellama2-13b":
            return folder + "codellama-13b.Q8_0.gguf"
        elif model_name == "codellama2-34b":
            return folder + "phind-codellama-34b-v2.Q5_K_M.gguf"
        elif model_name == "llama2chat-7b":
            return folder + "llama-2-7b-chat.Q5_K_M.gguf"
        elif model_name == "llama3-8b":
            return folder + "meta-llama-3-8b-instruct.Q5_K_M.gguf"
        elif model_name == "llama3.1-8b":
            return folder + "meta-llama-3.1-8b-instruct.Q5_K_M.gguf"
        elif model_name == "codellama3-8b":
            return folder + "Code-Llama-3-8B-Q5_K_M.gguf"
        elif model_name == "codestral-22b":
            return folder + ""
        elif model_name == "mistral-7b":
            return folder + ""
        elif model_name == "gemma2-27b":
            return folder + ""
            
        else:
            raise Exception("Invalid model name: " + model_name + "\n")