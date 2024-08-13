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
These libraries probably won't be found in Miniconda's default channel, so you can run the following commands to install them (remember to have your env activated):
```
pip install llama-cpp-python
```
```
pip install ctransformers
```

### Download models

You can find plenty of models in [HuggingFace](https://huggingface.co/models). You can download any of your choice. We are using the following models, and you can execute the following commands from the root of the project to download them:
- [CodeLlama-13B-GGUF](https://huggingface.co/TheBloke/CodeLlama-13B-GGUF/blob/main/codellama-13b.Q8_0.gguf) (Q8_0).
```
wget -P models https://huggingface.co/TheBloke/CodeLlama-13B-GGUF/resolve/main/codellama-13b.Q8_0.gguf
```

- [Phind-CodeLlama-34B-v2-GGUF](https://huggingface.co/lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF/blob/main/Meta-Llama-3.1-8B-Instruct-Q5_K_M.gguf) (Q5_K_M).
```
wget -P models https://huggingface.co/TheBloke/Phind-CodeLlama-34B-v2-GGUF/resolve/main/phind-codellama-34b-v2.Q5_K_M.gguf
```

- [Llama-2-7B-Chat-GGUF](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/blob/main/llama-2-7b-chat.Q5_K_M.gguf) (Q5_K_M).
```
wget -P models https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q5_K_M.gguf
```

- [Meta-Llama-3-8B-Instruct-GGUF](https://huggingface.co/SanctumAI/Meta-Llama-3-8B-Instruct-GGUF/blob/main/meta-llama-3-8b-instruct.Q5_K_M.gguf) (Q5_K_M).
```
wget -P models https://huggingface.co/SanctumAI/Meta-Llama-3-8B-Instruct-GGUF/resolve/main/meta-llama-3-8b-instruct.Q5_K_M.gguf
```

- [Meta-Llama-3.1-8B-Instruct-GGUF](https://huggingface.co/lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF/blob/main/Meta-Llama-3.1-8B-Instruct-Q5_K_M.gguf) (Q5_K_M).
```
wget -P models https://huggingface.co/lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF/resolve/main/Meta-Llama-3.1-8B-Instruct-Q5_K_M.gguf
```

- [Code-Llama-3-8B-GGUF](https://huggingface.co/bartowski/Code-Llama-3-8B-GGUF/blob/main/Code-Llama-3-8B-Q5_K_M.gguf) (Q5_K_M).
```
wget -P models https://huggingface.co/bartowski/Code-Llama-3-8B-GGUF/resolve/main/Code-Llama-3-8B-Q5_K_M.gguf
```

### Run models
To run a model, there are two types of argument needed:
- Model Name. The script would look for the input argument in the 'models' folder.
- Prompt. You can pass a prompt from file or terminal command line:
  - `-fp <file_name>`. The script will look the input argument in the 'prompts' folder.
  - `-tp <text_prompt>`. Terminal command line.
Examples:
```
python3 scripts/run_model.py -mn "llama-2-7b-chat.Q5_K_M.gguf" -tp "Q: Hi ¿Can you explain me some of Python Programming Language? A:" 
```
```
python3 scripts/run_model.py -mn "llama-2-7b-chat.Q5_K_M.gguf" -fp "promptTestGen.txt"
```
