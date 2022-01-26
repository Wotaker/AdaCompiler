
# C Code Generator
class CCG():

    ws = " "
    tab = "    "
    nl = "\n"
    ptype_dict = {
        "int":      "%d",
        "float":    "%f",
        "str":      "%s",
        "bool":     "%d"
    }
    relop_dict = {
        "=":        "==",
        "\=":       "!="
    }


    def __init__(self, deriviation_tree) -> None:
        self.deriviation_tree = deriviation_tree
    
    
    def generate_code(self):
        return self.gen_prog(self.deriviation_tree)
    
    # ===== Code generating part =====

    def gen_prog(self, prog):
        default_headers = """#include <stdio.h>
#include <stdbool.h>

"""
        return default_headers +\
            (self.gen_headers(prog.childs[0]) if str(prog.childs[0]) == "headers" else "") + \
            self.gen_subprogram(prog.childs[-1])

    def gen_headers(self, headers):
        return ""
    
    def gen_subprogram(self, subprogram):
        return (self.gen_procedure(subprogram.childs[0]) if str(subprogram.childs[0]) == "procedure" \
            else self.gen_function(subprogram.childs[0]))
    
    def gen_procedure(self, proc, main=False):
        name = proc.childs[1].node.value

        return f"void {name}{self.gen_args_opt(proc.childs[2])} {{\n" + \
            f"{self.gen_declarations(proc.childs[4])}{self.gen_statements(proc.childs[6])}}}\n"
    
    def gen_args_opt(self, args_opt):
        return "()" if args_opt.childs[0].node == "empty" else \
            f"({self.gen_args(args_opt.childs[1])})"
    
    def gen_args(self, args):
        return (f"{self.gen_args(args.childs[0])}, " if str(args.childs[0]) == "args" else "") + \
            self.gen_arg(args.childs[-1])
    
    def gen_arg(self, arg):
        name = arg.childs[0].node.value
        return f"{self.gen_type(arg.childs[2])} {name}"

    def gen_type(sefl, type):
        ada_type = type.childs[0].node.value
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
        if declaration.childs[0].node == "function":
            return self.gen_function(declaration.childs[0])
        if declaration.childs[0].node == "procedure":
            return self.gen_procedure(declaration.childs[0])
        if declaration.childs[0].node == "empty":
            return ""
        return f"{self.gen_type(declaration.childs[2])} {declaration.childs[0].node.value} = " +\
            f"{self.gen_value(declaration.childs[4])};\n"
    
    def gen_value(self, value):
        return self.gen_expr(value.childs[0]) if str(value.childs[0]) == "expr" \
            else self.gen_bool_expr(value.childs[0])
    
    def gen_expr(self, expr):
        return (f"{self.gen_expr(expr.childs[0])} {expr.childs[1].node.value} " if len(expr.childs) == 3 else "") \
            + self.gen_term(expr.childs[-1])
    
    def gen_term(self, term):
        return (f"{self.gen_term(term.childs[0])} {term.childs[1].node.value} " if len(term.childs) == 3 else "") \
            + self.gen_factor(term.childs[-1])
    
    def gen_factor(self, factor):
        if len(factor.childs) == 3:
            return f"({self.gen_expr(factor.childs[1])})"
        if factor.childs[0].node == "function_call":
            return self.gen_function_call(factor.childs[0])
        return factor.childs[0].node.value

    def gen_bool_expr(self, bool_expr):
        print(bool_expr)
        if len(bool_expr.childs) == 1:
            return self.gen_bool_term(bool_expr.childs[0])
        sign = "||" if bool_expr.childs[1].node.value == "or" else "&&"
        return self.gen_bool_term(bool_expr.childs[0]) + f" {sign} " + self.gen_bool_term(bool_expr.childs[2])

    def gen_bool_term(self, bool_term):
        return ("!" if len(bool_term.childs) == 2 else "") + self.gen_bool_factor(bool_term.childs[-1])

    def gen_bool_factor(self, bool_factor):
        if len(bool_factor.childs) == 3 and bool_factor.childs[1].node == "bool_expr":
            return f"({self.gen_bool_expr(bool_factor.childs[1])})"
        if len(bool_factor.childs) == 3 and bool_factor.childs[1].node == "rel_operator":
            return self.gen_rel_operand(bool_factor.childs[0]) +\
                f" {self.gen_rel_operator(bool_factor.childs[1])} " + self.gen_rel_operand(bool_factor.childs[2])
        if bool_factor.childs[0].node.name == "IDENT":
            return bool_factor.childs[0].node.value
        return "0" if bool_factor.childs[0].node.value == "FALSE" else "1"
    
    def gen_rel_operator(self, rel_operator):
        return self.relop_dict.get(rel_operator.childs[0].node.value, rel_operator.childs[0].node.value)

    def gen_rel_operand(self, rel_operand):
        return rel_operand.childs[0].node.value

    def gen_statements(self, stms):
        return (self.gen_statements(stms.childs[0]) if str(stms.childs[0]) == "statements" else "") +\
            self.gen_statement(stms.childs[-1])
    
    def gen_statement(self, stm):
        if stm.childs[0].node == "assign":
            return self.gen_assign(stm.childs[0])
        if stm.childs[0].node == "if":
            return self.gen_if(stm.childs[0])
        if stm.childs[0].node == "loop":
            return self.gen_loop(stm.childs[0])
        if stm.childs[0].node == "put_line":
            return self.gen_put_line(stm.childs[0])
        if stm.childs[0].node == "function_call":
            return f"{self.gen_function_call(stm.childs[0])};" 
        else:
            print("ERROR in gen_statement")
    
    def gen_ret_statements(self, ret_stms):
        return (self.gen_ret_statements(ret_stms.childs[0]) if len(ret_stms.childs) == 2 else "") \
            + self.gen_ret_statement(ret_stms.childs[-1])

    def gen_ret_statement(self, ret_stm):
        if len(ret_stm.childs) == 1:
            return self.gen_statement(ret_stm.childs[0])
        return f"return {self.gen_value(ret_stm.childs[1])};\n"
    
    def gen_assign(self, assign):
        return f"{assign.childs[0].node.value} = {self.gen_value(assign.childs[2])};\n"

    def gen_if(self, if_stm):
        return f"if ({self.gen_bool_expr(if_stm.childs[1])}) {{\n{self.gen_ret_statements(if_stm.childs[3])}}}\n" +\
            f"{self.gen_elsifs(if_stm.childs[4])}{self.gen_else(if_stm.childs[5])}"

    def gen_elsifs(self, elsifs):
        return self.gen_elsifs(elsifs.childs[0]) + self.gen_elsif(elsifs.childs[1]) \
            if len(elsifs.childs) == 2 else ""

    def gen_elsif(self, elsif):
        return f"else if ({self.gen_bool_expr(elsif.childs[1])}) {{\n{self.gen_ret_statements(elsif.childs[3])}}}\n"

    def gen_else(self, else_stm):
        if len(else_stm.childs) == 2:
            return f"else {{\n{self.gen_ret_statements(else_stm.childs[1])}}}\n"
        return ""

    def gen_loop(self, loop):
        if len(loop.childs) == 1:
            return f"for (;;) {self.gen_loop_body(loop.childs[0])}"
        if loop.childs[0].node == "for_range":
            return self.gen_for_range(loop.childs[0]) + self.gen_loop_body(loop.childs[1])
        if loop.childs[0].node == "while":
            return self.gen_while(loop.childs[0]) + self.gen_loop_body(loop.childs[1])

    def gen_loop_body(self, loop_body):
        return f"{{\n{self.gen_statements(loop_body.childs[1])}}}\n"

    def gen_for_range(self, for_range):
        return f"for (int {for_range.childs[1].node.value} = {self.gen_expr(for_range.childs[3])}; " +\
            f"i <= {self.gen_expr(for_range.childs[5])}; i++) "

    def gen_while(self, while_stm):
        return f"while ({self.gen_bool_expr(while_stm.childs[1])}) "

    def gen_function(self, func):
        return f"{self.gen_type(func.childs[4])} {func.childs[1].node.value}" +\
            f"{self.gen_args_opt(func.childs[2])} {{\n" + \
            f"{self.gen_declarations(func.childs[6])}{self.gen_ret_statements(func.childs[8])}}}\n"
    
    def gen_function_call(self, func_call):
        return f"{func_call.childs[0].node.value}({self.gen_value(func_call.childs[2])})"
    
    def gen_put_line(self, put_line):
        return self.gen_str_expr(put_line.childs[2]) + 'printf("\\' + 'n");\n'
    
    def gen_str_expr(self, str_expr):
        return (self.gen_str_expr(str_expr.childs[0]) if len(str_expr.childs) == 3 else "") \
            + self.gen_str_term(str_expr.childs[-1])
    
    def gen_str_term(self, str_term):
        if len(str_term.childs) == 1:
            return f'printf({str_term.childs[0].node.value});'
        else:
            ptype = self.gen_type(str_term.childs[0])
            return f'printf(" {self.ptype_dict[ptype]}", {self.gen_value(str_term.childs[4])});'
