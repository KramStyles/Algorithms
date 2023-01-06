import re

pattern = "[\w]"
string = "3443"
if re.search(pattern, string):
    print("Valid")
else:
    print("Invalid")
