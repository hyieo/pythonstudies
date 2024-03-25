def sum(a: int, b: int) -> int: 
    return a + b

def returnString(): 
    return "a"

# this wont work cause 'returnString' is returning a string 
# print(sum(1, returnString)) 

print(sum(1, 2))