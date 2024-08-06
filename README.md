# Final Project

## Overview

The code in this replication package constructs the analysis files for the project.

## Instructions to Replicators

### Download requirements
- Download [Miniconda](https://docs.anaconda.com/miniconda/).
- Create and activate an environment with Miniconda:
```
conda create -n <env-name>
conda activate <env-name>
```
- Inside the environment download a transformers library:
  - [llama-cpp-python](https://github.com/abetlen/llama-cpp-python). This is the one we used.
  - [ctransformers](https://github.com/marella/ctransformers).
In general, to install packages:
```
conda install <package-name>
```

### Download models

You can find plenty of models in [HuggingFace Web](https://huggingface.co/models). You can download any of your choice. We are using the following models, and you can execute the following commands from the root of the project to download them:
- [CodeLlama-13B-GGUF](https://huggingface.co/TheBloke/CodeLlama-13B-GGUF) (Using Q8_0.gguf version).
```
wget -P models https://huggingface.co/TheBloke/CodeLlama-13B-GGUF/resolve/main/codellama-13b.Q8_0.gguf
```

- [Phind-CodeLlama-34B-v2-GGUF](https://huggingface.co/TheBloke/Phind-CodeLlama-34B-v2-GGUF) (Using Q5_K_M.gguf version).
```
wget -P models https://huggingface.co/TheBloke/Phind-CodeLlama-34B-v2-GGUF/resolve/main/phind-codellama-34b-v2.Q5_K_M.gguf
```

- [Llama-2-7B-Chat-GGUF](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF)
```
wget -P models https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q5_K_M.gguf
```

### Run models
To run a model, there are two types of argument needed:
- Model. According to the models that we use, you can select three choices:
  - `codellama-13b`
  - `llama-2-chat`
  - `codellama-34b` 
- Prompt. You can pass a prompt from file or terminal command line:
  - `-f <filename>`
  - `-p <prompt>` (Terminal command line) 
Examples:
```
python3 llama_cpp_file.py -mdl "codellama-13b" -p "Q: Hi ¿Can you explain me some of Python Programming Language? A:" 
```
```
python3 llama_cpp_file.py -mdl "codellama-13b" -f "../prompts/promptTestGen.txt"
```
