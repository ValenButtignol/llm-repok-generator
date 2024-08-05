from ctransformers import AutoModelForCausalLM

# Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.


llm = AutoModelForCausalLM.from_pretrained("TheBloke/CodeLlama-13B-GGUF",model_file="codellama-13b.Q6_K.gguf", model_type="llama", gpu_layers=0)

from transformers import LlamaTokenizerFast
import transformers
import torch


tokenizer = LlamaTokenizerFast.from_pretrained("TheBloke/CodeLlama-13B-GGUF")
pipeline = transformers.pipeline("text-generation",model="TheBloke/CodeLlama-13B-GGUF")

sequences = pipeline(
    "AI is going to",
    do_sample=True,
    top_k=10,
    temperature=0.1,
    top_p=0.95,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
    max_length=200,
)
for seq in sequences:
    print(f"Result: {seq['generated_text']}")



