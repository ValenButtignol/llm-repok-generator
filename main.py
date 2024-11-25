import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from classes.input_parser import InputParser
from classes.model import Model

def main():
    parser = InputParser()
    parser.parse()
    model = Model(parser.model_path, parser.temperature, parser.max_tokens, parser.n_ctx, parser.prompt)
    completion = model.create_chat_completion() #The completion isn't written to a file yet because the model has to register the execution time of the prompt.
    parser.output_manager.write(repr(model))
    parser.output_manager.write(completion)
    parser.prompt.add_role_message("assistant", completion)
    parser.prompt.add_role_message("user", "3+2=?")
    print(model.prompt.get_text())
    completion = model.create_chat_completion() #The completion isn't written to a file yet because the model has to register the execution time of the prompt.
    parser.output_manager.write(completion)

#python3 main.py -mn "llama3-8b" -tmp 0.2 -mtk 1500 -nctx 1024 -pc "default_prompts/test_generation_prompt.txt" -pt "file" -ot "file" -oc "output.txt"
if __name__ == "__main__":
    main()
    
