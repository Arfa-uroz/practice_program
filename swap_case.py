def swap_case(s):
    new_string = s.swapcase()       #swaps the case of all the letters
    return(new_string)

if __name__ == '__main__':
    s = input("Enter your string here   ")
    result = swap_case(s)
    print(result)