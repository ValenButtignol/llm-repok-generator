import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from classes.input_parser import InputParser
from classes.model import Model

#python3 main.py -mn "llama2chat-7b" -tmp 0.2 -mtk 1500 -nctx 1024 -pc "test_generation_prompt.txt" -pt "file"
if __name__ == "__main__":
    parser = InputParser()
    parser.parse()
    print(parser.temperature)
    print(parser.max_tokens)
    print(parser.model_path)
    print(parser.prompt.get_text())
    print(parser.n_ctx)
    model = Model(parser.model_path, parser.temperature, parser.max_tokens, parser.n_ctx, parser.prompt)
    parser.output_manager.write(model.create_completion())