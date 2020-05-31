lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0):
    # Implement your generator function here
    for var in iterable:
        yield start, var
        start+=1

for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))