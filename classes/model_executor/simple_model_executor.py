from classes.model_executor.model_executor_interface import ModelExecutorInterface

class SimpleModelExecutor(ModelExecutorInterface):

    def __init__(self):
        super().__init__()


    def execute(self, model):
        completion = model.create_chat_completion()
        self.write_completion(completion)
        return [completion]