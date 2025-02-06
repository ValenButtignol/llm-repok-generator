LLAMA="Llama3.1"
LLAMA_NAME="meta-llama-3.1-8b-instruct.Q6_K_L.gguf"

DISTILL_LLAMA="Distill-Llama"
DISTILL_LLAMA_NAME=""

QWEN="Qwen2.5.1-Coder"
QWEN_NAME=""

DISTILL_QWEN_7B="Distill-Qwen-7b"
DISTILL_QWEN_7B_NAME=""

DISTILL_QWEN_14B="Distill-Qwen-14b"
DISTILL_QWEN_14B_NAME=""

MODELS_FOLDER="models/"
OUTPUT_FOLDER="output/"
TOOLS_FOLDER="tools/"

GLOBAL_PROMPT_TYPE="global"
FEWSHOT_WHOLECLASS_PROMPT_TYPE="fs-w"
FEWSHOT_PARTSOFCLASS_PROMPT_TYPE="fs-p"
DUAL_WHOLECLASS_PROMPT_TYPE="dual-w"
DUAL_PARTSOFCLASS_PROMPT_TYPE="dual-p"

REPOK_CLASS_FILENAME="RepOkClass.java"
PROPERTIES_CLASS_FILENAME="PropertiesClass.java"

JAVAPARSER_JAR="javaparser-core-3.26.3.jar"

CLASS_SIGNATURE="""[Class Signature]
"""
CLASS_ATTRS="""[Class Attributes]
"""
CLASS_METHODS="""[Class Methods]
"""

CLASS_TAG="""[Class]
"""
REPOK_TAG="""[repOk]
"""
BEGIN_CODE_SNIPPET="""```java"""
END_CODE_SNIPPET="""```"""
TAB="    "
REPOK_CLASS_PREFIX="""public class RepOkClass {\n"""
PROP_CLASS_PREFIX="""public class PropertiesClass {\n"""
CLASS_SUFFIX="""}\n"""
PROPERTY_TAG="""[Property]"""
PROPERTY_METHOD_NAME="property"