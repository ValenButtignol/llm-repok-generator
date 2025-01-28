class JsonPrompt():
    def __init__(self, raw_class="", class_name=""):
        self.raw_class = raw_class
        self.class_name = class_name
        self.prompt_data = {"messages":[]}
        
    def get_text(self) -> str:
        return self.prompt_data["messages"]
        
    def add_role_message(self, role, message):
        self.prompt_data["messages"].append({
            "role": role,
            "content": message
        })
        
    def add_assistant_message(self, message):
        self.add_role_message("assistant", message)
        
    def add_user_message(self, message):
        self.add_role_message("user", message)

    def add_system_message(self, message):
        self.add_role_message("system", message)