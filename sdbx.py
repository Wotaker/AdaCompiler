import re
from lexer import tokens

ptype_dict = {
        "Integer": "%d",
        "Float":   "%f",
        "String":  "%s"
    }


print("Check:")
if re.match(r'[-]?(\d+\.)?\d+', "-69"):
    print("Succ")

print(ptype_dict["String"])
for t in sorted(tokens):
    print(t)

