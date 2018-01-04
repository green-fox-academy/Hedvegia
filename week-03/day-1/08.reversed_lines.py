# Create a method that decrypts reversed-lines.txt
def decrypt(file_name):
    file_name = "reversed.txt"
    to_file_name = "new_reversed.txt"
    f = open(file_name, "r")
    f_cont = f.readlines()
    f.close()
    print(f_cont)
    f1 = open(to_file_name, "w")
    f2 = []
    for i in f_cont:
        f2.append(i[::-1])
    f3 = ''.join(str(i) for i in f2)
    f1.write(f3)
    f1.close()
decrypt("reversed.txt")