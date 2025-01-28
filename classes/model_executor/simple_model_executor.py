from classes.model_executor.model_executor_interface import ModelExecutorInterface

class SimpleModelExecutor(ModelExecutorInterface):

    def execute(self, model):
        return model.create_chat_completion()