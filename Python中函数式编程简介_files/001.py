'''
there are 1,2,3,4 four numbers, how many different three-digit
numbers will they compose(no same numbers in a three-digit number)
'''

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if( i != k ) and (i != j) and (j != k):
                print i,j,k
