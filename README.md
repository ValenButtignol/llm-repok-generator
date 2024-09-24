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

- [Meta-Llama-3.1-8B-Instruct-GGUF](https://huggingface.co/SanctumAI/Meta-Llama-3.1-8B-Instruct-GGUF/blob/main/meta-llama-3.1-8b-instruct.Q5_K_M.gguf) (Q5_K_M).
```
wget -P models https://huggingface.co/SanctumAI/Meta-Llama-3.1-8B-Instruct-GGUF/resolve/main/meta-llama-3.1-8b-instruct.Q5_K_M.gguf
```

- [Code-Llama-3-8B-GGUF](https://huggingface.co/bartowski/Code-Llama-3-8B-GGUF/blob/main/Code-Llama-3-8B-Q5_K_M.gguf) (Q5_K_M).
```
wget -P models https://huggingface.co/bartowski/Code-Llama-3-8B-GGUF/resolve/main/Code-Llama-3-8B-Q5_K_M.gguf
```

### Run models
To run a model, run from root the following command:
```
python3 main.py -mn "model_name" -tmp N -mtk N -nctx N -pc "prompt" -pt "prompt_type"
```
Where:
- `mn` is the name of the model you want to run. You can add options in `classes/model_path_factory.py`.
- `tmp` is the temperature of the model. It is not required, 0.1 it's default value.
- `mtk` is the maximum tokens. It is not required, 1000 it's default value.
- `nctx` is the number tokens for context. It is not required, 2048 it's default value.
- `pc` is the prompt container you want to use. It can be plain text from terminal or a file.
- `pt` is the prompt type. It can be "text" or "file".

An example:
```
python3 main.py -mn "llama2chat-7b" -tmp 0.2 -mtk 1500 -nctx 1024 -pc "test_generation_prompt.txt" -pt "file"
```
