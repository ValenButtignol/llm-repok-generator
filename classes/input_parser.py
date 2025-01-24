from argparse import ArgumentParser
from classes.model_path_factory import ModelPathFactory
from classes.prompt.prompt_factory import PromptFactory
from classes.output_manager.output_manager_factory import OutputManagerFactory

class InputParser:
    def __init__(self):
        self.parser = ArgumentParser()
        self.parser.add_argument("-mn", "--model_name", dest="model_name", help="check 'models' folder")
        self.parser.add_argument("-pt", "--prompt_type", dest="prompt_type", help="format of the prompt", required=True)
        self.parser.add_argument("-ct", "--class_text", dest="class_text", help="The plain text class to generate the repOk", required=True)
        self.parser.add_argument("-cn", "--class_name", dest="class_name", help="Name of the class to generate the repOk", required=True)
        self.parser.add_argument("-ot", "--output_type", dest="output_type", help="type of output", required=True)
        self.parser.add_argument("-oc", "--output_container", dest="output_container", help="file or None (terminal) containing the output", required=False, default=None)
    
    def parse(self):
        args = self.parser.parse_args()
        self.prompt_type = args.prompt_type
        model_path_factory = ModelPathFactory()
        output_manager_factory = OutputManagerFactory()
        self.output_manager = output_manager_factory.create(args.output_type, args.output_container)
        self.model_path = model_path_factory.create(args.model_name)
        prompt_factory = PromptFactory()
        self.prompt = prompt_factory.create(args.prompt_type, args.prompt_container, args.class_name)
        
