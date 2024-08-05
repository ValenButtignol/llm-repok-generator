from llama_cpp import Llama
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-f", "--file", dest="filename",
                    help="write report to FILE", metavar="FILE")

args = parser.parse_args()

prompt_file = open(args.filename, "r")
prompt = prompt_file.read()

llm = Llama(
      model_path="../../models/phind-codellama-34b-v2.Q5_K_M.gguf",
)

output = llm(
      prompt, # Prompt
      max_tokens=300, 
      #stop=["}\n\n"],
      echo=True # Echo the prompt back in the output
)


print("\n")
print(output['choices'][0]['text']) 
