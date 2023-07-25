def fn_pizza(size,piza):

    pizza_total = size * piza
    return pizza_total

def fn_pasta(size,pasta):

    pasta_total = size * pasta
    return pasta_total

def fn_check():
    check = input("Want to Continue (y/n) : ").upper()
    if check == "Y" or check == "YES":
        return True
    elif check == "N" or check == "NO":
        return  False
    else :
        return False