# Create a method that decrypts reversed-lines.txt
def decrypt(file_name):
    file_name = "reversed.txt"
    to_file_name = "new_reversed.txt"
    f = open(file_name, "r")
    f_cont = f.read()
    f.close()
    f1 = open(to_file_name, "w")
    for i in list(f_cont)[-1]:
        f1.write(i)
    