from classes.output_manager.output_manager_interface import OutputManagerInterface

class ConsoleOutputManager(OutputManagerInterface):
    def write(self, text):
        print(text)