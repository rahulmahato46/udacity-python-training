new_list=[]
with open("udacity_demo.txt") as f:
    for line in f:
        new_list.append(line.strip())
print(new_list)