from classes.input_parser import InputParser
from classes.model import Model
from classes.model_executor.model_executor_factory import ModelExecutorFactory
from classes.model_path_factory import ModelPathFactory
from classes.output_manager.output_manager_factory import OutputManagerFactory
from classes.prompt.prompt_factory import PromptFactory
from classes.repok_parser.repok_parser_factory import RepOkParserFactory

class System:
    def __init__(self):
        self.model_path_factory = ModelPathFactory()
        self.output_manager_factory = OutputManagerFactory()
        self.prompt_factory = PromptFactory()
        self.model_executor_factory = ModelExecutorFactory()
        self.repOk_parser_factory = RepOkParserFactory()
        self.parser = InputParser()
        self.parser.parse()

        self.temperature = 0.1
        self.max_tokens = 2000
        self.n_ctx = 4096
        self.model_name = self.parser.model_name
        self.prompt_type = self.parser.prompt_type
        self.raw_class = self.parser.raw_class
        self.class_name = self.parser.class_name
        self.output_type = self.parser.output_type
        self.output_container = self.parser.output_container

    def initialize(self):
        self.output_manager = self.output_manager_factory.create(self.output_type, self.output_container)
        self.model_path = self.model_path_factory.create(self.model_name)
        self.prompt = self.prompt_factory.create(self.prompt_type, self.raw_class, self.class_name)
        self.model_executor = self.model_executor_factory.create(self.prompt_type)
        self.repOk_parser = self.repOk_parser_factory.create(self.prompt_type)

        self.model = Model(
            self.model_path, 
            self.temperature, 
            self.max_tokens, 
            self.n_ctx, 
            self.prompt
        )

    def execute(self):
        completion = self.model_executor.execute(self.model)
        self.repOk_parser.set_repOk_completion(completion)
        repOk_class = self.repOk_parser.parse()
        self.output_manager.write(repOk_class)
