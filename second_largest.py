if __name__ == '__main__':
    n = int(input("enter the length of list:"))
    arr = map(int, input("enter space-separated items:").split())
    arr = list(arr)
    max1 = max(arr)
    max2 = min(arr)   #it only works if we take max2 as the smallest value in the list or the smallest delimitter
    for i in arr:
        if i>max2 and i<max1:
            max2=i
    print("2nd largest item:",max2)