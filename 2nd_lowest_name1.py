if __name__ == '__main__':
    list1 =[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list1.append([score, name])
    list1.sort()     #sorts in ascending order the 1st thing in the list i.e.score in this case
    i=1
    while(True):     #runs forever
        if list1[i][0] != list1[0][0]:
            break     #to come out of the never ending loop that we created
        else:
            i= i+1
    list2 = []
    for j in list1:    #each list in the lists of list i.e,list1 comes as an argument as j
        if j[0] == list1[i][0]:
            list2.append(j)
    allnames=[]
    for k in list2:    #each list from the list of sorted lists comes as an argument at k
        allnames.append(k[1])
    allnames.sort()
    for names in allnames:    #print(*allnames, sep="\n")   \n stands for new line
        print(names)
