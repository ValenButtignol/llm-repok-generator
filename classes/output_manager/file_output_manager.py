from classes.output_manager.output_manager_interface import OutputManagerInterface
from classes.string_constants import OUTPUT_FOLDER

class FileOutputManager(OutputManagerInterface):
    def __init__(self):
        pass

    def set_output_file_name(self, output_file_name):
        self.output_file_name = OUTPUT_FOLDER + output_file_name

    def write(self, text):
        with open(self.output_file_name, 'w') as output_file:
            output_file.write(text)
        output_file.close()