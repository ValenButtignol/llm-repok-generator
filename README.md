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
- Inside the environment download dependencies:
```
pip install -r requirements.txt
```
- Run the following command to download javaparser:
```
wget -P tools https://repo1.maven.org/maven2/com/github/javaparser/javaparser-core/3.26.3/javaparser-core-3.26.3.jar
```

### Download models

You can find plenty of models in [HuggingFace](https://huggingface.co/models). You can download any of your choice. We are using the following models, and you can execute the following commands from the root of the project to download them:

- [bartowski/Meta-Llama-3.1-8B-Instruct-GGUF](https://huggingface.co/bartowski/Meta-Llama-3.1-8B-Instruct-GGUF) (Q5_K_M).
```
wget -P models https://huggingface.co/bartowski/Meta-Llama-3.1-8B-Instruct-GGUF/resolve/main/Meta-Llama-3.1-8B-Instruct-Q6_K_L.gguf
```

- [bartowski/Qwen2.5.1-Coder-7B-Instruct-GGUF](https://huggingface.co/bartowski/Qwen2.5.1-Coder-7B-Instruct-GGUF) (Q6_K_L)
```
wget -P models https://huggingface.co/bartowski/Qwen2.5.1-Coder-7B-Instruct-GGUF/resolve/main/Qwen2.5.1-Coder-7B-Instruct-Q6_K_L.gguf
```

- [bartowski/DeepSeek-R1-Distill-Qwen-14B-GGUF](https://huggingface.co/bartowski/DeepSeek-R1-Distill-Qwen-14B-GGUF) (Q6_K_L)
```
wget -P models https://huggingface.co/bartowski/DeepSeek-R1-Distill-Qwen-14B-GGUF/resolve/main/DeepSeek-R1-Distill-Qwen-14B-Q6_K_L.gguf
```

- [bartowski/DeepSeek-R1-Distill-Llama-8B-GGUF](https://huggingface.co/bartowski/DeepSeek-R1-Distill-Llama-8B-GGUF) (Q6_K_L)
```
wget -P models https://huggingface.co/bartowski/DeepSeek-R1-Distill-Llama-8B-GGUF/resolve/main/DeepSeek-R1-Distill-Llama-8B-Q6_K_L.gguf
```

- [bartowski/DeepSeek-R1-Distill-Qwen-7B-GGUF](https://huggingface.co/bartowski/DeepSeek-R1-Distill-Qwen-7B-GGUF) (Q6_K_L)
```
wget -P models https://huggingface.co/bartowski/DeepSeek-R1-Distill-Qwen-7B-GGUF/resolve/main/DeepSeek-R1-Distill-Qwen-7B-Q6_K_L.gguf
```

### Run models
To run a model, have in mind the following parameters:

Where:
- `mn` is the name of the model you want to run. You can add options in `classes/model_path_factory.py`.
- `pt` is the prompt type. It can be the following options:
  - `text` for plain text.
  - `txt` for a TXT file.
  - `json` for a JSON file.
  - `global` for basic global repOk prompt.
  - `fs-w` for few-shot with a whole class repOk prompt.
  - `fs-p` for few-shot with parts of a class repOk prompt.
  - `dual-w` for dual prompting with a whole class repOk.
  - `dual-p` for dual prompting with parts of a class repOk.
- `pc` is the prompt container you want to use. It can be plain text from terminal or a file. When `pt` is any repOk option, this parameter must be a Java class.
- `ot` is the output type. It can be "console" or "file".
- `oc` is the output container. It's necessary when `ot` is "file".

An example:
```
python3 main.py -mn "Llama3.1" -pt "json" -pc "prompt_file.json"
```
