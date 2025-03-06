from classes.string_constants import OUTPUT_FOLDER

class ModelExecutorInterface:
    DIRECTORY_CLASS=OUTPUT_FOLDER

    def execute(self, model):
        raise NotImplementedError
    
    def write_completion(self, completion):
        with open(self.DIRECTORY_CLASS + "completions.txt", "a") as output_file:

            output_file.write("--------------------------------------------------------\n")
            output_file.write("\n")
            output_file.write(completion)
            output_file.write("\n")
        
        output_file.close()