if __name__ == '__main__':
    N = int(input())
    list_1 = []
    for n in range(0,N):
        list_1.append(input().split(" "))
    list_2 = []
    for i in range(0,N):
        a =  list_1[i][0]
        
        if a=="insert" :
            b = int(list_1[i][1])
            c = int(list_1[i][2])
            list_2.insert(b,c)
        elif a=="print":
            print(list_2)
        elif a=="remove":
            b = int(list_1[i][1])
            list_2.remove(b)
        elif a =="append":
            b = int(list_1[i][1])
            list_2.append(b)
        elif a=="sort":
            list_2.sort()
        elif a=="pop":
            list_2.pop()
        elif a=="reverse":
            list_2.reverse()
        
            
    
