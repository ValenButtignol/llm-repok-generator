from classes.factories.system_abstract_factory import SystemAbstractFactory
from classes.input_parser import InputParser
from classes.model import Model
from classes.factories.model_path_factory import ModelPathFactory

class System:
    def __init__(self):
        self.parser = InputParser()
        self.parser.parse()

        self.temperature = 0.1
        self.max_tokens = 2000
        self.n_ctx = 4096
        self.model_name = self.parser.model_name
        self.prompt_type = self.parser.prompt_type
        self.raw_class = self.parser.raw_class
        self.class_name = self.parser.class_name

        self.model_path_factory = ModelPathFactory(self.model_name)
        self.model_path = self.model_path_factory.create()
        self.system_abstract_factory = SystemAbstractFactory(self.prompt_type, self.raw_class, self.class_name)
        self.prompt_type_factory = self.system_abstract_factory.create() 
        self.output_manager = self.prompt_type_factory.create_output_manager()
        self.prompt = self.prompt_type_factory.create_prompt()
        self.repOk_parser = self.prompt_type_factory.create_repok_parser()
        self.model_executor = self.prompt_type_factory.create_model_executor()

        self.basic_prompt()

        self.model = Model(
            self.model_path, 
            self.temperature, 
            self.max_tokens, 
            self.n_ctx, 
            self.prompt
        )

    def execute(self):
#         props = [
# "Consistent size: The size attribute must be equal to the number of nodes in the list.",
# "Non-cyclicity: The list should not contain any cycles, meaning there should be no node that points back to a previous node in the list.",
# "Proper linking: Each node's next pointer should correctly point to the next node in the list, except for the last node, which should have a next pointer set to null.",
# "Head integrity: The head pointer should correctly point to the first node in the list, or be null if the list is empty."

#         ]
        # self.create_props_fewshot_deepseek(props)

        # self.output_manager.clean_output_folder()
        completion = self.model_executor.execute(self.model)
        with open("output/" + self.model_name + ".txt", "a") as f:
            f.write(repr(self.prompt))
            f.write("\n\nTIME\n")
            f.write(str(self.model.time) + "\n")

        # self.repOk_parser.set_repOk_completion(completion)
        # repOk_classes = self.repOk_parser.parse()
        # for repOk_class, file_name in repOk_classes:
        #     self.output_manager.set_output_file_name(file_name)
        #     self.output_manager.write(repOk_class)

