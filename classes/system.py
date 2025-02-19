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

        self.create_meta_suggested_prompt()

        self.model = Model(
            self.model_path, 
            self.temperature, 
            self.max_tokens, 
            self.n_ctx, 
            self.prompt
        )

    def execute(self):
        props = [

        ]
        self.create_props_deepseek_format(props)

        # self.output_manager.clean_output_folder()
        # completion = self.model_executor.execute(self.model)
        # print(repr(self.prompt))
        # print("TIME")
        # print(self.model.time)

        # self.repOk_parser.set_repOk_completion(completion)
        # repOk_classes = self.repOk_parser.parse()
        # for repOk_class, file_name in repOk_classes:
        #     self.output_manager.set_output_file_name(file_name)
        #     self.output_manager.write(repOk_class)


    def create_deepseek_suggested_prompt(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_1, REPOK_EXAMPLE_1, CLASS_EXAMPLE_2, REPOK_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("You are a Java code generation assistant. Your task is to write the `repOk` method for Java classes. The `repOk` method checks the representation invariants of the class, ensuring the object is in a valid state.\n\nRules:\n1. Only write the `repOk` method. Do not provide any explanations, comments, or additional code.\n2. The `repOk` method must only check properties that exist in the class. Do not add checks for non-existent properties.\n3. The method must return a `boolean` value (`true` if the object is valid, `false` otherwise).\n4. Use proper Java syntax and follow best practices for writing representation invariants.\n\nYou will be given a Java class as input. Write the `repOk` method for that class.")
        prompt.add_user_message(CLASS_EXAMPLE_1.replace("[Class]", "").replace("```java\n", "").replace("```", ""))
        prompt.add_assistant_message(REPOK_EXAMPLE_1.replace("[repOk]", "").replace("```java\n", "").replace("```", ""))
        prompt.add_user_message(CLASS_EXAMPLE_2.replace("[Class]", "").replace("```java\n", "").replace("```", ""))
        prompt.add_assistant_message(REPOK_EXAMPLE_2.replace("[repOk]", "").replace("```java\n", "").replace("```", ""))
        prompt.add_user_message(CLASS_EXAMPLE_3.replace("[Class]", "").replace("```java\n", "").replace("```", ""))

        self.prompt = prompt

    def create_openai_suggested_prompt(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_1, REPOK_EXAMPLE_1, CLASS_EXAMPLE_2, REPOK_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("You are an expert Java programmer. Your task is to generate the `repOk` method for a given Java class, which checks the representation invariant of the class. The method must:\n- Be consistent with the class definition.\n- Only check properties that are explicitly present in the class.\n- Not include explanations, only output the Java code.\n- Not assume additional properties beyond what is defined.\n- Ensure proper syntax and correctness.\n\nYou will be provided with examples of Java classes and their correct `repOk` methods.")
        prompt.add_user_message(CLASS_EXAMPLE_1.replace("[Class]", "").replace("```java\n", "").replace("```", ""))
        prompt.add_assistant_message(REPOK_EXAMPLE_1.replace("[repOk]", "").replace("```java\n", "").replace("```", ""))
        prompt.add_user_message(CLASS_EXAMPLE_2.replace("[Class]", "").replace("```java\n", "").replace("```", ""))
        prompt.add_assistant_message(REPOK_EXAMPLE_2.replace("[repOk]", "").replace("```java\n", "").replace("```", ""))
        prompt.add_user_message(CLASS_EXAMPLE_3.replace("[Class]", "").replace("```java\n", "").replace("```", ""))
        
        self.prompt = prompt

    def create_meta_suggested_prompt(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_1, REPOK_EXAMPLE_1, CLASS_EXAMPLE_2, REPOK_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("Write a repOk method for the given Java class. Do not provide explanations, only the repOk method code. Ensure the repOk method is consistent with the provided class and only checks properties that exist in the class.")
        prompt.add_user_message(CLASS_EXAMPLE_1.replace("[Class]", "Write a repOk method for the following Java class:"))
        prompt.add_assistant_message(REPOK_EXAMPLE_1.replace("[repOk]", "").replace("```java\n", "").replace("```", ""))
        prompt.add_user_message(CLASS_EXAMPLE_2.replace("[Class]", "Write a repOk method for the following Java class:"))
        prompt.add_assistant_message(REPOK_EXAMPLE_2.replace("[repOk]", "").replace("```java\n", "").replace("```", ""))
        prompt.add_user_message(CLASS_EXAMPLE_3.replace("[Class]", "Write a repOk method for the following Java class:"))
        
        self.prompt = prompt

    def create_user_tips_suggested_prompt(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_1, REPOK_EXAMPLE_1, CLASS_EXAMPLE_2, REPOK_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("You are an expert software engineer with proficiency in the Java programming language, first I'll give you some tips, and I need you to remember the tips, and do not make same mistakes.")
        prompt.add_user_message("Tips 1:\nThe `repOk` method must only check properties that exist in the class. Do not add checks for non-existent properties.")
        prompt.add_assistant_message("Thank you for the tip! I'll keep in mind that I should only check properties that exist in the class.")
        prompt.add_user_message("Tips 2:\nThe method must return a `boolean` value (`true` if the object is valid, `false` otherwise).")
        prompt.add_assistant_message("Thank you for the tip! I'll keep in mind that the method must return a `boolean` value.")
        prompt.add_user_message("Tips 3:\nUse proper Java syntax and follow best practices for writing representation invariants.")
        prompt.add_assistant_message("Thank you for the tip! I'll keep in mind that I should use proper Java syntax and follow best practices.")
        prompt.add_user_message("Tips 4:\nDo not provide explanations, only the repOk method code.")
        prompt.add_assistant_message("Thank you for the tip! I'll keep in mind that I should not provide explanations, only the repOk method code.")
        
        prompt.add_user_message(CLASS_EXAMPLE_1.replace("[Class]", "Write a repOk method for the following Java class:"))
        prompt.add_assistant_message(REPOK_EXAMPLE_1.replace("[repOk]", "").replace("```java\n", "").replace("```", ""))
        prompt.add_user_message(CLASS_EXAMPLE_2.replace("[Class]", "Write a repOk method for the following Java class:"))
        prompt.add_assistant_message(REPOK_EXAMPLE_2.replace("[repOk]", "").replace("```java\n", "").replace("```", ""))
        prompt.add_user_message(CLASS_EXAMPLE_3.replace("[Class]", "Write a repOk method for the following Java class:"))
        
        self.prompt = prompt

    def create_user_tips_openai_format_prompt(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_1, REPOK_EXAMPLE_1, CLASS_EXAMPLE_2, REPOK_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()
        
        prompt.add_system_message("You are an expert software engineer with proficiency in the Java programming language, first I'll give you some tips, and I need you to remember the tips, and do not make same mistakes.")
        prompt.add_user_message("### The `repOk` method must only check properties that exist in the class. Do not add checks for non-existent properties.")
        prompt.add_assistant_message("Thank you for the tip! I'll keep in mind that I should only check properties that exist in the class.")
        prompt.add_user_message("### The method must return a `boolean` value (`true` if the object is valid, `false` otherwise).")
        prompt.add_assistant_message("Thank you for the tip! I'll keep in mind that the method must return a `boolean` value.")
        prompt.add_user_message("### Use proper Java syntax and follow best practices for writing representation invariants.")
        prompt.add_assistant_message("Thank you for the tip! I'll keep in mind that I should use proper Java syntax and follow best practices.")
        prompt.add_user_message("### Do not provide explanations, only the repOk method code.")
        prompt.add_assistant_message("Thank you for the tip! I'll keep in mind that I should not provide explanations, only the repOk method code.")
        
        prompt.add_user_message(CLASS_EXAMPLE_1.replace("[Class]", "### Write a repOk method for the following Java class:").replace("```java\n", "").replace("```", ""))
        prompt.add_assistant_message(REPOK_EXAMPLE_1.replace("[repOk]", "").replace("```java\n", "").replace("```", ""))
        prompt.add_user_message(CLASS_EXAMPLE_2.replace("[Class]", "### Write a repOk method for the following Java class:").replace("```java\n", "").replace("```", ""))
        prompt.add_assistant_message(REPOK_EXAMPLE_2.replace("[repOk]", "").replace("```java\n", "").replace("```", ""))
        prompt.add_user_message(CLASS_EXAMPLE_3.replace("[Class]", "### Write a repOk method for the following Java class:").replace("```java\n", "").replace("```", ""))

        self.prompt = prompt
    
    def create_user_zeroshot_tips_suggested_prompt(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_1, REPOK_EXAMPLE_1, CLASS_EXAMPLE_2, REPOK_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("You are an expert software engineer with proficiency in the Java programming language, first I'll give you some tips, and I need you to remember the tips, and do not make same mistakes.")
        prompt.add_user_message("Tips 1:\nThe `repOk` method must only check properties that exist in the class. Do not add checks for non-existent properties.")
        prompt.add_assistant_message("Thank you for the tip! I'll keep in mind that I should only check properties that exist in the class.")
        prompt.add_user_message("Tips 2:\nThe method must return a `boolean` value (`true` if the object is valid, `false` otherwise).")
        prompt.add_assistant_message("Thank you for the tip! I'll keep in mind that the method must return a `boolean` value.")
        prompt.add_user_message("Tips 3:\nUse proper Java syntax and follow best practices for writing representation invariants.")
        prompt.add_assistant_message("Thank you for the tip! I'll keep in mind that I should use proper Java syntax and follow best practices.")
        prompt.add_user_message("Tips 4:\nDo not provide explanations, only the repOk method code.")
        prompt.add_assistant_message("Thank you for the tip! I'll keep in mind that I should not provide explanations, only the repOk method code.")
        
        prompt.add_user_message(CLASS_EXAMPLE_3.replace("[Class]", "Write a repOk method for the following Java class:"))
        
        self.prompt = prompt
    
    
    def create_user_oneshot_tips_suggested_prompt(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_1, REPOK_EXAMPLE_1, CLASS_EXAMPLE_2, REPOK_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("You are an expert software engineer with proficiency in the Java programming language, first I'll give you some tips, and I need you to remember the tips, and do not make same mistakes.")
        prompt.add_user_message("Tips 1:\nThe `repOk` method must only check properties that exist in the class. Do not add checks for non-existent properties.")
        prompt.add_assistant_message("Thank you for the tip! I'll keep in mind that I should only check properties that exist in the class.")
        prompt.add_user_message("Tips 2:\nThe method must return a `boolean` value (`true` if the object is valid, `false` otherwise).")
        prompt.add_assistant_message("Thank you for the tip! I'll keep in mind that the method must return a `boolean` value.")
        prompt.add_user_message("Tips 3:\nUse proper Java syntax and follow best practices for writing representation invariants.")
        prompt.add_assistant_message("Thank you for the tip! I'll keep in mind that I should use proper Java syntax and follow best practices.")
        prompt.add_user_message("Tips 4:\nDo not provide explanations, only the repOk method code.")
        prompt.add_assistant_message("Thank you for the tip! I'll keep in mind that I should not provide explanations, only the repOk method code.")
        
        prompt.add_user_message(CLASS_EXAMPLE_1.replace("[Class]", "Write a repOk method for the following Java class:"))
        prompt.add_assistant_message(REPOK_EXAMPLE_1.replace("[repOk]", "").replace("```java\n", "").replace("```", ""))
        prompt.add_user_message(CLASS_EXAMPLE_3.replace("[Class]", "Write a repOk method for the following Java class:"))
        
        self.prompt = prompt


    def create_QA_openai_format_prompt(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_1, REPOK_EXAMPLE_1, CLASS_EXAMPLE_2, REPOK_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("You are an expert software engineer with proficiency in the Java programming language")
        prompt.add_user_message(CLASS_EXAMPLE_1.replace("[Class]", "### Here is a Java class:\n").replace("```java\n", "").replace("```", "") + "\n### What is the `repOk` method for this class? Do not add checks for non-existent properties, and do not provide explanations, only the repOk method code.")
        prompt.add_assistant_message(REPOK_EXAMPLE_1.replace("[repOk]", "").replace("```java\n", "").replace("```", ""))
        prompt.add_user_message(CLASS_EXAMPLE_2.replace("[Class]", "### Here is a Java class:\n").replace("```java\n", "").replace("```", "") + "\n### What is the `repOk` method for this class? Do not add checks for non-existent properties, and do not provide explanations, only the repOk method code.")
        prompt.add_assistant_message(REPOK_EXAMPLE_2.replace("[repOk]", "").replace("```java\n", "").replace("```", ""))
        prompt.add_user_message(CLASS_EXAMPLE_3.replace("[Class]", "### Here is a Java class:\n").replace("```java\n", "").replace("```", "") + "\n### What is the `repOk` method for this class? Do not add checks for non-existent properties, and do not provide explanations, only the repOk method code.")

        self.prompt = prompt

    def create_QA_code_format_prompt(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_1, REPOK_EXAMPLE_1, CLASS_EXAMPLE_2, REPOK_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("You are an expert software engineer with proficiency in the Java programming language")
        prompt.add_user_message(CLASS_EXAMPLE_1.replace("[Class]", "/* Here is a Java class: */\n").replace("```java\n", "").replace("```", "") + "\n/* What is the `repOk` method for this class? Do not add checks for non-existent properties, and do not provide explanations, only the repOk method code. */")
        prompt.add_assistant_message(REPOK_EXAMPLE_1.replace("[repOk]", "").replace("```java\n", "").replace("```", ""))
        prompt.add_user_message(CLASS_EXAMPLE_2.replace("[Class]", "/* Here is a Java class: */\n").replace("```java\n", "").replace("```", "") + "\n/* What is the `repOk` method for this class? Do not add checks for non-existent properties, and do not provide explanations, only the repOk method code. */")
        prompt.add_assistant_message(REPOK_EXAMPLE_2.replace("[repOk]", "").replace("```java\n", "").replace("```", ""))
        prompt.add_user_message(CLASS_EXAMPLE_3.replace("[Class]", "/* Here is a Java class: */\n").replace("```java\n", "").replace("```", "") + "\n/* What is the `repOk` method for this class? Do not add checks for non-existent properties, and do not provide explanations, only the repOk method code. */")

        self.prompt = prompt

    def create_fewshot_openai_format(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_1, REPOK_EXAMPLE_1, CLASS_EXAMPLE_2, REPOK_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("You are an expert software engineer with proficiency in the Java programming language")
        prompt.add_user_message(CLASS_EXAMPLE_1.replace("[Class]", "### Generate a representation invariant for this class. Ensure that the repOk you generate returns true when run on valid instances of the class and false otherwise. Do not provide any explanation.\n### Class:\n").replace("```java\n", "").replace("```", ""))
        prompt.add_assistant_message(REPOK_EXAMPLE_1.replace("[repOk]", "").replace("```java\n", "").replace("```", ""))
        prompt.add_user_message(CLASS_EXAMPLE_2.replace("[Class]", "### Generate a representation invariant for this class. Ensure that the repOk you generate returns true when run on valid instances of the class and false otherwise. Do not provide any explanation.\n### Class:\n").replace("```java\n", "").replace("```", ""))
        prompt.add_assistant_message(REPOK_EXAMPLE_2.replace("[repOk]", "").replace("```java\n", "").replace("```", ""))
        prompt.add_user_message(CLASS_EXAMPLE_3.replace("[Class]", "### Generate a representation invariant for this class. Ensure that the repOk you generate returns true when run on valid instances of the class and false otherwise. Do not provide any explanation.\n### Class:\n").replace("```java\n", "").replace("```", ""))

        self.prompt = prompt

    def create_fewshot_code_format(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_1, REPOK_EXAMPLE_1, CLASS_EXAMPLE_2, REPOK_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("You are an expert software engineer with proficiency in the Java programming language")
        prompt.add_user_message(CLASS_EXAMPLE_1.replace("[Class]", "/* Generate a representation invariant for this class. Ensure that the repOk you generate returns true when run on valid instances of the class and false otherwise. Do not provide any explanation.*/\n/* Class: */\n").replace("```java\n", "").replace("```", ""))
        prompt.add_assistant_message(REPOK_EXAMPLE_1.replace("[repOk]", "").replace("```java\n", "").replace("```", ""))
        prompt.add_user_message(CLASS_EXAMPLE_2.replace("[Class]", "/* Generate a representation invariant for this class. Ensure that the repOk you generate returns true when run on valid instances of the class and false otherwise. Do not provide any explanation.*/\n/* Class: */\n").replace("```java\n", "").replace("```", ""))
        prompt.add_assistant_message(REPOK_EXAMPLE_2.replace("[repOk]", "").replace("```java\n", "").replace("```", ""))
        prompt.add_user_message(CLASS_EXAMPLE_3.replace("[Class]", "/* Generate a representation invariant for this class. Ensure that the repOk you generate returns true when run on valid instances of the class and false otherwise. Do not provide any explanation.*/\n/* Class: */\n").replace("```java\n", "").replace("```", ""))

        self.prompt = prompt

    def create_props_deepseek_format(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_1, TEXT_PROP_LIST_EXAMPLE_1, CLASS_EXAMPLE_2, TEXT_PROP_LIST_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("You are a Java code analysis tool. Your task is to analyze a given Java class and generate a list of properties that must hold true for valid instances of the class. These properties should be derived from the representation invariant of the class. Ensure that the properties are minimal, meaning they should not include any unnecessary or redundant conditions. Each property should be listed in the following format:\n\n- Property: Short description")
        prompt.add_user_message(CLASS_EXAMPLE_1.replace("[Class]", "Here is a Java class:\n\n") + "\n\nPlease generate the properties that must hold true for valid instances of this class.")
        prompt.add_assistant_message(TEXT_PROP_LIST_EXAMPLE_1.replace("[Properties]\n", ""))
        prompt.add_user_message(CLASS_EXAMPLE_2.replace("[Class]", "Here is a Java class:\n\n") + "\n\nPlease generate the properties that must hold true for valid instances of this class.")
        prompt.add_assistant_message(TEXT_PROP_LIST_EXAMPLE_2.replace("[Properties]\n", ""))
        prompt.add_user_message(CLASS_EXAMPLE_3.replace("[Class]", "Here is a Java class:\n\n") + "\n\nPlease generate the properties that must hold true for valid instances of this class.")

        self.prompt = prompt
    
    def create_zeroshot_props_deepseek_format(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_1, TEXT_PROP_LIST_EXAMPLE_1, CLASS_EXAMPLE_2, TEXT_PROP_LIST_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("You are a Java code analysis tool. Your task is to analyze a given Java class and generate a list of properties that must hold true for valid instances of the class. These properties should be derived from the representation invariant of the class. Ensure that the properties are minimal, meaning they should not include any unnecessary or redundant conditions. Each property should be listed in the following format:\n\n- Property: Short description")
        prompt.add_user_message(CLASS_EXAMPLE_3.replace("[Class]", "Here is a Java class:\n\n") + "\n\nPlease generate the properties that must hold true for valid instances of this class.")

        self.prompt = prompt

    def create_props_openai_format(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_1, TEXT_PROP_LIST_EXAMPLE_1, CLASS_EXAMPLE_2, TEXT_PROP_LIST_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("You are an expert Java software engineer. Your task is to analyze Java classes and extract valid representation invariants in a structured list format. \n\nOnly include properties that are always true for valid instances of the class. Do not invent new properties or assume behavior beyond the provided code.")
        prompt.add_user_message(CLASS_EXAMPLE_1.replace("[Class]", "Analyze the following Java class and extract valid representation invariants. Only list properties that are always true for valid instances of the class.\n\n") + "\n\nProvide the representation invariants in the required format.")
        prompt.add_assistant_message(TEXT_PROP_LIST_EXAMPLE_1.replace("[Properties]\n", ""))
        prompt.add_user_message(CLASS_EXAMPLE_2.replace("[Class]", "Analyze the following Java class and extract valid representation invariants. Only list properties that are always true for valid instances of the class.\n\n") + "\n\nProvide the representation invariants in the required format.")
        prompt.add_assistant_message(TEXT_PROP_LIST_EXAMPLE_2.replace("[Properties]\n", ""))
        prompt.add_user_message(CLASS_EXAMPLE_3.replace("[Class]", "Analyze the following Java class and extract valid representation invariants. Only list properties that are always true for valid instances of the class.\n\n") + "\n\nProvide the representation invariants in the required format.")
        
        self.prompt = prompt

    def create_zeroshot_props_openai_format(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_1, TEXT_PROP_LIST_EXAMPLE_1, CLASS_EXAMPLE_2, TEXT_PROP_LIST_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("You are an expert Java software engineer. Your task is to analyze Java classes and extract valid representation invariants in a structured list format. \n\nOnly include properties that are always true for valid instances of the class. Do not invent new properties or assume behavior beyond the provided code.")
        prompt.add_user_message(CLASS_EXAMPLE_3.replace("[Class]", "Analyze the following Java class and extract valid representation invariants. Only list properties that are always true for valid instances of the class.\n\n") + "\n\nProvide the representation invariants in the required format.")
        
        self.prompt = prompt


    def create_props_meta_format(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_3, CLASS_EXAMPLE_1, TEXT_PROP_LIST_EXAMPLE_1, CLASS_EXAMPLE_2, TEXT_PROP_LIST_EXAMPLE_2
        prompt = JsonPrompt()

        prompt.add_system_message("Generate a list of properties that can be verified through the representation invariant of the given Java class. These properties should be true for all valid instances of the class. Minimize the properties to only those that can be directly inferred from the class definition. Use the following format for each property: - Property: Short description")
        prompt.add_user_message(CLASS_EXAMPLE_1.replace("[Class]", "Analyze the following Java class and generate the list of properties:\n") + "\n\nProvide the representation invariants in the required format.")
        prompt.add_assistant_message(TEXT_PROP_LIST_EXAMPLE_1.replace("[Properties]\n", ""))
        prompt.add_user_message(CLASS_EXAMPLE_2.replace("[Class]", "Analyze the following Java class and generate the list of properties:\n") + "\n\nProvide the representation invariants in the required format.")
        prompt.add_assistant_message(TEXT_PROP_LIST_EXAMPLE_2.replace("[Properties]\n", ""))
        prompt.add_user_message(CLASS_EXAMPLE_3.replace("[Class]", "Analyze the following Java class and generate the list of properties:\n") + "\n\nProvide the representation invariants in the required format.")
        
        self.prompt = prompt

    def create_zeroshot_props_meta_format(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("Generate a list of properties that can be verified through the representation invariant of the given Java class. These properties should be true for all valid instances of the class. Minimize the properties to only those that can be directly inferred from the class definition. Use the following format for each property: - Property: Short description")
        prompt.add_user_message(CLASS_EXAMPLE_3.replace("[Class]", "Analyze the following Java class and generate the list of properties:\n") + "\n\nProvide the representation invariants in the required format.")
        
        self.prompt = prompt

    def create_meta_zeroshot_suggested_prompt(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_1, REPOK_EXAMPLE_1, CLASS_EXAMPLE_2, REPOK_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("Write a repOk method for the given Java class. Do not provide explanations, only the repOk method code. Ensure the repOk method is consistent with the provided class and only checks properties that exist in the class.")
        prompt.add_user_message(CLASS_EXAMPLE_3.replace("[Class]", "Write a repOk method for the following Java class:"))
        
        self.prompt = prompt

    def create_QA_zeroshot_code_format_prompt(self):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_1, REPOK_EXAMPLE_1, CLASS_EXAMPLE_2, REPOK_EXAMPLE_2, CLASS_EXAMPLE_3
        prompt = JsonPrompt()

        prompt.add_system_message("You are an expert software engineer with proficiency in the Java programming language")
        prompt.add_user_message(CLASS_EXAMPLE_3.replace("[Class]", "/* Here is a Java class: */\n").replace("```java\n", "").replace("```", "") + "\n/* What is the `repOk` method for this class? Do not add checks for non-existent properties, and do not provide explanations, only the repOk method code. */")

        self.prompt = prompt

    def create_props_fewshot_deepseek(self, props):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_1, CODE_SINGLE_PROP_EXAMPLE_1, TEXT_SINGLE_PROP_EXAMPLE_1, CLASS_EXAMPLE_2, CODE_SINGLE_PROP_EXAMPLE_2, TEXT_SINGLE_PROP_EXAMPLE_2, CLASS_EXAMPLE_3

        props_and_time = ""

        for prop in props:
            prompt = JsonPrompt()
            prompt.add_system_message("You are a Java programming expert. Your task is to write a `property` method for a given Java class. The method must check whether a specific property (provided as input) is part of the class's representation invariant. Follow these rules:\n1. Write only the `property` method. Do not include any explanations or additional code.\n2. Use the best Java programming practices, including proper null checks, validation, and efficient logic.\n3. The method must be named `property` and return a `boolean`.\n4. Assume the class and its fields are already defined. Do not redefine the class or its fields.\n5. Focus only on the property provided in the input.")
            prompt.add_user_message("Here is a Java class:\n" + CLASS_EXAMPLE_1.replace("[Class]", "") + "\nThe property to check is: " + TEXT_SINGLE_PROP_EXAMPLE_1.replace("[Property]\n- ", ""))
            prompt.add_assistant_message(CODE_SINGLE_PROP_EXAMPLE_1.replace("[Property]\n", ""))
            prompt.add_user_message("Here is a Java class:\n" + CLASS_EXAMPLE_2.replace("[Class]", "") + "\nThe property to check is: " + TEXT_SINGLE_PROP_EXAMPLE_2.replace("[Property]\n- ", ""))
            prompt.add_assistant_message(CODE_SINGLE_PROP_EXAMPLE_2.replace("[Property]\n", ""))
            prompt.add_user_message("Here is a Java class:\n" + CLASS_EXAMPLE_3.replace("[Class]", "") + "\nThe property to check is: " + prop)

            model2 = Model(self.model.model_path, self.model.temperature, self.model.max_tokens, self.model.n_ctx, prompt)
            model2.create_chat_completion()

            props_and_time += "\n*****************************************************\n"
            props_and_time += (repr(self.prompt))
            props_and_time += ("\nTIME:" + model2.time + "\n")
        print(props_and_time)


    def create_props_zeroshot_deepseek(self, props):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_3

        props_and_time = ""

        for prop in props:
            prompt = JsonPrompt()
            prompt.add_system_message("You are a Java programming expert. Your task is to write a `property` method for a given Java class. The method must check whether a specific property (provided as input) is part of the class's representation invariant. Follow these rules:\n1. Write only the `property` method. Do not include any explanations or additional code.\n2. Use the best Java programming practices, including proper null checks, validation, and efficient logic.\n3. The method must be named `property` and return a `boolean`.\n4. Assume the class and its fields are already defined. Do not redefine the class or its fields.\n5. Focus only on the property provided in the input.")
            prompt.add_user_message("Here is a Java class:\n" + CLASS_EXAMPLE_3.replace("[Class]", "") + "\nThe property to check is:" + prop)

            model2 = Model(self.model.model_path, self.model.temperature, self.model.max_tokens, self.model.n_ctx, prompt)
            model2.create_chat_completion()

            props_and_time += "\n*****************************************************\n"
            props_and_time += (repr(self.prompt))
            props_and_time += ("\nTIME:" + model2.time + "\n")
        print(props_and_time)

    def create_props_fewshot_meta(self, props):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_1, CODE_SINGLE_PROP_EXAMPLE_1, TEXT_SINGLE_PROP_EXAMPLE_1, CLASS_EXAMPLE_2, CODE_SINGLE_PROP_EXAMPLE_2, TEXT_SINGLE_PROP_EXAMPLE_2, CLASS_EXAMPLE_3

        props_and_time = ""

        for prop in props:
            prompt = JsonPrompt()
            prompt.add_system_message("Write a Java method named \"property\" that checks if the given property of the class holds true. Use best practices for Java coding. Provide the method in the format of public boolean property() { return /* condition */; }. Do not provide explanations.")
            prompt.add_user_message("Please write the Java method \"property\" for the following class:\n\n" + CLASS_EXAMPLE_1.replace("[Class]\n```java", "").replace("```", "") + "\n\nProperty: " + TEXT_SINGLE_PROP_EXAMPLE_1.replace("[Property]\n- ", ""))
            prompt.add_assistant_message(CODE_SINGLE_PROP_EXAMPLE_1.replace("[Property]\n```java", "").replace("```", ""))
            prompt.add_user_message("Please write the Java method \"property\" for the following class:\n\n" + CLASS_EXAMPLE_2.replace("[Class]\n```java", "").replace("```", "") + "\n\nProperty: " + TEXT_SINGLE_PROP_EXAMPLE_2.replace("[Property]\n- ", ""))
            prompt.add_assistant_message(CODE_SINGLE_PROP_EXAMPLE_2.replace("[Property]\n```java", "").replace("```", ""))
            prompt.add_user_message("Please write the Java method \"property\" for the following class:\n\n" + CLASS_EXAMPLE_3.replace("[Class]\n```java", "").replace("```", "") + "\n\nProperty: " + prop)

            model2 = Model(self.model.model_path, self.model.temperature, self.model.max_tokens, self.model.n_ctx, prompt)
            model2.create_chat_completion()

            props_and_time += "\n*****************************************************\n"
            props_and_time += (repr(self.prompt))
            props_and_time += ("\nTIME:" + model2.time + "\n")
        print(props_and_time)


    def create_props_fewshot_meta_v2(self, props):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_3

        props_and_time = ""

        for prop in props:
            prompt = JsonPrompt()
            prompt.add_system_message("Write a Java method named \"property\" that checks if the given property of the class holds true. Use best practices for Java coding. Provide the method in the format of public boolean property() { return /* condition */; }. Do not provide explanations.")
            prompt.add_user_message("Here are a few examples of Java methods that check properties:\n\npublic boolean property() { return x > 0; }\npublic boolean property() { return list.size() > 0; }\npublic boolean property() { return str != null && !str.isEmpty(); }\n\nPlease write the Java method \"property\" for the following class:\n\nPlease write the Java method \"property\" for the following class:\n\n" + CLASS_EXAMPLE_3.replace("[Class]\n```java", "").replace("```", "") + "\n\nProperty: " + prop)

            model2 = Model(self.model.model_path, self.model.temperature, self.model.max_tokens, self.model.n_ctx, prompt)
            model2.create_chat_completion()

            props_and_time += "\n*****************************************************\n"
            props_and_time += (repr(self.prompt))
            props_and_time += ("\nTIME:" + model2.time + "\n")
        print(props_and_time)

    def create_props_zeroshot_meta(self, props):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_3

        props_and_time = ""

        for prop in props:
            prompt = JsonPrompt()
            prompt.add_system_message("Write a Java method named \"property\" that checks if the given property of the class holds true. Use best practices for Java coding. Provide the method in the format of public boolean property() { return /* condition */; }. Do not provide explanations.")
            prompt.add_user_message("Please write the Java method \"property\" for the following class:\n\n" + CLASS_EXAMPLE_3.replace("[Class]\n```java", "").replace("```", "") + "\n\nProperty: " + prop)

            model2 = Model(self.model.model_path, self.model.temperature, self.model.max_tokens, self.model.n_ctx, prompt)
            model2.create_chat_completion()

            props_and_time += "\n*****************************************************\n"
            props_and_time += (repr(self.prompt))
            props_and_time += ("\nTIME:" + model2.time + "\n")
        print(props_and_time)

    def create_props_fewshot_openai(self, props):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_1, CODE_SINGLE_PROP_EXAMPLE_1, TEXT_SINGLE_PROP_EXAMPLE_1, CLASS_EXAMPLE_2, CODE_SINGLE_PROP_EXAMPLE_2, TEXT_SINGLE_PROP_EXAMPLE_2, CLASS_EXAMPLE_3

        props_and_time = ""

        for prop in props:
            prompt = JsonPrompt()

            prompt.add_system_message("You are a Java expert specializing in formal verification and representation invariants. Your task is to generate a `property` method for the given Java class. This method must implement the given property as a boolean condition.\n\nFollow these guidelines:\n- Implement the method using the best Java programming techniques.\n- Do not provide any explanation, only return the Java method.\n- Format the method consistently based on the given examples.")
            prompt.add_system_message("You are a Java expert specializing in formal verification and representation invariants. Your task is to generate a `property` method for the given Java class. This method must implement the given property as a boolean condition.\n\nFollow these guidelines:\n- Implement the method using the best Java programming techniques.\n- Do not provide any explanation, only return the Java method.\n- Format the method consistently based on the given examples.")
            prompt.add_user_message("Here is the Java class:\n\n" + CLASS_EXAMPLE_1.replace("[Class]\n", "") + "\n\nProperty to verify:\n" + TEXT_SINGLE_PROP_EXAMPLE_1.replace("[Property]\n") + "\n\nGenerate the following boolean method inside the class:\n\n```java\npublic boolean property() { ... }\n```\n\nEnsure the method correctly enforces the given property.")
            prompt.add_assistant_message(CODE_SINGLE_PROP_EXAMPLE_1.replace("[Property]", ""))
            prompt.add_user_message("Here is the Java class:\n\n" + CLASS_EXAMPLE_2.replace("[Class]\n", "") + "\n\nProperty to verify:\n" + TEXT_SINGLE_PROP_EXAMPLE_2.replace("[Property]\n") + "\n\nGenerate the following boolean method inside the class:\n\n```java\npublic boolean property() { ... }\n```\n\nEnsure the method correctly enforces the given property.")
            prompt.add_assistant_message(CODE_SINGLE_PROP_EXAMPLE_1.replace("[Property]", ""))
            prompt.add_user_message("Here is the Java class:\n\n" + CLASS_EXAMPLE_3.replace("[Class]\n", "") + "\n\nProperty to verify:\n" + prop + "\n\nGenerate the following boolean method inside the class:\n\n```java\npublic boolean property() { ... }\n```\n\nEnsure the method correctly enforces the given property.")

            model2 = Model(self.model.model_path, self.model.temperature, self.model.max_tokens, self.model.n_ctx, prompt)
            model2.create_chat_completion()

            props_and_time += "\n*****************************************************\n"
            props_and_time += (repr(self.prompt))
            props_and_time += ("\nTIME:" + model2.time + "\n")
        print(props_and_time)

    def create_props_zeroshot_openai(self, props):
        from classes.prompt.json_prompt import JsonPrompt
        from classes.prompt.templates import CLASS_EXAMPLE_3

        props_and_time = ""

        for prop in props:
            prompt = JsonPrompt()
            prompt.add_system_message("You are a Java expert specializing in formal verification and representation invariants. Your task is to generate a `property` method for the given Java class. This method must implement the given property as a boolean condition.\n\nFollow these guidelines:\n- Implement the method using the best Java programming techniques.\n- Do not provide any explanation, only return the Java method.\n- Format the method consistently based on the given examples.")
            prompt.add_user_message("Here is the Java class:\n\n" + CLASS_EXAMPLE_3.replace("[Class]\n", "") + "\n\nProperty to verify:\n" + prop + "\n\nGenerate the following boolean method inside the class:\n\n```java\npublic boolean property() { ... }\n```\n\nEnsure the method correctly enforces the given property.")

            model2 = Model(self.model.model_path, self.model.temperature, self.model.max_tokens, self.model.n_ctx, prompt)
            model2.create_chat_completion()

            props_and_time += "\n*****************************************************\n"
            props_and_time += (repr(self.prompt))
            props_and_time += ("\nTIME:" + model2.time + "\n")
        print(props_and_time)