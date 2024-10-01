import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from classes.input_parser import InputParser
from classes.model import Model

def main():
    parser = InputParser()
    parser.parse()
    model = Model(parser.model_path, parser.temperature, parser.max_tokens, parser.n_ctx, parser.prompt)
    completion = model.create_completion() #The completion isn't written to a file yet because the model has to register the execution time of the prompt.
    parser.output_manager.write(repr(model))
    parser.output_manager.write("\n\n")
    parser.output_manager.write(completion)

def exhaustive_main():
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

#python3 main.py -mn "llama3-8b" -tmp 0.2 -mtk 1500 -nctx 1024 -pc "test_generation_prompt.txt" -pt "file" -ot "file" -oc "output.txt"
if __name__ == "__main__":
    exhaustive_main()
    
