for number in range(1, 101):
    printed = ""
    if number%3 == 0:
        printed += "Fizz"
    if number%5 == 0: 
        if(printed != "Fizz"):
            printed += "Buzz"
        else:
            printed += "Buzz"
    if len(printed) != 0: 
        print(printed)
    else: 
        print(number)