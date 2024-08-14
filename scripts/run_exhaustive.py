from llama_cpp import Llama
import os


def create_model_for_chat_completion(model, data):
    output = model.create_chat_completion(
        max_tokens=1000,
        messages = [
          {
              "role": "system", 
              "content": data["SYSTEM"]},
          {
              "role": "user",
              "content": data["USER"]
          }
      ]
    )

    return output['choices'][0]['message']['content']
    
    
def list_files(folder):
    files = []
    for file_name in os.listdir(folder):
        file_path = os.path.join(folder, file_name)
        files.append(file_path)
    return files

def list_models():
    models = list_files('models/')
    for model in models:
        if not model.endswith('.gguf'):
            models.remove(model)
    return models

def list_prompts():
    default_prompts = list_files('prompts/default_prompts')
    sur_prompts = list_files('prompts/system_user_roles_prompts')
    prompts = default_prompts + sur_prompts
    return prompts

if __name__ == "__main__":
    from run_model import create_model, get_system_user_role_prompt, run_model, get_default_prompt
    model_paths = list_models()
    prompt_paths = list_prompts()
    for model_path in model_paths:
        model = create_model(model_path)
        for prompt_path in prompt_paths:
            if prompt_path.endswith(".txt"):
                prompt_data = get_default_prompt(prompt_path)
                run_model(model, prompt_data)
            else:     
                prompt_data = get_system_user_role_prompt(prompt_path)
                create_model_for_chat_completion(model, prompt_data)
            
