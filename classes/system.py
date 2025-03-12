from classes.factories.system_abstract_factory import SystemAbstractFactory
from classes.input_parser import InputParser
from classes.model import Model
from classes.factories.model_path_factory import ModelPathFactory
from classes.output_manager.file_output_manager import FileOutputManager
from classes.repok_parser import RepOKParser

class System:
    def __init__(self):
        self.parser = InputParser()
        self.parser.parse()

        self.temperature = 0.1
        self.max_tokens = 4000
        self.n_ctx = 8192
        self.model_name = self.parser.model_name
        self.prompt_type = self.parser.prompt_type
        self.raw_class = self.parser.raw_class
        self.class_name = self.parser.class_name

        self.model_path_factory = ModelPathFactory(self.model_name)
        self.model_path = self.model_path_factory.create()
        self.system_abstract_factory = SystemAbstractFactory(self.prompt_type, self.raw_class, self.class_name)
        self.prompt_type_factory = self.system_abstract_factory.create() 
        self.output_manager = self.prompt_type_factory.create_output_manager()
        self.prompt = self.prompt_type_factory.create_prompt()
        self.repOk_parser = RepOKParser()
        self.model_executor = self.prompt_type_factory.create_model_executor()

        self.model = Model(
            self.model_path, 
            self.temperature, 
            self.max_tokens, 
            self.n_ctx, 
            self.prompt
        )

    def execute(self):
        self.output_manager.clean_output_folder()
        completions = self.model_executor.execute(self.model)
        self.repOk_parser.set_repOK_completion(completions)
        repOk_classes = self.repOk_parser.parse()
        for repOk_class, file_name in repOk_classes:
            self.output_manager.set_output_file_name(file_name)
            self.output_manager.write(repOk_class)
