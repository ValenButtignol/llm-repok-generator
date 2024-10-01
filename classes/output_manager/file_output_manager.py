from classes.output_manager.output_manager_interface import OutputManagerInterface

class FileOutputManager(OutputManagerInterface):
    def __init__(self, output_file_path):
        output_folder = "output/"
        self.output_file_path = output_folder + output_file_path

    def write(self, text):
        with open(self.output_file_path, 'a') as output_file:
            output_file.write(text)
        output_file.close()