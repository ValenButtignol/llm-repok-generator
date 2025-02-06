from argparse import ArgumentParser

class InputParser:
    def __init__(self):
        self.parser = ArgumentParser()
        self.parser.add_argument("-mn", "--model_name", dest="model_name", help="check 'models' folder")
        self.parser.add_argument("-pt", "--prompt_type", dest="prompt_type", help="format of the prompt", required=True)
        self.parser.add_argument("-rc", "--raw_class", dest="raw_class", help="The plain text class to generate the repOk", required=True)
        self.parser.add_argument("-cn", "--class_name", dest="class_name", help="Name of the class to generate the repOk", required=True)
    
    def parse(self):
        args = self.parser.parse_args()
        self.model_name = args.model_name
        self.prompt_type = args.prompt_type
        self.raw_class = args.raw_class
        self.class_name = args.class_name
