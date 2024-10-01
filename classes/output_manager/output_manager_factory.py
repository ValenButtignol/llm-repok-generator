from classes.output_manager.console_output_manager import ConsoleOutputManager
from classes.output_manager.file_output_manager import FileOutputManager

class OutputManagerFactory:
    def create_output_manager(self, output_manager_type, output_container):
        if output_manager_type == "console":
            return ConsoleOutputManager()
        elif output_manager_type == "file":
            return FileOutputManager(output_container)
        else:
            raise ValueError("Invalid output manager type")