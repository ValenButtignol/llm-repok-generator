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


    def basic_prompt(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_1, REPOK_EXAMPLE_1, CLASS_EXAMPLE_2, REPOK_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("### You are an expert software engineer with proficiency in the Java programming language.")
        prompt.add_user_message("### Your task is to write representation invariants for Java classes. Answer by giving the representation invariant as a Java method called `repOK`.\n### Write a representation invariant for the LinkedList class.\n" + CLASS_EXAMPLE_3.replace("[Class]\n","") + "\n### repOK:\n")

        self.prompt = prompt

    def user_hints(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_1, REPOK_EXAMPLE_1, CLASS_EXAMPLE_2, REPOK_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("### You are an expert software engineer with proficiency in the Java programming language.")
        prompt.add_user_message("### Your task is to write representation invariants for Java classes. Answer by giving the representation invariant as a Java method called `repOK`.\n### Take into account the following rules for writing the representation invariant:\n- The representation invariant is a boolean method of the class.\n- The representation invariant must return `true` if the object is valid, and `false` otherwise.\n- Only verify properties in the representation invariant that you are completely sure are valid.\n- Do not provide any explanation.\n### Write a representation invariant for the LinkedList class.\n" + CLASS_EXAMPLE_3.replace("[Class]\n","") + "\n### repOK:\n")

        self.prompt = prompt

    def user_fewshot(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_1, REPOK_EXAMPLE_1, CLASS_EXAMPLE_2, REPOK_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("### You are an expert software engineer with proficiency in the Java programming language.")
        prompt.add_user_message("### Your task is to write representation invariants for Java classes. Answer by giving the representation invariant as a Java method called `repOK`.\n### Write a representation invariant for the MinHeap class.\n" + CLASS_EXAMPLE_1.replace("[Class]\n","") + "\n### repOK:\n" + REPOK_EXAMPLE_1.replace("[repOk]\n", "") + "\n### Write a representation invariant for the BinTree class.\n" + CLASS_EXAMPLE_2.replace("[Class]\n","") + "\n### repOK:\n" + REPOK_EXAMPLE_2.replace("[repOk]\n", "") + "\n### Write a representation invariant for the LinkedList class.\n" + CLASS_EXAMPLE_3.replace("[Class]\n","") + "\n### repOK:\n")

        self.prompt = prompt

    def user_assistant_fewshot(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_1, REPOK_EXAMPLE_1, CLASS_EXAMPLE_2, REPOK_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("### You are an expert software engineer with proficiency in the Java programming language.")
        prompt.add_user_message("### Your task is to write representation invariants for Java classes. Answer by giving the representation invariant as a Java method called `repOK`.\n### Write a representation invariant for the MinHeap class.\n" + CLASS_EXAMPLE_1.replace("[Class]\n","") + "\n### repOK:\n")
        prompt.add_assistant_message(REPOK_EXAMPLE_1.replace("[repOk]\n", ""))
        prompt.add_user_message("\n### Write a representation invariant for the BinTree class.\n" + CLASS_EXAMPLE_2.replace("[Class]\n","") + "\n### repOK:\n") 
        prompt.add_assistant_message(REPOK_EXAMPLE_2.replace("[repOk]\n", "")) 
        prompt.add_user_message("\n### Write a representation invariant for the LinkedList class.\n" + CLASS_EXAMPLE_3.replace("[Class]\n","") + "\n### repOK:\n")

        self.prompt = prompt

    def user_hints_user_fewshot(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_1, REPOK_EXAMPLE_1, CLASS_EXAMPLE_2, REPOK_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("### You are an expert software engineer with proficiency in the Java programming language.")
        prompt.add_user_message("### Your task is to write representation invariants for Java classes. Answer by giving the representation invariant as a Java method called `repOK`.\n### Take into account the following rules for writing the representation invariant:\n- The representation invariant is a boolean method of the class.\n- The representation invariant must return `true` if the object is valid, and `false` otherwise.\n- Only verify properties in the representation invariant that you are completely sure are valid.\n- Do not provide any explanation.\n### Write a representation invariant for the MinHeap class.\n" + CLASS_EXAMPLE_1.replace("[Class]\n","") + "\n### repOK:\n" + REPOK_EXAMPLE_1.replace("[repOk]\n", "") + "\n### Write a representation invariant for the BinTree class.\n" + CLASS_EXAMPLE_2.replace("[Class]\n","") + "\n### repOK:\n" + REPOK_EXAMPLE_2.replace("[repOk]\n", "") + "\n### Write a representation invariant for the LinkedList class.\n" + CLASS_EXAMPLE_3.replace("[Class]\n","") + "\n### repOK:\n")

        self.prompt = prompt
    
    def user_hints_user_assistant_fewshot(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_1, REPOK_EXAMPLE_1, CLASS_EXAMPLE_2, REPOK_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("### You are an expert software engineer with proficiency in the Java programming language.")
        prompt.add_user_message("### Your task is to write representation invariants for Java classes. Answer by giving the representation invariant as a Java method called `repOK`.\n### Take into account the following rules for writing the representation invariant:\n- The representation invariant is a boolean method of the class.\n- The representation invariant must return `true` if the object is valid, and `false` otherwise.\n- Only verify properties in the representation invariant that you are completely sure are valid.\n- Do not provide any explanation.\n### Write a representation invariant for the MinHeap class.\n" + CLASS_EXAMPLE_1.replace("[Class]\n","") + "\n### repOK:\n")
        prompt.add_assistant_message(REPOK_EXAMPLE_1.replace("[repOk]\n", ""))
        prompt.add_user_message("\n### Write a representation invariant for the BinTree class.\n" + CLASS_EXAMPLE_2.replace("[Class]\n","") + "\n### repOK:\n") 
        prompt.add_assistant_message(REPOK_EXAMPLE_2.replace("[repOk]\n", "")) 
        prompt.add_user_message("\n### Write a representation invariant for the LinkedList class.\n" + CLASS_EXAMPLE_3.replace("[Class]\n","") + "\n### repOK:\n")

        self.prompt = prompt

    def basic_system(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_1, REPOK_EXAMPLE_1, CLASS_EXAMPLE_2, REPOK_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("### You are an expert software engineer with proficiency in the Java programming language. Your task is to write representation invariants for Java classes. Answer by giving the representation invariant as a Java method called `repOK`.")
        prompt.add_user_message("### Write a representation invariant for the LinkedList class.\n" + CLASS_EXAMPLE_3.replace("[Class]\n","") + "\n### repOK:\n")

        self.prompt = prompt

    def system_hints(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_1, REPOK_EXAMPLE_1, CLASS_EXAMPLE_2, REPOK_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("### You are an expert software engineer with proficiency in the Java programming language. Your task is to write representation invariants for Java classes. Answer by giving the representation invariant as a Java method called `repOK`.\n### Take into account the following rules for writing the representation invariant:\n- The representation invariant is a boolean method of the class.\n- The representation invariant must return `true` if the object is valid, and `false` otherwise.\n- Only verify properties in the representation invariant that you are completely sure are valid.\n- Do not provide any explanation.\n")
        prompt.add_user_message("### Write a representation invariant for the LinkedList class.\n" + CLASS_EXAMPLE_3.replace("[Class]\n","") + "\n### repOK:\n")

        self.prompt = prompt

    def system_hints_user_fewshot(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_1, REPOK_EXAMPLE_1, CLASS_EXAMPLE_2, REPOK_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("### You are an expert software engineer with proficiency in the Java programming language. Your task is to write representation invariants for Java classes. Answer by giving the representation invariant as a Java method called `repOK`.\n### Take into account the following rules for writing the representation invariant:\n- The representation invariant is a boolean method of the class.\n- The representation invariant must return `true` if the object is valid, and `false` otherwise.\n- Only verify properties in the representation invariant that you are completely sure are valid.\n- Do not provide any explanation.\n")
        prompt.add_user_message("### Write a representation invariant for the MinHeap class.\n" + CLASS_EXAMPLE_1.replace("[Class]\n","") + "\n### repOK:\n" + REPOK_EXAMPLE_1.replace("[repOk]\n", "") + "\n### Write a representation invariant for the BinTree class.\n" + CLASS_EXAMPLE_2.replace("[Class]\n","") + "\n### repOK:\n" + REPOK_EXAMPLE_2.replace("[repOk]\n", "") + "\n### Write a representation invariant for the LinkedList class.\n" + CLASS_EXAMPLE_3.replace("[Class]\n","") + "\n### repOK:\n")

        self.prompt = prompt

    def system_hints_user_assistant_fewshot(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_1, REPOK_EXAMPLE_1, CLASS_EXAMPLE_2, REPOK_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("### You are an expert software engineer with proficiency in the Java programming language. Your task is to write representation invariants for Java classes. Answer by giving the representation invariant as a Java method called `repOK`.\n### Take into account the following rules for writing the representation invariant:\n- The representation invariant is a boolean method of the class.\n- The representation invariant must return `true` if the object is valid, and `false` otherwise.\n- Only verify properties in the representation invariant that you are completely sure are valid.\n- Do not provide any explanation.\n")
        prompt.add_user_message("\n### Write a representation invariant for the MinHeap class.\n" + CLASS_EXAMPLE_1.replace("[Class]\n","") + "\n### repOK:\n") 
        prompt.add_assistant_message(REPOK_EXAMPLE_1.replace("[repOk]\n", ""))
        prompt.add_user_message("\n### Write a representation invariant for the BinTree class.\n" + CLASS_EXAMPLE_2.replace("[Class]\n","") + "\n### repOK:\n") 
        prompt.add_assistant_message(REPOK_EXAMPLE_2.replace("[repOk]\n", "")) 
        prompt.add_user_message("\n### Write a representation invariant for the LinkedList class.\n" + CLASS_EXAMPLE_3.replace("[Class]\n","") + "\n### repOK:\n")

        self.prompt = prompt





    def props_basic_prompt(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_1, TEXT_PROP_LIST_EXAMPLE_1, CLASS_EXAMPLE_2, TEXT_PROP_LIST_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("### You are an expert software engineer with proficiency in the Java programming language.")
        prompt.add_user_message("### Your task is to provide a list of properties of representation invariants for Java classes as plain text. Answer by giving the list of properties with the format \"- Property Name: Short Description.\".\n### Write a list of properties for the LinkedList class.\n" + CLASS_EXAMPLE_3.replace("[Class]\n","") + "\n### Properties:\n")

        self.prompt = prompt

    def props_user_hints(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_1, TEXT_PROP_LIST_EXAMPLE_1, CLASS_EXAMPLE_2, TEXT_PROP_LIST_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("### You are an expert software engineer with proficiency in the Java programming language.")
        prompt.add_user_message("### Your task is to provide a list of properties of representation invariants for Java classes as plain text. Answer by giving the list of properties with the format \"- Property Name: Short Description.\"\n### Take into account the following rules for writing the properties:\n- A representation invariant is a boolean method of the class.\n- The representation invariant must return `true` if the object is valid, and `false` otherwise.\n- Answer by giving only the list of properties.\n- Only list properties that you are completely sure are valid.\n- Do not provide any explanation.\n### Write a list of properties for the LinkedList class.\n" + CLASS_EXAMPLE_3.replace("[Class]\n","") + "\n### Properties:\n")

        self.prompt = prompt

    def props_user_fewshot(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_1, TEXT_PROP_LIST_EXAMPLE_1, CLASS_EXAMPLE_2, TEXT_PROP_LIST_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("### You are an expert software engineer with proficiency in the Java programming language.")
        prompt.add_user_message("### Your task is to provide a list of properties of representation invariants for Java classes as plain text. Answer by giving the list of properties with the format \"- Property Name: Short Description.\"\n### Write a list of properties for the MinHeap class.\n" + CLASS_EXAMPLE_1.replace("[Class]\n","") + "\n### Properties:\n" + TEXT_PROP_LIST_EXAMPLE_1.replace("[Properties]\n", "") + "\n### Write a list of properties for the BinTree class.\n" + CLASS_EXAMPLE_2.replace("[Class]\n","") + "\n### Properties:\n" + TEXT_PROP_LIST_EXAMPLE_2.replace("[Properties]\n", "") + "\n### Write a list of properties for the LinkedList class.\n" + CLASS_EXAMPLE_3.replace("[Class]\n","") + "\n### Properties:\n")

        self.prompt = prompt

    def props_user_assistant_fewshot(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_1, TEXT_PROP_LIST_EXAMPLE_1, CLASS_EXAMPLE_2, TEXT_PROP_LIST_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("### You are an expert software engineer with proficiency in the Java programming language.")
        prompt.add_user_message("### Your task is to provide a list of properties of representation invariants for Java classes as plain text. Answer by giving the list of properties with the format \"- Property Name: Short Description.\"\n### Write a list of properties for the MinHeap class.\n" + CLASS_EXAMPLE_1.replace("[Class]\n","") + "\n### Properties:\n")
        prompt.add_assistant_message(TEXT_PROP_LIST_EXAMPLE_1.replace("[Properties]\n", ""))
        prompt.add_user_message("\n### Write a list of properties for the BinTree class.\n" + CLASS_EXAMPLE_2.replace("[Class]\n","") + "\n### Properties:\n") 
        prompt.add_assistant_message(TEXT_PROP_LIST_EXAMPLE_2.replace("[Properties]\n", "")) 
        prompt.add_user_message("\n### Write a list of properties for the LinkedList class.\n" + CLASS_EXAMPLE_3.replace("[Class]\n","") + "\n### Properties:\n")

        self.prompt = prompt

    def props_user_hints_user_fewshot(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_1, TEXT_PROP_LIST_EXAMPLE_1, CLASS_EXAMPLE_2, TEXT_PROP_LIST_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("### You are an expert software engineer with proficiency in the Java programming language.")
        prompt.add_user_message("### Your task is to provide a list of properties of representation invariants for Java classes as plain text. Answer by giving the list of properties with the format \"- Property Name: Short Description.\"\n### Take into account the following rules for writing the properties:\n- A representation invariant is a boolean method of the class.\n- The representation invariant must return `true` if the object is valid, and `false` otherwise.\n- Answer by giving only the list of properties.\n- Only list properties that you are completely sure are valid.\n- Do not provide any explanation.\n### Write a list of properties for the MinHeap class.\n" + CLASS_EXAMPLE_1.replace("[Class]\n","") + "\n### Properties:\n" + TEXT_PROP_LIST_EXAMPLE_1.replace("[Properties]\n", "") + "\n### Write a list of properties for the BinTree class.\n" + CLASS_EXAMPLE_2.replace("[Class]\n","") + "\n### Properties:\n" + TEXT_PROP_LIST_EXAMPLE_2.replace("[Properties]\n", "") + "\n### Write a list of properties for the LinkedList class.\n" + CLASS_EXAMPLE_3.replace("[Class]\n","") + "\n### Properties:\n")

        self.prompt = prompt
    
    def props_user_hints_user_assistant_fewshot(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_1, TEXT_PROP_LIST_EXAMPLE_1, CLASS_EXAMPLE_2, TEXT_PROP_LIST_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("### You are an expert software engineer with proficiency in the Java programming language.")
        prompt.add_user_message("### Your task is to provide a list of properties of representation invariants for Java classes as plain text. Answer by giving the list of properties with the format \"- Property Name: Short Description.\" \n### Take into account the following rules for writing the properties:\n- A representation invariant is a boolean method of the class.\n- The representation invariant must return `true` if the object is valid, and `false` otherwise.\n- Answer by giving only the list of properties.\n- Only list properties that you are completely sure are valid.\n- Do not provide any explanation.\n### Write a list of properties for the MinHeap class.\n" + CLASS_EXAMPLE_1.replace("[Class]\n","") + "\n### Properties:\n")
        prompt.add_assistant_message(TEXT_PROP_LIST_EXAMPLE_1.replace("[Properties]\n", ""))
        prompt.add_user_message("\n### Write a list of properties for the BinTree class.\n" + CLASS_EXAMPLE_2.replace("[Class]\n","") + "\n### Properties:\n") 
        prompt.add_assistant_message(TEXT_PROP_LIST_EXAMPLE_2.replace("[Properties]\n", "")) 
        prompt.add_user_message("\n### Write a list of properties for the LinkedList class.\n" + CLASS_EXAMPLE_3.replace("[Class]\n","") + "\n### Properties:\n")

        self.prompt = prompt

    def props_basic_system(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_1, TEXT_PROP_LIST_EXAMPLE_1, CLASS_EXAMPLE_2, TEXT_PROP_LIST_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("### You are an expert software engineer with proficiency in the Java programming language. Your task is to provide a list of properties of representation invariants for Java classes as plain text. Answer by giving the list of properties with the format \"- Property Name: Short Description.\".")
        prompt.add_user_message("### Write a list of properties for the LinkedList class.\n" + CLASS_EXAMPLE_3.replace("[Class]\n","") + "\n### Properties:\n")

        self.prompt = prompt

    def props_system_hints(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_1, TEXT_PROP_LIST_EXAMPLE_1, CLASS_EXAMPLE_2, TEXT_PROP_LIST_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("### You are an expert software engineer with proficiency in the Java programming language. Your task is to provide a list of properties of representation invariants for Java classes as plain text. Answer by giving the list of properties with the format \"- Property Name: Short Description.\".\n### Take into account the following rules for writing the properties:\n- A representation invariant is a boolean method of the class.\n- The representation invariant must return `true` if the object is valid, and `false` otherwise.\n- Answer by giving only the list of properties.\n- Only list properties that you are completely sure are valid.\n- Do not provide any explanation.\n")
        prompt.add_user_message("### Write a list of properties for the LinkedList class.\n" + CLASS_EXAMPLE_3.replace("[Class]\n","") + "\n### Properties:\n")

        self.prompt = prompt

    def props_system_hints_user_fewshot(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_1, TEXT_PROP_LIST_EXAMPLE_1, CLASS_EXAMPLE_2, TEXT_PROP_LIST_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("### You are an expert software engineer with proficiency in the Java programming language. Your task is to provide a list of properties of representation invariants for Java classes as plain text. Answer by giving the list of properties with the format \"- Property Name: Short Description.\".\n### Take into account the following rules for writing the properties:\n- A representation invariant is a boolean method of the class.\n- The representation invariant must return `true` if the object is valid, and `false` otherwise.\n- Answer by giving only the list of properties.\n- Only list properties that you are completely sure are valid.\n- Do not provide any explanation.\n")
        prompt.add_user_message("### Write a list of properties for the MinHeap class.\n" + CLASS_EXAMPLE_1.replace("[Class]\n","") + "\n### Properties:\n" + TEXT_PROP_LIST_EXAMPLE_1.replace("[Properties]\n", "") + "\n### Write a list of properties for the BinTree class.\n" + CLASS_EXAMPLE_2.replace("[Class]\n","") + "\n### Properties:\n" + TEXT_PROP_LIST_EXAMPLE_2.replace("[Properties]\n", "") + "\n### Write a list of properties for the LinkedList class.\n" + CLASS_EXAMPLE_3.replace("[Class]\n","") + "\n### Properties:\n")

        self.prompt = prompt

    def props_system_hints_user_assistant_fewshot(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_1, TEXT_PROP_LIST_EXAMPLE_1, CLASS_EXAMPLE_2, TEXT_PROP_LIST_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("### You are an expert software engineer with proficiency in the Java programming language. Your task is to provide a list of properties of representation invariants for Java classes as plain text. Answer by giving the list of properties with the format \"- Property Name: Short Description.\".\n### Take into account the following rules for writing the properties:\n- A representation invariant is a boolean method of the class.\n- The representation invariant must return `true` if the object is valid, and `false` otherwise.\n- Answer by giving only the list of properties.\n- Only list properties that you are completely sure are valid.\n- Do not provide any explanation.\n")
        prompt.add_user_message("\n### Write a list of properties for the MinHeap class.\n" + CLASS_EXAMPLE_1.replace("[Class]\n","") + "\n### Properties:\n") 
        prompt.add_assistant_message(TEXT_PROP_LIST_EXAMPLE_1.replace("[Properties]\n", ""))
        prompt.add_user_message("\n### Write a list of properties for the BinTree class.\n" + CLASS_EXAMPLE_2.replace("[Class]\n","") + "\n### Properties:\n") 
        prompt.add_assistant_message(TEXT_PROP_LIST_EXAMPLE_2.replace("[Properties]\n", "")) 
        prompt.add_user_message("\n### Write a list of properties for the LinkedList class.\n" + CLASS_EXAMPLE_3.replace("[Class]\n","") + "\n### Properties:\n")

        self.prompt = prompt





    def codeprops_basic_prompt(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import TEXT_SINGLE_PROP_EXAMPLE_3, CLASS_EXAMPLE_1, TEXT_PROP_LIST_EXAMPLE_1, CLASS_EXAMPLE_2, TEXT_PROP_LIST_EXAMPLE_2, CLASS_EXAMPLE_3, TEXT_SINGLE_PROP_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("### You are an expert software engineer with proficiency in the Java programming language.")
        prompt.add_user_message("### Your task is to provide the code for a property of the representation invariant for Java classes. Answer by giving the property as a Java method called `property`.\n### Write the property of the representation invariant for the LinkedList class.\n" + CLASS_EXAMPLE_3.replace("[Class]\n","") + "\n### Property:\n" + TEXT_SINGLE_PROP_EXAMPLE_3.replace("[Property]\n", "") + "\n### Code Property:")

        self.prompt = prompt

    def codeprops_user_hints(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import TEXT_SINGLE_PROP_EXAMPLE_3, CLASS_EXAMPLE_1, TEXT_PROP_LIST_EXAMPLE_1, CLASS_EXAMPLE_2, TEXT_PROP_LIST_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("### You are an expert software engineer with proficiency in the Java programming language.")
        prompt.add_user_message("### Your task is to provide the code for a property of the representation invariant for Java classes.Answer by giving the property as a Java method called `property`.\n### Take into account the following rules for writing the property:\n- The property is a boolean method of the class.\n- The property must return `true` if the object satisfies the property, and `false` otherwise.\n- Do not provide any explanation.\n### Write the property of the representation invariant for the LinkedList class.\n" + CLASS_EXAMPLE_3.replace("[Class]\n","") + "\n### Property:\n" + TEXT_SINGLE_PROP_EXAMPLE_3.replace("[Property]\n", "") + "\n### Code Property:")

        self.prompt = prompt

    def codeprops_user_fewshot(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import TEXT_SINGLE_PROP_EXAMPLE_1, CODE_SINGLE_PROP_EXAMPLE_1, TEXT_SINGLE_PROP_EXAMPLE_2, CODE_SINGLE_PROP_EXAMPLE_2, TEXT_SINGLE_PROP_EXAMPLE_3, CLASS_EXAMPLE_1, TEXT_PROP_LIST_EXAMPLE_1, CLASS_EXAMPLE_2, TEXT_PROP_LIST_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("### You are an expert software engineer with proficiency in the Java programming language.")
        prompt.add_user_message("### Your task is to provide the code for a property of the representation invariant for Java classes. Answer by giving the property as a Java method called `property`.\n### Write the property of the representation invariant for the MinHeap class.\n" + CLASS_EXAMPLE_1.replace("[Class]\n","") + "\n### Property:\n" + TEXT_SINGLE_PROP_EXAMPLE_1.replace("[Property]\n", "") + "\n### Code Property:" + CODE_SINGLE_PROP_EXAMPLE_1.replace("[Property]\n","") + "\n### Write the property of the representation invariant for the BinTree class.\n" + CLASS_EXAMPLE_2.replace("[Class]\n","") + "\n### Property:\n" + TEXT_SINGLE_PROP_EXAMPLE_2.replace("[Property]\n", "") + "\n### Code Property:" + CODE_SINGLE_PROP_EXAMPLE_2.replace("[Property]\n","") + "\n### Write the property of the representation invariant for the LinkedList class.\n" + CLASS_EXAMPLE_3.replace("[Class]\n","") + "\n### Property:\n" + TEXT_SINGLE_PROP_EXAMPLE_3.replace("[Property]\n", "") + "\n### Code Property:")

        self.prompt = prompt

    def codeprops_user_assistant_fewshot(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import TEXT_SINGLE_PROP_EXAMPLE_1,TEXT_SINGLE_PROP_EXAMPLE_2,CODE_SINGLE_PROP_EXAMPLE_1,CODE_SINGLE_PROP_EXAMPLE_2,TEXT_SINGLE_PROP_EXAMPLE_3, CLASS_EXAMPLE_1, TEXT_PROP_LIST_EXAMPLE_1, CLASS_EXAMPLE_2, TEXT_PROP_LIST_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("### You are an expert software engineer with proficiency in the Java programming language.")
        prompt.add_user_message("### Your task is to provide the code for a property of the representation invariant for Java classes. Answer by giving the property as a Java method called `property`.\n### Write the property of the representation invariant for the MinHeap class.\n" + CLASS_EXAMPLE_1.replace("[Class]\n","") + "\n### Property:\n" + TEXT_SINGLE_PROP_EXAMPLE_1.replace("[Property]\n", "") + "\n### Code Property:")
        prompt.add_assistant_message(CODE_SINGLE_PROP_EXAMPLE_1.replace("[Property]\n", ""))
        prompt.add_user_message("\n### Write the property of the representation invariant for the BinTree class.\n" + CLASS_EXAMPLE_2.replace("[Class]\n","") + "\n### Property:\n" + TEXT_SINGLE_PROP_EXAMPLE_2.replace("[Property]\n", "") + "\n### Code Property:") 
        prompt.add_assistant_message(CODE_SINGLE_PROP_EXAMPLE_2.replace("[Property]\n", ""))
        prompt.add_user_message("\n### Write the property of the representation invariant for the LinkedList class.\n" + CLASS_EXAMPLE_3.replace("[Class]\n","") + "\n### Property:\n" + TEXT_SINGLE_PROP_EXAMPLE_3.replace("[Property]\n", "") + "\n### Code Property:")

        self.prompt = prompt

    def codeprops_user_hints_user_fewshot(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import TEXT_SINGLE_PROP_EXAMPLE_1,TEXT_SINGLE_PROP_EXAMPLE_2,CODE_SINGLE_PROP_EXAMPLE_1,CODE_SINGLE_PROP_EXAMPLE_2,TEXT_SINGLE_PROP_EXAMPLE_3, CLASS_EXAMPLE_1, TEXT_PROP_LIST_EXAMPLE_1, CLASS_EXAMPLE_2, TEXT_PROP_LIST_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("### You are an expert software engineer with proficiency in the Java programming language.")
        prompt.add_user_message("### Your task is to provide the code for a property of the representation invariant for Java classes. Answer by giving the property as a Java method called `property`.\n### Take into account the following rules for writing the property:\n- The property is a boolean method of the class.\n- The property must return `true` if the object satisfies the property, and `false` otherwise.\n- Do not provide any explanation.\n### Write the property of the representation invariant for the MinHeap class.\n" + CLASS_EXAMPLE_1.replace("[Class]\n","") + "\n### Property:\n" + TEXT_SINGLE_PROP_EXAMPLE_1.replace("[Property]\n", "") + "\n### Code Property:" + CODE_SINGLE_PROP_EXAMPLE_1.replace("[Property]\n","") + "\n### Write the property of the representation invariant for the BinTree class.\n" + CLASS_EXAMPLE_2.replace("[Class]\n","") + "\n### Property:\n" + TEXT_SINGLE_PROP_EXAMPLE_2.replace("[Property]\n", "") + "\n### Code Property:" + CODE_SINGLE_PROP_EXAMPLE_2.replace("[Property]\n","") + "\n### Write the property of the representation invariant for the LinkedList class.\n" + CLASS_EXAMPLE_3.replace("[Class]\n","") + "\n### Property:\n" + TEXT_SINGLE_PROP_EXAMPLE_3.replace("[Property]\n", "") + "\n### Code Property:")

        self.prompt = prompt
    
    def codeprops_user_hints_user_assistant_fewshot(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import TEXT_SINGLE_PROP_EXAMPLE_3, TEXT_SINGLE_PROP_EXAMPLE_1, TEXT_SINGLE_PROP_EXAMPLE_2, CODE_SINGLE_PROP_EXAMPLE_1, CODE_SINGLE_PROP_EXAMPLE_2, CLASS_EXAMPLE_1, TEXT_PROP_LIST_EXAMPLE_1, CLASS_EXAMPLE_2, TEXT_PROP_LIST_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("### You are an expert software engineer with proficiency in the Java programming language.")
        prompt.add_user_message("### Your task is to provide the code for a property of the representation invariant for Java classes. Answer by giving the property as a Java method called `property`.\n### Take into account the following rules for writing the property:\n- The property is a boolean method of the class.\n- The property must return `true` if the object satisfies the property, and `false` otherwise.\n- Do not provide any explanation.\n### Write the property of the representation invariant for the MinHeap class.\n" + CLASS_EXAMPLE_1.replace("[Class]\n","") + "\n### Property:\n" + TEXT_SINGLE_PROP_EXAMPLE_1.replace("[Property]\n", "") + "\n### Code Property:")
        prompt.add_assistant_message(CODE_SINGLE_PROP_EXAMPLE_1.replace("[Property]\n", ""))
        prompt.add_user_message("\n### Write the property of the representation invariant for the BinTree class.\n" + CLASS_EXAMPLE_2.replace("[Class]\n","") + "\n### Property:\n" + TEXT_SINGLE_PROP_EXAMPLE_2.replace("[Property]\n", "") + "\n### Code Property:") 
        prompt.add_assistant_message(CODE_SINGLE_PROP_EXAMPLE_2.replace("[Property]\n", ""))
        prompt.add_user_message("\n### Write the property of the representation invariant for the LinkedList class.\n" + CLASS_EXAMPLE_3.replace("[Class]\n","") + "\n### Property:\n" + TEXT_SINGLE_PROP_EXAMPLE_3.replace("[Property]\n", "") + "\n### Code Property:")

        self.prompt = prompt

    def codeprops_basic_system(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import TEXT_SINGLE_PROP_EXAMPLE_3, CLASS_EXAMPLE_1, TEXT_PROP_LIST_EXAMPLE_1, CLASS_EXAMPLE_2, TEXT_PROP_LIST_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("### You are an expert software engineer with proficiency in the Java programming language. Your task is to provide the code for a property of the representation invariant for Java classes. Answer by giving the property as a Java method called `property`.")
        prompt.add_user_message("### Write the property of the representation invariant for the LinkedList class.\n" + CLASS_EXAMPLE_3.replace("[Class]\n","") + "\n### Property:\n" + TEXT_SINGLE_PROP_EXAMPLE_3.replace("[Property]\n", "") + "\n### Code Property:")

        self.prompt = prompt

    def codeprops_system_hints(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import TEXT_SINGLE_PROP_EXAMPLE_3, CLASS_EXAMPLE_1, TEXT_PROP_LIST_EXAMPLE_1, CLASS_EXAMPLE_2, TEXT_PROP_LIST_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("### You are an expert software engineer with proficiency in the Java programming language. Your task is to provide the code for a property of the representation invariant for Java classes. Answer by giving the property as a Java method called `property`.\n### Take into account the following rules for writing the property:\n- The property is a boolean method of the class.\n- The property must return `true` if the object satisfies the property, and `false` otherwise.\n- Do not provide any explanation.\n")
        prompt.add_user_message("### Write the property of the representation invariant for the LinkedList class.\n" + CLASS_EXAMPLE_3.replace("[Class]\n","") + "\n### Property:\n" + TEXT_SINGLE_PROP_EXAMPLE_3.replace("[Property]\n", "") + "\n### Code Property:")

        self.prompt = prompt

    def codeprops_system_hints_user_fewshot(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import TEXT_SINGLE_PROP_EXAMPLE_3, CLASS_EXAMPLE_1, TEXT_PROP_LIST_EXAMPLE_1, CLASS_EXAMPLE_2, TEXT_PROP_LIST_EXAMPLE_2, CLASS_EXAMPLE_3, TEXT_SINGLE_PROP_EXAMPLE_1, TEXT_SINGLE_PROP_EXAMPLE_2, CODE_SINGLE_PROP_EXAMPLE_1, CODE_SINGLE_PROP_EXAMPLE_2
        prompt = JsonPrompt()

        prompt.add_system_message("### You are an expert software engineer with proficiency in the Java programming language. Your task is to provide the code for a property of the representation invariant for Java classes. Answer by giving the property as a Java method called `property`.\n### Take into account the following rules for writing the property:\n- The property is a boolean method of the class.\n- The property must return `true` if the object satisfies the property, and `false` otherwise.\n- Do not provide any explanation.\n")
        prompt.add_user_message("### Write the property of the representation invariant for the MinHeap class.\n" + CLASS_EXAMPLE_1.replace("[Class]\n","") + "\n### Property:\n" + TEXT_SINGLE_PROP_EXAMPLE_1.replace("[Property]\n", "") + "\n### Code Property:" + CODE_SINGLE_PROP_EXAMPLE_1.replace("[Property]\n","") + "\n### Write the property of the representation invariant for the BinTree class.\n" + CLASS_EXAMPLE_2.replace("[Class]\n","") + "\n### Property:\n" + TEXT_SINGLE_PROP_EXAMPLE_2.replace("[Property]\n", "") + "\n### Code Property:" + CODE_SINGLE_PROP_EXAMPLE_2.replace("[Property]\n","") + "\n### Write the property of the representation invariant for the LinkedList class.\n" + CLASS_EXAMPLE_3.replace("[Class]\n","") + "\n### Property:\n" + TEXT_SINGLE_PROP_EXAMPLE_3.replace("[Property]\n", "") + "\n### Code Property:")

        self.prompt = prompt

    def codeprops_system_hints_user_assistant_fewshot(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import TEXT_SINGLE_PROP_EXAMPLE_1,TEXT_SINGLE_PROP_EXAMPLE_2, CODE_SINGLE_PROP_EXAMPLE_1, CODE_SINGLE_PROP_EXAMPLE_2, TEXT_SINGLE_PROP_EXAMPLE_3, CLASS_EXAMPLE_1, TEXT_PROP_LIST_EXAMPLE_1, CLASS_EXAMPLE_2, TEXT_PROP_LIST_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("### You are an expert software engineer with proficiency in the Java programming language. Your task is to provide the code for a property of the representation invariant for Java classes. Answer by giving the property as a Java method called `property`.\n### Take into account the following rules for writing the property:\n- The property is a boolean method of the class.\n- The property must return `true` if the object satisfies the property, and `false` otherwise.\n- Do not provide any explanation.\n")
        prompt.add_user_message("\n### Write the property of the representation invariant for the MinHeap class.\n" + CLASS_EXAMPLE_1.replace("[Class]\n","") + "\n### Property:\n" + TEXT_SINGLE_PROP_EXAMPLE_1.replace("[Property]\n", "") + "\n### Code Property:") 
        prompt.add_assistant_message(CODE_SINGLE_PROP_EXAMPLE_1.replace("[Property]\n", ""))
        prompt.add_user_message("\n### Write the property of the representation invariant for the BinTree class.\n" + CLASS_EXAMPLE_2.replace("[Class]\n","") + "\n### Property:\n" + TEXT_SINGLE_PROP_EXAMPLE_2.replace("[Property]\n", "") + "\n### Code Property:") 
        prompt.add_assistant_message(CODE_SINGLE_PROP_EXAMPLE_2.replace("[Property]\n", ""))
        prompt.add_user_message("\n### Write the property of the representation invariant for the LinkedList class.\n" + CLASS_EXAMPLE_3.replace("[Class]\n","") + "\n### Property:\n" + TEXT_SINGLE_PROP_EXAMPLE_3.replace("[Property]\n", "") + "\n### Code Property:")

        self.prompt = prompt

