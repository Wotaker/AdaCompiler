import re

ptype_dict = {
        "Integer": "%d",
        "Float":   "%f",
        "String":  "%s"
    }


print("Check:")
if re.match(r'[-]?(\d+\.)?\d+', "-69"):
    print("Succ")

print(ptype_dict["String"])

