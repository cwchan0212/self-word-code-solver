# Study permuttations & combinations
# https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permuttations-of-a-given-string/?ref=lbp
# https://www.geeksforgeeks.org/print-all-possible-combinations-of-r-elements-in-a-given-array-of-size-n/

# permuttations Calculator: nCr = C(n,r) = n! / ( r! (n - r)! )
# https://www.calculatorsoup.com/calculators/discretemathematics/permuttations.php
# Comination calculators: nCr = C(n,r) = n! / ( r! (n - r)! )
#https://www.calculatorsoup.com/calculators/discretemathematics/combinations.php

#from itertools import permutations
#from itertools import combinations

combi = []
permut = []

def perm(wl, x, y):

    if (x==y):
        wTmp = list2Str(wl).strip()
        if len(wTmp) > 0:
            permut.append(wTmp.split("@"))
        else:
            permut.append([''])
    else:
        for i in range(x, y+1):
            wl[x], wl[i] = wl[i], wl[x]
            perm(wl, x+1, y)
            wl[x], wl[i] = wl[i], wl[x]

    return permut

def comp(wl, n, r):
    sl = []
    for i in range(r):
        sl.append(r)
    combine(wl, sl, 0, n-1, 0, r)

def combine(wl, sl, start, end, index, r):

    tmp = ""
    if (index == r):
        for j in range(r):
            tmp = tmp + sl[j] + "@"
        tmp = tmp[0: len(tmp)-1]
        combi.append(tmp.split("@"))
        return

    i = start;
    while (i <= end and end-1+1 >= r-index):
        sl[index] = wl[i];
        combine(wl, sl, i+1, end, index+1, r)
        i += 1

    return combi

def list2Str(wl):

    wStr = ""
    for i in range(len(wl)):
        wStr +=  str(wl[i]) + "@"
    wStr = wStr[0:len(wStr)-1]
    try:
        if (wStr.index("@") >0 ):
            pass
        else:
            wStr = ""
    except ValueError:
        wStr = ""

    return wStr


def main():
    # Sample
    # permuttations nPr
    # P(4,0) = 1
    # P(4,1) = 4
    # P(4,2) = 12
    # P(4,3) = 24
    # P(4,4) = 24

    #Combinations nCr
    # C(4,0) = 1
    # C(4,1) = 4
    # C(4,2) = 6
    # C(4,3) = 4
    # C(4,4) = 1

    wl = ["a", "b", "c", "d"]
    r = 3 # no of balls drawn
    n = len(wl)
    cl = []

    if (n==r):
        cl = wl.copy()
        perm(cl, 0, len(cl)-1)
        # for i in range(len(permut)):
        #     print (i, permut[i])
    else:
        if (r > 0):
            comp(wl, n, r)
            for i in range(len(combi)):
                #print("c", i, combi[i])
                perm(combi[i], 0, len(combi[i])-1)
        else:
            comp(wl, n, r)
            perm(combi, 0, len(combi)-1)

    for i in range(len(combi)):
        print (i, combi[i])

    print()

    for i in range(len(permut)):
        print (i, permut[i])

if __name__ == "__main__":
    main()
