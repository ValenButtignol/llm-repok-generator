from classes.output_manager.console_output_manager import ConsoleOutputManager
from classes.output_manager.file_output_manager import FileOutputManager
from string_constants import GLOBAL_PROMPT_TYPE, FEWSHOT_WHOLECLASS_PROMPT_TYPE, FEWSHOT_PARTSOFCLASS_PROMPT_TYPE, DUAL_WHOLECLASS_PROMPT_TYPE, DUAL_PARTSOFCLASS_PROMPT_TYPE, REPOK_CLASS_FILENAME, PROPERTIES_CLASS_FILENAME

class OutputManagerFactory:
    def create(self, prompt_type):
        if prompt_type == GLOBAL_PROMPT_TYPE:
            return FileOutputManager(REPOK_CLASS_FILENAME)
        elif prompt_type == FEWSHOT_WHOLECLASS_PROMPT_TYPE:
            return FileOutputManager(REPOK_CLASS_FILENAME)
        elif prompt_type == FEWSHOT_PARTSOFCLASS_PROMPT_TYPE:
            return FileOutputManager(REPOK_CLASS_FILENAME)
        elif prompt_type == DUAL_WHOLECLASS_PROMPT_TYPE:
            return FileOutputManager(PROPERTIES_CLASS_FILENAME)
        elif prompt_type == DUAL_PARTSOFCLASS_PROMPT_TYPE:
            return FileOutputManager(PROPERTIES_CLASS_FILENAME)
        
        else:
            raise ValueError("Invalid output manager type")