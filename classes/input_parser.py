from argparse import ArgumentParser
from classes.model_path_factory import ModelPathFactory
from classes.prompt.prompt_factory import PromptFactory

class InputParser:
    def __init__(self):
        self.parser = ArgumentParser()
        self.parser.add_argument("-mn", "--model_name", dest="model_name", help="check 'models' folder")
        self.parser.add_argument("-tmp", "--temperature", dest="temperature", required=False, default=0.1)
        self.parser.add_argument("-mtk", "--max_tokens", dest="max_tokens", required=False, default=1000)
        self.parser.add_argument("-nctx", "--n_ctx", dest="n_ctx", required=False, default=2048)    
        self.parser.add_argument("-pc", "--prompt_container", dest="prompt_container", help="file or plain text containing the prompt")
        self.parser.add_argument("-pt", "--prompt_type", dest="prompt_type", help="format of the prompt")
    
    def parse(self):
        args = self.parser.parse_args()
        self.temperature = args.temperature
        self.max_tokens = args.max_tokens
        self.n_ctx = args.n_ctx
        model_path_factory = ModelPathFactory()
        self.model_path = model_path_factory.create(args.model_name)
        prompt_factory = PromptFactory()
        self.prompt = prompt_factory.create(args.prompt_type, args.prompt_container)
        
        
    
