def haveThree(a):
    threes = 0

    for(i = 0; i < len(a); i += 1):
        if (a[i] == 3):
            threes += 1
    return threes == 3


Print haveThree([3,1,3,1,3])#True
Print haveThree([3,4,3,4])#False

def sum28(a):
    for(i = 0; i < len(a); i += 1):
        if (a[i] == 2):
            
