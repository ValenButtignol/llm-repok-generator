from classes.model_executor.dual_prop_model_executor import DualPropModelExecutor
from classes.prompt.dual_properties_partsofclass_prompt import DualRepOkFewShotCoTPartsOfClassPrompt

class DualPartsOfClassModelExecutor(DualPropModelExecutor):

    def __init__(self):
        super().__init__()

    def _instance_dual_prompt(self, classwithprop):
        self.dual_prompt = DualRepOkFewShotCoTPartsOfClassPrompt(classwithprop)