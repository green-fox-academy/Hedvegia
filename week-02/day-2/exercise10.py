# - Create a variable named `r`
#   with the following content: `[54, 23, 66, 12]`
# - Print the sum of the second and the third element

r = [54, 23, 66, 12]
print(r[1] + r[2])

#training

r = [54, 23, 66, 12]

print(sum(r))

r2 = 0
for i in r:
    r2 += i

print(r2)