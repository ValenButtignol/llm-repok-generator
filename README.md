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

You can find plenty of models in [HuggingFace Web](https://huggingface.co/models). You can download any of your choice. We are using the following models:
- [CodeLlama-13B-GGUF](https://huggingface.co/TheBloke/CodeLlama-13B-GGUF) (Using Q8_0.gguf version).
```
wget -O /models https://huggingface.co/TheBloke/CodeLlama-13B-GGUF/resolve/main/codellama-13b.Q8_0.gguf
```

- [Phind-CodeLlama-34B-v2-GGUF](https://huggingface.co/TheBloke/Phind-CodeLlama-34B-v2-GGUF) (Using Q5_K_M.gguf version).
```
wget -O /models https://huggingface.co/TheBloke/Phind-CodeLlama-34B-v2-GGUF/resolve/main/phind-codellama-34b-v2.Q5_K_M.gguf
```
  
### Run models
