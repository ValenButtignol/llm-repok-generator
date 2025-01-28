from classes.model_executor.dual_partsofclass_model_executor import DualPartsOfClassModelExecutor
from classes.model_executor.dual_wholeclass_model_executor import DualWholeClassModelExecutor
from classes.model_executor.simple_model_executor import SimpleModelExecutor

class ModelExecutorFactory:
    
    def create(self, prompt_type):
        if prompt_type == "global":
            return SimpleModelExecutor()
        elif prompt_type == "fs-w":
            return SimpleModelExecutor()
        elif prompt_type == "fs-p":
            return SimpleModelExecutor()
        elif prompt_type == "dual-w":
            return DualWholeClassModelExecutor()
        elif prompt_type == "dual-p":
            return DualPartsOfClassModelExecutor()
    
        else:
            raise Exception("Invalid prompt type: " + prompt_type + "\n")