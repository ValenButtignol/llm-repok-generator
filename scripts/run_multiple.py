from llama_cpp import Llama
import yaml

def get_system_user_role_prompt(file_prompt):
    with open(f"prompts/system_user_roles_prompts/{file_prompt}", 'r') as file:
        data = yaml.safe_load(file)
    return data

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
    

if __name__ == "__main__":
    from run_model import create_model
    modelpaths = ["models/Code-Llama-3-8B-Q5_K_M.gguf"]
    prompts = [
               "code_mutation_prompt_testpilot2.yaml"
               #"code_mutation_prompt.yaml",
               #"oracle_extension_prompt.yaml",
               #"properties_prompt.yaml",
               #"properties_prompt2.yaml",
               #"test_generation_prompt.yaml"
            ]
    for path in modelpaths:
        model = create_model(path)
        for prompt in prompts:
            prompt_data = get_system_user_role_prompt(prompt)
            create_model_for_chat_completion(model, prompt_data)
            
