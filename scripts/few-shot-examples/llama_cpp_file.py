from llama_cpp import Llama
from argparse import ArgumentParser

def create_parser():
    parser = ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-f", "--file", dest="filename", help="write report to FILE", metavar="FILE")
    group.add_argument("-p", "--prompt", dest="prompt", help="write a prompt from terminal")
    parser.add_argument("-mdl", "--model", dest="model", help="check 'models' folder")
    args = parser.parse_args()
    return args

def get_prompt(filename, prompt):
    if filename is not None:
        prompt_file = open(filename, "r")
        prompt = prompt_file.read()
    elif prompt is not None:
        return prompt

def get_model_string(model_input):
    if model_input == 'codellama-13b':
        return "codellama-13b.Q8_0.gguf"
    elif model_input == 'llama-2-chat':
        return "llama-2-7b-chat.Q5_K_M.gguf"
    elif model_input == 'codellama-34b':
        return "phind-codellama-34b-v2.Q5_K_M.gguf"
    else:
        raise ValueError("Must choose between 'codellama-13b', 'llama-2-chat' or 'codellama-34b'.")

def create_model(model_string):
    model = Llama(
        model_path=f"../../models/{model_string}",
    )
    return model

def run_model(model, prompt):
    output = model(
        prompt,
        max_tokens=300,
        #stop=["}\n\n"],
        echo=True # Echo the prompt back in the output
    )
    return output['choices'][0]['text']

if __name__ == "__main__":
    args = create_parser()
    prompt = get_prompt(args.filename, args.prompt)
    model_string = get_model_string(args.model)
    model = create_model(model_string)
    output = run_model(model, prompt)
    print("\n")
    print(output)
