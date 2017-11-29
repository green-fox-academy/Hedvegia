# I would like to replace "dishwasher" with "galaxy" in this example
# Please fix it for me!
# Expected ouput: In a galaxy far far away


original = "In a dishwasher far far away"
change = original[ : 5] + 'galaxy' + original[15: ]
print(change)