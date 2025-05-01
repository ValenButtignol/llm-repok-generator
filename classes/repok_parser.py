from classes.string_constants import CLASS_SUFFIX, CLOSE_REASONING_TAG, OPEN_REASONING_TAG, PRIVATE_DECL, PRIVATE_PROP_SIG, PRIVATE_REPOK_SIG, PROTECTED_DECL, PROTECTED_PROP_SIG, PROTECTED_REPOK_SIG, PUBLIC_DECL, PUBLIC_PROP_SIG, PUBLIC_REPOK_SIG, REPOK_CLASS_FILENAME, REPOK_CLASS_PREFIX, TAB

class RepOKParser:

    def set_repOK_completion(self, completions : str):
        self.completions = completions

    def parse(self) -> str:
        repok_snippets = self._parse_methods()
        return self._build_repOK_classes(repok_snippets)
    
    def _parse_methods(self) -> list:
        snippets = []
        for completion in self.completions:
            lines = completion.splitlines()
            inside_reasoning = False
            inside_snippet = False
            snippet = ""
            for line in lines:
                stripped = line.strip()        
                if stripped == OPEN_REASONING_TAG:
                    inside_reasoning = True
                    
                elif stripped == CLOSE_REASONING_TAG:
                    inside_reasoning = False

                elif not inside_reasoning and not inside_snippet and self._startswith_repoksignature(stripped):
                    inside_snippet = True
                    bracket_count = 1
                    snippet += TAB + line + "\n"

                elif not inside_reasoning and inside_snippet and self._startswith_accessmodifier(stripped):
                    inside_snippet = True
                    bracket_count += 1
                    snippet += TAB + line + "\n"

                elif inside_snippet and bracket_count != 0:
                    bracket_count += line.count("{") - line.count("}")
                    snippet += TAB + line + "\n"
                    if bracket_count == 0:
                        snippet += "\n"

            snippets.append(snippet)
        return snippets
    
    def _build_repOK_classes(self, repok_snippets):
        classes = []
        class_number = 1
        for snippet in repok_snippets:
            modified_snippet = snippet.replace("repOK", f"repOK_{class_number}") \
                                      .replace("property", f"property_{class_number}")
            
            repok_class = REPOK_CLASS_PREFIX(class_number)
            repok_class += modified_snippet + "\n"
            repok_class += CLASS_SUFFIX
            classes.append((repok_class, REPOK_CLASS_FILENAME(class_number)))
            class_number += 1
    
        return classes

    
    def _startswith_repoksignature(self, text):
        return (text.startswith(PUBLIC_REPOK_SIG) or text.startswith(PUBLIC_PROP_SIG) or
                text.startswith(PROTECTED_REPOK_SIG) or text.startswith(PROTECTED_PROP_SIG) or 
                text.startswith(PRIVATE_REPOK_SIG) or text.startswith(PRIVATE_PROP_SIG))
    
    def _startswith_accessmodifier(self, text):
        return (text.startswith(PUBLIC_DECL) or text.startswith(PRIVATE_DECL) or
                text.startswith(PROTECTED_DECL))
