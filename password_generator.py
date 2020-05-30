# Use an import statement at the top
import random
word_file = "words.txt"
word_list = []

def generate_password():
    new_pwd=[]
    for var in range(3):
        rand_num = word_list.pop()
        new_pwd.append(rand_num)
    return(new_pwd)

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# Add your function generate_password here
# It should return a string consisting of three random words 
# concatenated together without spaces
def generate_password():
    #return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)
    
    return ''.join(random.sample(word_list,3))


# test your function
print(generate_password())