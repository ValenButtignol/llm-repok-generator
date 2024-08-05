from llama_cpp import Llama

llm = Llama(
      model_path="../../models/phind-codellama-34b-v2.Q5_K_M.gguf",
      # n_gpu_layers=-1, # Uncomment to use GPU acceleration
      # seed=1337, # Uncomment to set a specific seed
      # n_ctx=2048, # Uncomment to increase the context window
)
output = llm(
      "Q: Write a function in Python that makes insertion sort for a given array? A:", # Prompt
      max_tokens=200, # Generate upto 200 tokens, set to None to generate up to the end of the context window
      stop=["```\n\n"],
      #stop=["Q:", "\n"], # Stop generating just before the model would generate a new question
      echo=True # Echo the prompt back in the output
) # Generate a completion, can also call create_completion


print("\n")
print(output) 
