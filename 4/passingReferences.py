def eggs(someParameter):
    newList = someParameter[:] # use slice to make copy
    # could also use import copy and copy.copy() as well
    newList.append('Hello')
    
spam = [1, 2, 3]
eggs(spam)
print(spam)
