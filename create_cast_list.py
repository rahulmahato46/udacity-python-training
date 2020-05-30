def create_cast_list(filename):
    cast_list=[]
    with open(filename) as f:
        for line in f:
            name = line.split(",")[0]
            cast_list.append(name.strip())
    return cast_list

cast_list = create_cast_list("flying_circus_cast.txt")
for actors in cast_list:
    print(actors)