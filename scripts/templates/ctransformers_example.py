from ctransformers import AutoModelForCausalLM

# Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
llm = AutoModelForCausalLM.from_pretrained("../models/codellama-13b.Q8_0.gguf", model_type="llama", gpu_layers=0)

print(llm("Can you write only a simple function that makes insertion sort for a given array in python?"))

