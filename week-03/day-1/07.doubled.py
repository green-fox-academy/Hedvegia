# Create a method that decrypts the duplicated-chars.txt

def decrypt(file_name, to_file_name):
    file_name = "duplicated-chars.txt"
    to_file_name = "new_duplicated-chars.txt"
    f = open(file_name, "r")
    f_cont = f.read()
    f.close()
    f1 = open(to_file_name, "w")
    for i in list(f_cont)[::2]:
        f1.write(i)
    f1.close()
decrypt("duolicated-chars", "new_duplicated-chars")