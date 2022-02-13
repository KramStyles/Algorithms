def to_jaden_case(string):
    Str = string.split(" ")
    String = ""
    for x in Str:
        if not "'" in x:
            String += x.title() + " "
        else:
            temp = x.split("'")
            temp[0] = temp[0].title()
            String +="'".join(temp) + " "
    return String.strip()
            

def toJadenCase(string):        
    return " ".join(w.capitalize() for w in string.split())