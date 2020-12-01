def count_substring(string, sub_string):
    l= len(sub_string)
    count =0 
    for i in range(0,len(string)):
        if string[i:i+l]==sub_string :
           count+=1 
    return(count)

if __name__ == '__main__':
    string = input("Enter the string   ")).strip()
    sub_string = input("Enter the sub string to be counted").strip()
    
    count = count_substring(string, sub_string)
    print(count)