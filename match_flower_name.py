def create_flower_dict(filename):
	flower_dict={}
	with open(filename) as flower:
		for line in flower:
			letter=line.split(": ")[0].lower()
			flower_name=line.split(": ")[1].strip()
			flower_dict[letter]=flower_name
	return flower_dict

def main():
	flower_d = create_flower_dict("flowers.txt")
	full_name = input("Enter full name with a space: ")
	first_letter = full_name[0]
	print(flower_d[first_letter])

main()