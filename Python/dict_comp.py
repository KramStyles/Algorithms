from ast import comprehension


# nest_dict = {key: {distionary comprehension} for variable in iterable}

{(i,j): i + j for i in range(2) for j in range(2)}

# exec("print('hello')")
# exec(""" 
# print("hi")
# """)

ages = [12, 33, 41, 122, 45, 6]
def ager(x):
    if x > 18:
        return True
    else:
        return False

adults = filter(ager, ages)
print(list(adults))