
# C Code Generator
class CCG():

    ws = " "
    tab = "    "
    nl = "\n"


    def __init__(self, deriviation_tree) -> None:
        self.deriviation_tree = deriviation_tree
    
    
    def generate_code(self):
        return self.gen_prog(self.deriviation_tree)
    
    # ===== Code generating part =====

    def gen_prog(self, prog):
        return (self.gen_headers(prog.childs[0]) if str(prog.childs[0]) == "headers" else "") + \
            self.gen_subprogram(prog.childs[-1])

    def gen_headers(self, headers):
        return "headers" + self.nl

    def gen_subprogram(self, subprogram):
        return (self.gen_procedure(subprogram.childs[0]) if str(subprogram.childs[0] == "proc") \
            else self.gen_function(subprogram.childs[0])) + self.nl
    
    def gen_procedure(self, proc):
        name = proc.childs[1].node.value

        return f"void {name}{self.gen_args_opt(proc.childs[2])} {{\n" + \
            f"{self.gen_declarations(proc.childs[4])}{self.gen_statements(proc.childs[6])}\n}}\n"
    
    def gen_args_opt(self, args_opt):
        return "()" if str(args_opt.childs[0]) == "empty" else \
            f"({self.gen_args(args_opt.childs[1])})"
    
    def gen_args(self, args):
        return (f"{self.gen_args(args.childs[0])}, " if str(args.childs[0]) == "args" else "") + \
            self.gen_arg(args.childs[-1])
    
    def gen_arg(self, arg):
        name = arg.childs[0].node.value
        return f"{self.gen_type(arg.childs[2])} {name}"

    def gen_type(sefl, type):
        ada_type = str(type.childs[0].node.value)
        if ada_type == "Integer":
            return "int"
        elif ada_type == "Float":
            return "double"
        elif ada_type == "Boolean":
            return "bool"

    def gen_declarations(self, declarations):
        return (self.gen_declarations(declarations.childs[0]) if str(declarations.childs[0]) == "declarations" \
            else "") + self.gen_declaration(declarations.childs[-1])
    
    def gen_declaration(self, declaration):
        name = declaration.childs[0].node.value
        return f"{self.gen_type(declaration.childs[2])} {name} = {self.gen_value(declaration.childs[4])}\n"
    
    def gen_value(self, value):
        return self.gen_expr(value.childs[0]) if str(value.childs[0]) == "expr" \
            else self.gen_bool_expr(value.childs[0])
    
    def gen_expr(self, expr):
        return (f"{self.gen_expr(expr.childs[0])} {expr.childs[1].node.value} " if len(expr.childs) == 3 else "") \
            + self.gen_term(expr.childs[-1])
    
    def gen_term(self, term):
        return (f"{self.gen_term(term.childs[0])} {term.childs[1].node.value} " if len(term.childs) == 3 else "") \
            + self.gen_factor(term.childs[-1])
    
    def gen_factor(self, term):
        return f"({self.gen_expr(term.childs[1])})" if len(term.childs) == 3 else term.childs[0].node.value

    def gen_bool_expr(self, bool_expr):
        if len(bool_expr.childs) == 1:
            return self.gen_bools(bool_expr.childs[0])
        sign = "||" if bool_expr.childs[1].node.value == "or" else "&&"
        return self.gen_bools(bool_expr.childs[0]) + f" {sign} " + bool_expr.childs[1].node.value \
            + self.gen_bools(bool_expr.childs[0])

    def gen_bools(self, bools):
        if len(bools.childs) == 3:
            insertion = self.gen_bool_expr(bools.childs[1]) if str(bools.childs[1]) == "bool_expr" else \
                self.gen_bool(bools.childs[1])
            return f"({insertion})"
        else:
            return ("!" if len(bools.childs) == 2 else "") + self.gen_bool(bools.childs[-1])

    def gen_bool(self, boolean):
        return "0" if boolean.childs[0].node.value == "FALSE" else "1"

    def gen_statements(self, statements):
        pass

    def gen_function(self, proc):
        pass