# Study permuttations & combinations
# https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permuttations-of-a-given-string/?ref=lbp
# https://www.geeksforgeeks.org/print-all-possible-combinations-of-r-elements-in-a-given-array-of-size-n/

# permuttations Calculator: nCr = C(n,r) = n! / ( r! (n - r)! )
# https://www.calculatorsoup.com/calculators/discretemathematics/permuttations.php
# Comination calculators: nCr = C(n,r) = n! / ( r! (n - r)! )
#https://www.calculatorsoup.com/calculators/discretemathematics/combinations.php

combi = []
permut = []

def perm(wl, x, y):

    if (x==y):
        #print (wl)
        permut.append(wl)
        #permut.append(wl)
    else:
        for i in range(x, y+1):
            wl[x], wl[i] = wl[i], wl[x]
            perm(wl, x+1, y)
            wl[x], wl[i] = wl[i], wl[x]
    #return permut
    #print (permut)

def comp(wl, n, r):
    sl = []
    for i in range(r):
        sl.append(r)
    combine(wl, sl, 0, n-1, 0, r)

def combine(wl, sl, start, end, index, r):

    tmp = ""
    #print(start, end, index, r)
    if (index == r):
        for j in range(r):
            tmp = tmp + sl[j] + "@"
            #print(sl[j])
        #print()
        tmp = tmp[0: len(tmp)-1]
        combi.append(tmp.split("@"))
        return

    i = start;
    while (i <= end and end-1+1 >= r-index):
        sl[index] = wl[i];
        combine(wl, sl, i+1, end, index+1, r)
        i += 1


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
    r = 2 # no of balls drawn
    n = len(wl)
    s = []

    comp(wl, n, r)
    #print (combi)

    for i in range(len(combi)):
        print (combi[i])
        print()

        perm(combi[i], 0, len(combi[i])-1)

    print(permut)

#     #print (r, n)
#     if (r==n):
#         x = 0
#         y = n - 1
#         perm(wl, 0, y)
#         #perm(wl, x, y)
#     else:
#         comp(wl, n, r)
#         for i in range(len(combi)):
#             x = 0
#             y = len(combi[i])-1
#             #print(combi[i])
#             perm(combi[i], x, y)
#
#             #print (combi[i])
#
# #    print(permut)
#
#     for i in range(len(permut)):
#         print (i, permut[i])


    #perm(wl, x , y)permu



if __name__ == "__main__":
    main()
