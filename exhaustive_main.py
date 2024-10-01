import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from classes.model import Model
from classes.prompt.file_prompt import FilePrompt
from classes.output_manager.file_output_manager import FileOutputManager

def main():
    import os
    model_names = [model for model in os.listdir("models") if model.endswith(".gguf")]
    prompt_paths = [("ollama_simple_prompts/" + prompt_path) for prompt_path in os.listdir("prompts/ollama_simple_prompts")]
    
    for model_name in model_names:
        for prompt_path in prompt_paths:
            file_prompt = FilePrompt(prompt_path)
            print("Model: " + model_name + " Prompt: " + prompt_path)
            model = Model(f"models/{model_name}", 0.2, 300, 2048, file_prompt)
            prompt_filename = prompt_path.split("/")[-1]
            output_manager = FileOutputManager(model_name + "_" + prompt_filename + ".txt")
            completion = model.create_completion() 
            output_manager.write(repr(model))
            output_manager.write("\n\n")
            output_manager.write(completion)
            output_manager.close()

#python3 exhaustive_main.py
if __name__ == "__main__":
    main()