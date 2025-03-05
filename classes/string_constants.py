LLAMA="Llama3.1"
LLAMA_NAME="Meta-Llama-3.1-8B-Instruct-Q6_K_L.gguf"

DISTILL_LLAMA="Distill-Llama"
DISTILL_LLAMA_NAME="DeepSeek-R1-Distill-Llama-8B-Q6_K_L.gguf"

QWEN="Qwen2.5.1-Coder"
QWEN_NAME="Qwen2.5.1-Coder-7B-Instruct-Q6_K_L.gguf"

DISTILL_QWEN_7B="Distill-Qwen-7b"
DISTILL_QWEN_7B_NAME="DeepSeek-R1-Distill-Qwen-7B-Q6_K_L.gguf"

DISTILL_QWEN_14B="Distill-Qwen-14b"
DISTILL_QWEN_14B_NAME="DeepSeek-R1-Distill-Qwen-14B-Q6_K_L.gguf"

MODELS_FOLDER="models/"
OUTPUT_FOLDER="output/"
TOOLS_FOLDER="tools/"

GLOBAL_PROMPT_TYPE="global"
FEWSHOT_WHOLECLASS_PROMPT_TYPE="fs-w"
FEWSHOT_PARTSOFCLASS_PROMPT_TYPE="fs-p"
DUAL_WHOLECLASS_PROMPT_TYPE="dual-w"
DUAL_PARTSOFCLASS_PROMPT_TYPE="dual-p"
FEWSHOT_OPENAI_WHOLECLASS_PROMPT_TYPE="fs-openai-w"
FEWSHOT_OPENAI_PARTSOFCLASS_PROMPT_TYPE="fs-openai-p"


JAVAPARSER_JAR="javaparser-core-3.26.3.jar"

CLASS_SIGNATURE="### Class Signature\n"
CLASS_ATTRS="### Class Attributes\n"
CLASS_METHODS="### Class Methods\n"

REPOK_TAG="### repOK\n"
BEGIN_CODE_SNIPPET="```java\n"
END_CODE_SNIPPET="\n```"
TAB="    "
CLASS_SUFFIX="""}\n"""
PROPERTY_TAG="""[Property]"""   #TODO: Delete
PROPERTY_METHOD_NAME="property"

def REPOK_CLASS_FILENAME(number):
    return "RepOkClass" + str(number) + ".java"

def REPOK_CLASS_PREFIX(number):
    return "public class RepOkClass" + str(number) + "{\n"