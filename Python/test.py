# count = 8
# for x in range(1, count):
#     count -= 1
#     space = '-'*count
#     ha = '#' * x
#     print(space,ha, ' ', ha, space)

def palindrome(string):
  string = [x.lower() for x in string if x != ' ']
  
  rev = list(reversed(string))
  print(string)
  print(rev)
  return print(string == rev)

palindrome('hello ')
palindrome('race car')
palindrome('Nurses run')