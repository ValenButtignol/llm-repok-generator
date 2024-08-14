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
        files.append(file_name)
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
    from run_model import get_model_path, create_model, get_system_user_role_prompt, run_model, get_default_prompt
    model_names = list_models()
    prompt_paths = list_prompts()
    
    with open('output.txt', 'w') as file:
        file.write("-----------------------------------------------------\n")
        for model_name in model_names:
            model_path = get_model_path(model_name)
            model = create_model(model_path)
            for prompt_path in prompt_paths:
                file.write(model_name + " -- " + prompt_path + "\n")
                if prompt_path.endswith(".txt"):
                    prompt_data = get_default_prompt(prompt_path)
                    output = run_model(model, prompt_data)
                else:     
                    prompt_data = get_system_user_role_prompt(prompt_path)
                    output = create_model_for_chat_completion(model, prompt_data)
                file.write("output: \n")
                file.write(output + "\n")
                file.write('\n')
                file.write("-----------------------------------------------------\n")
                file.write('\n')


