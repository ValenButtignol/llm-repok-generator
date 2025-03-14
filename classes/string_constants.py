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

USER_BASIC_REPOK_PT="u-b-r"
SYSTEM_BASIC_REPOK_PT="s-b-r"
USER_HINTS_REPOK_PT="u-h-r"
SYSTEM_HINTS_REPOK_PT="s-h-r"
USER_FS_REPOK_PT="ufs-r"
USER_ASSISTANT_FS_REPOK_PT="uafs-r"
USER_HINTS_USER_FS_REPOK_PT="u-h-ufs-r"
USER_HINTS_USER_ASSISTANT_FS_REPOK_PT="u-h-uafs-r"
SYSTEM_HINTS_USER_FS_REPOK_PT="s-h-ufs-r"
SYSTEM_HINTS_USER_ASSISTANT_FS_REPOK_PT="s-h-uafs-r"
USER_BASIC_PROPS_PT="u-b-p"
SYSTEM_BASIC_PROPS_PT="s-b-p"
USER_HINTS_PROPS_PT="u-h-p"
SYSTEM_HINTS_PROPS_PT="s-h-p"
USER_FS_PROPS_PT="ufs-p"
USER_ASSISTANT_FS_PROPS_PT="uafs-p"
USER_HINTS_USER_FS_PROPS_PT="u-h-ufs-p"
USER_HINTS_USER_ASSISTANT_FS_PROPS_PT="u-h-uafs-p"
SYSTEM_HINTS_USER_FS_PROPS_PT="s-h-u-p"
SYSTEM_HINTS_USER_ASSISTANT_FS_PROPS_PT="s-h-uafs-p"

JAVAPARSER_JAR="javaparser-core-3.26.3.jar"

CLASS_SIGNATURE="### Class Signature\n"
CLASS_ATTRS="### Class Attributes\n"
CLASS_METHODS="### Class Methods\n"

REPOK_TAG="### repOK\n"
BEGIN_CODE_SNIPPET="```java"
END_CODE_SNIPPET="```"

PUBLIC_REPOK_SIG="public boolean repOK"
PROTECTED_REPOK_SIG="protected boolean repOK"
PRIVATE_REPOK_SIG="private boolean repOK"
PUBLIC_PROP_SIG="public boolean property"
PROTECTED_PROP_SIG="protected boolean property"
PRIVATE_PROP_SIG="private boolean property"
PUBLIC_DECL="public"
PRIVATE_DECL="private"
PROTECTED_DECL="protected"
OPEN_REASONING_TAG="<think>"
CLOSE_REASONING_TAG="</think>"
TAB="    "
CLASS_SUFFIX="""}\n"""
PROPERTY_TAG="\n### Property\n"

def REPOK_CLASS_FILENAME(number):
    return "RepOkClass" + str(number) + ".java"

def REPOK_CLASS_PREFIX(number):
    return "public class RepOkClass" + str(number) + "{\n"