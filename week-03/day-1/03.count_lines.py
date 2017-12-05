# Write a function that takes a filename as string,
# then returns the number of lines the file contains.
# It should return zero if it can't open the file, and
# should not raise any error.
my_file = "myfile.txt"
def count_lines(my_file):
    try:  
        f = open(my_file, "r")
        lines = f.readlines()
        print(len(lines))
    except FileNotFoundError:
        print("0")
count_lines(my_file)