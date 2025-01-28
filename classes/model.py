from llama_cpp import Llama
import time

class Model:
    def __init__(self, model_path, temperature, max_tokens, n_ctx, prompt):
        self.model_path = model_path
        self.temperature = float(temperature)
        self.max_tokens = int(max_tokens)
        self.n_ctx = int(n_ctx)
        self.prompt = prompt
        self.time = 0

        self.model = Llama(
            model_path=model_path,
            n_ctx=self.n_ctx    
        )
     
    def create_chat_completion(self):
        start = time.time()
        output = self.model.create_chat_completion(
            max_tokens=self.max_tokens,
            messages = self.prompt.get_text(),
            temperature=self.temperature
        )
        end = time.time()
        self.time = end - start
        completion = output['choices'][0]['message']['content']
        self.prompt.add_assistant_message(completion)
        return completion
    
    def reprompt(self, user_message):
        self.prompt.add_user_message(user_message)
        return self.create_chat_completion()
    
    def __repr__(self) -> str:
        content_width = 80
        return f"""
{'-' * (content_width + 2)}
| Model: {self.model_path.ljust(content_width - len("Model: "))}|
| Temperature: {str(self.temperature).ljust(content_width - len("Temperature: "))}|
| Max Tokens: {str(self.max_tokens).ljust(content_width - len("Max Tokens: "))}|
| n_ctx: {str(self.n_ctx).ljust(content_width - len("n_ctx: "))}|
| Time: {str(self.time).ljust(content_width - len("Time: "))}|
{'-' * (content_width + 2)}
    
    Prompt: 
{self.prompt.get_text()}
{'-' * (content_width + 2)}
        """