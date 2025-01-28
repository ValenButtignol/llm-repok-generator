from classes.model_executor.dual_prop_model_executor import DualPropModelExecutor
from classes.prompt.dual_properties_wholeclass_prompt import DualRepOkFewShotCoTWholeClassPrompt

class DualWholeClassModelExecutor(DualPropModelExecutor):

    def __init__(self):
        super().__init__()
    
    def _instance_dual_prompt(self, classwithprop):
        self.dual_prompt = DualRepOkFewShotCoTWholeClassPrompt(classwithprop)