import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from classes.model import Model

def main():
    import os
    models = os.listdir("models")
    models = [model for model in models if model.endswith(".gguf")]
    prompts = os.listdir("prompts/ollama_simple_prompts")
    for model_name in models:
        for prompt_path in prompts:
            prompt_file = open("prompts/ollama_simple_prompts/" + prompt_path, "r")
            prompt = prompt_file.read()
            prompt_file.close()
            print("Model: " + model_name + " Prompt: " + prompt_path)
            model = Model(f"models/{model_name}", 0.2, 300, 2048, prompt)
            output_file = open("output/" + model_name + "_" + prompt_path, "w")
            completion = model.create_completion() 
            output_file.write(repr(model))
            output_file.write("\n\n")
            output_file.write(completion)
            output_file.close()

#python3 exhaustive_main.py
if __name__ == "__main__":
    main()