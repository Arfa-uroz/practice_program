def mutate_string(string, position, character):
    new_string = string[:position] + character + string[(position + 1):]
    return(new_string)

if __name__ == '__main__':
    s = input("Enter your word   ")
    i, c = input("Enter position  and the character with a space").split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)