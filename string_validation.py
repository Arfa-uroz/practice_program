if __name__ == '__main__':
    s = input()
    alnum=False
    alpha=False
    digit=False
    lower=False
    upper=False
    for i in s:           #checks if any of the characters in the string belong to the following category
        if i.isalnum():   #if True then it enters the if statement oterwise it has False as its initialization 
            alnum=True
        if i.isalpha():
            alpha=True
        if i.isdigit():
            digit=True
        if i.islower():
            lower=True
        if i.isupper():
            upper=True
    print(alnum,alpha,digit,lower,upper,sep="\n")
