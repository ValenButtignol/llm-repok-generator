from classes.string_constants import OUTPUT_FOLDER

class ModelExecutorInterface:

    def execute(self, model):
        raise NotImplementedError
    
    def write_completion(self, completion):
        with open(OUTPUT_FOLDER + "completions.txt", "a") as output_file:

            output_file.write("\n")
            output_file.write(completion)
            output_file.write("\n")
        
        output_file.close()