from llama_cpp import LlamaGrammar

ALLOY_GBNF = r"""
root          ::= alloyModule
alloyModule   ::= (moduleDecl ws)? import* paragraph* ws

moduleDecl    ::= "module" ws qualName ("[" name ("," ws name)* "]")? ws
import        ::= "open" ws qualName ("[" qualName ("," ws qualName)* "]")? ("as" ws name)? ws

paragraph     ::= sigDecl | factDecl | predDecl | funDecl | assertDecl | cmdDecl

sigDecl       ::= ("abstract" ws)? (mult ws)? "sig" ws name ("," ws name)* (sigExt ws)? ("{" ws decl* "}")? ws (block ws)?
sigExt        ::= "extends" ws qualName | "in" ws qualName ("+" ws qualName)* ws
mult          ::= "lone" | "some" | "one" ws
decl          ::= ("disj" ws)? name ("," ws name)* ":" ws ("disj" ws)? expr ws

factDecl      ::= "fact" ws (name ws)? block ws
predDecl      ::= "pred" ws (qualName "." ws)? name (paraDecls ws)? block ws
funDecl       ::= "fun" ws (qualName "." ws)? name (paraDecls ws)? ":" ws expr ws "{" ws expr ws "}"
paraDecls     ::= "(" ws decl* ")" | "[" ws decl* "]" ws

assertDecl    ::= "assert" ws (name ws)? block ws
cmdDecl       ::= (name ws ":")? ("run" | "check") ws (qualName | block) (scope ws)?

scope         ::= "for" ws number (("but" ws typescope ("," ws typescope)*) | (typescope ("," ws typescope)*)) ws
typescope     ::= ("exactly" ws)? number ws qualName ws

expr          ::= const | qualName | "@" ws name ws | "this" ws
                | unOp ws expr
                | expr binOp expr
                | expr arrowOp expr
                | expr "[" ws (expr ("," ws expr)*)? "]"
                | expr ("!" | "not") ws compareOp expr
                | expr ("=>" | "implies") ws expr "else" ws expr
                | "let" ws letDecl ("," ws letDecl)* blockOrBar
                | quant ws decl ("," ws decl)* blockOrBar
                | "{" ws decl* blockOrBar "}"
                | "(" ws expr ")" ws | block ws

const         ::= "-"? ws number | "none" ws | "univ" ws | "iden" ws
unOp          ::= "!" | "not" | "no" | mult | "set" | "hash" | "~" | "*" | "^" ws
binOp         ::= "||" | "or" | "&&" | "and" | "<=>" | "iff" | "=>" | "implies" | "&" | "+" | "-" | "++" | "<:" | ":>" | "." ws
arrowOp       ::= (mult | "set")? "->" (mult | "set")? ws
compareOp     ::= "in" | "=" | "<" | ">" | "=<" | ">=" ws

letDecl       ::= name "=" ws expr ws

block         ::= "{" ws expr* "}" ws
blockOrBar    ::= block | bar ws expr ws
bar           ::= "|" ws
quant         ::= "all" | "no" | "sum" | mult ws

qualName      ::= ("this/" ws)? (name "/" ws)* name ws

name          ::= [a-zA-Z_] [a-zA-Z0-9_]* ws
number        ::= [0-9]+ ws
ws            ::= [ \t\n]*
"""

ARITHMETIC_GBNF = r"""
root  ::= (expr "=" ws term "\n")+
expr  ::= term ([-+*/] term)*
term  ::= ident | num | "(" ws expr ")" ws
ident ::= [a-z] [a-z0-9_]* ws
num   ::= [0-9]+ ws
ws    ::= [ \t\n]*
"""

minimal_grammar = LlamaGrammar.from_string(ARITHMETIC_GBNF)

#alloy_grammar = LlamaGrammar.from_string(grammar=ALLOY_GBNF)
