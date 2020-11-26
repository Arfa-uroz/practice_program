def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return(line)
sentence= input("Enter your sentence  ")
r = split_and_join(sentence)
print(r) 