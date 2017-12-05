# Write a function that copies a file to an other
# It should take the filenames as parameters
# It should return a boolean that shows if the copy was successful

def copy_file(from_file, to_file):
        from_file = "myfile.txt"
        to_file = "copiedmyfile.txt"
        f = open(from_file, "r")
        copy = f.read()
        f.close()
        f1 = open(to_file, "w")
        f1.write(copy)
        f1.close()
copy_file("myfile.txt", "copiedmyfile.txt")