from classes.model_executor.model_executor_interface import ModelExecutorInterface

class SimpleModelExecutor(ModelExecutorInterface):
    def __init__(self):
        raise NotImplementedError

    def execute(self, model):
        raise NotImplementedError
    
    def write_output(self, completion):
        raise NotImplementedError