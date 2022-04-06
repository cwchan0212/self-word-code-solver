# Study permutations & combinations
# https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/?ref=lbp

# Permutations Calculator: nCr = C(n,r) = n! / ( r! (n - r)! )
# https://www.calculatorsoup.com/calculators/discretemathematics/permutations.php

# Sample
# Permutations nPr
# P(4,0) = 1
# P(4,1) = 4
# P(4,2) = 12
# P(4,3) = 24
# P(4,4) = 1

def perm(wl, x, y):
    if (x==y):
        print (wl)
    else:
        for i in range(x, y+1):
            wl[x], wl[i] = wl[i], wl[x]
            perm(wl, x+1, y)
            wl[x], wl[i] = wl[i], wl[x]

def main():
    wl = ["CAST", "CARS", "PART", "TRIP"]
    x = 0
    y = len(wl)- 1
    perm(wl, x , y)

if __name__ == "__main__":
    main()
