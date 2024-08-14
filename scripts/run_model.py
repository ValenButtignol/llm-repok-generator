from llama_cpp import Llama
from argparse import ArgumentParser

def create_parser():
    parser = ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-fp", "--file_prompt", dest="file_prompt", help="write a prompt inside a file located in 'prompts' folder")
    group.add_argument("-tp", "--text_prompt", dest="text_prompt", help="write a prompt from terminal")
    parser.add_argument("-mn", "--model_name", dest="model_name", help="check 'models' folder")
    args = parser.parse_args()
    return args

def get_prompt(file_prompt, text_prompt):
    if file_prompt is not None:
        file = open(f"prompts/default_prompts/{file_prompt}", "r")
        prompt = file.read()
        return prompt
    elif text_prompt is not None:
        return text_prompt

def get_model_path(model_name):
    return f"models/{model_name}"

def create_model(modelpath):
    model = Llama(
        model_path=modelpath,
        n_ctx=2048    
    )
    return model

def run_model(model, prompt):
    output = model(
        prompt,
        max_tokens=1000,
        #stop=["}\n\n"],
        echo=True # Echo the prompt back in the output
    )
    return output['choices'][0]['text']


def execute():
    args = create_parser()
    prompt = get_prompt(args.file_prompt, args.text_prompt)
    model_path = get_model_path(args.model_name)
    print(model_path)
    model = create_model(model_path)
    output = run_model(model, prompt)
    print("\n")
    print(output)

if __name__ == "__main__":
    execute()
