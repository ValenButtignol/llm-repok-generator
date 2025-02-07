from classes.model_executor.model_executor_interface import ModelExecutorInterface
from classes.output_manager.output_manager_interface import OutputManagerInterface
from classes.prompt.json_prompt import JsonPrompt
from classes.repok_parser.repok_parser_interface import RepOkParserInterface

class PromptTypeFactoryInterface:

    def create_output_manager(self) -> OutputManagerInterface:
        raise NotImplementedError 

    def create_prompt(self) -> JsonPrompt:
        raise NotImplementedError 

    def create_repok_parser(self) -> RepOkParserInterface:
        raise NotImplementedError 
    
    def create_model_executor(self) -> ModelExecutorInterface:
        raise NotImplementedError