from typing import List
from lexer import tokens

BRANCH_2 = " ──└"
BRANCH_3 = " ──├"

class DeriveTree():
    parent = None
    depth = 0
    last = True

    def __init__(self, node, childs=[]):
        self.node = node
        self.childs = childs
    
    def propagate(self):
        if type(self.childs) != type([1]):      # debug
            print(self.childs)
        n = len(self.childs)
        i = 0
        for c in self.childs:
            if (type(c) == str):
                print(c)       # debug
            i += 1
            c.parent = self
            c.depth = self.depth + 1
            if i < n:
                c.last = False
            c.propagate()
            
    def printTree(self):
        result = ""

        buff = str(self.node)[::-1] if self.childs else f"{str(self.node)[::-1]}"
        if self.depth > 0:
            buff += BRANCH_2 if self.last else BRANCH_3
            ancestor = self.parent
            while ancestor.parent:
                if ancestor.last:
                    buff += "    "
                else:
                    buff += "   │"
                ancestor = ancestor.parent
        result += buff[::-1]
        
        for c in self.childs:
            result += '\n' + c.printTree()
        
        return result
    
    def __str__(self) -> str:
        return self.node
    

    # === Now the code generating part ===

    # def generate_outcode(self):
    #     output_code = ""
    #     if self.node == "prog":
    #         output_code += self.gen_prog()
    #     return output_code
    

    def gen_prog(self):
        if self.childs[0] == "headers":
            pass
        return self.gen_subprogram()
    
    def gen_headers(self):
        return ""
    
    def gen_subprogram(self):
        return ""


