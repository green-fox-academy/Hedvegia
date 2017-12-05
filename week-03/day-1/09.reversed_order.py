# Create a method that decrypts reversed-order.txt
def decrypt(file_name):
    file_name = "reversed_order.txt"
    to_file_name = "new_reversed_order.txt"
    f = open(file_name, "r")
    f_cont = f.readlines()
    f.close()
    f1 = open(to_file_name, "w")
    for i in list(f_cont)[::-1]:
        f1.write(i)
    f1.close()
decrypt("reversed_order.txt")