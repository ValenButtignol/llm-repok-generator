from classes.output_manager.output_manager_interface import OutputManagerInterface
from classes.string_constants import OUTPUT_FOLDER

class FileOutputManager(OutputManagerInterface):
    def __init__(self, output_file_path):
        self.output_file_path = OUTPUT_FOLDER + output_file_path

    def write(self, text):
        with open(self.output_file_path, 'w') as output_file:
            output_file.write(text)
        output_file.close()