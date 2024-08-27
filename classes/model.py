from llama_cpp import Llama

class Model:
    def __init__(self, model_path, temperature, max_tokens, n_ctx, prompt):
        self.model_path = model_path
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.n_ctx = n_ctx
        self.prompt = prompt

        self.model = Llama(
            model_path=model_path,
            n_ctx=2048    
        )
 
    def run(self):
        output = self.model(
            self.prompt.get_text(),
            max_tokens=self.max_tokens,
            echo=True
        )
        return output['choices'][0]['text'] 
    
    def __repr__(self) -> str:
        content_width = 80
        return f"""
{'-' * (content_width + 2)}
| Model: {self.model_path.ljust(content_width - len("Model: "))}|
| Temperature: {str(self.temperature).ljust(content_width - len("Temperature: "))}|
| Max Tokens: {str(self.max_tokens).ljust(content_width - len("Max Tokens: "))}|
| n_ctx: {str(self.n_ctx).ljust(content_width - len("n_ctx: "))}|
{'-' * (content_width + 2)}
    
    Prompt: 
{self.prompt.get_text()}
    
{'-' * (content_width + 2)}
        """
        
# The idea should be to get the messages from prompt attribute.
#    def create_chat_completion(self, messages):
#        output = self.model.create_chat_completion(
#            max_tokens=self.max_tokens,
#            messages = messages
#        )
#        return output['choices'][0]['message']['content']

