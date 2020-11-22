if __name__ == '__main__':
    n = int(input("no of students"))
    student_marks = {}
    for i in range(n):                       #it stores all the "names":[scores] in a dictionary named student_marks
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input("query name")
    student_marks1 = student_marks.keys()    #it makes a list of al the keys,i.e. names
    def average(l):
        x=sum(l)                             #it calculates the sum of all the elements in the list i.e. l
        avg =(x/len(l))
        print(f"{avg:.2f}")                  #it prints the average with 2 decimal places          
    for key in student_marks1:
        if key  == query_name:
            average(student_marks[key])    #here actually when we write student_marks[key], we send the values in that key to the function average
    