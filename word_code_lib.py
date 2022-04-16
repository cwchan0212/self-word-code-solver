# word_code library

from itertools import permutations

class WordBank():
    def __init__(self):
        self.key = None

    def solveCode(self, wl, nl):
        print(wl)
        print(nl)

        nlStr = "".join(str(x) for x in nl)
        wStrList = []
        p = permutations(wl, 3)
        for i in list(p):
            #lnStr = ''.join(str(e) for e in p[i])
            lnStr = "".join(i)
            wStrList.append(lnStr)
        compare(wStrList, nlStr)

def compare(wStrList, nlStr):
    dict ={}
    sl = []
    temp = ""
    cnt = 0
    nl = [int(i) for i in list(nlStr)]
    print (nlStr)
    xx = ""
    for i in range(len(wStrList)):
        xx = wStrList[i]
        #print (xx)
        for j in range(len(nl)):
            wStrList[i] = wStrList[i].replace(wStrList[i][j:j+1], str(nl[j]))
        #print(xx)

        if (wStrList[i] == nlStr):
            print(wStrList[i], nlStr)
        #sl = list(wStrList[i])
        #print (wStrList[i])
        # for j in range(len(wStrList[i])):
        #     temp = wStrList[i].replace(wStrList[i][i:i+1],str(nl[j]))
        # print (temp)



def str2List(wStr):
    wl = wStr.split(" ")
    return wl

wStr = "TALE STAB BELT TILL"
nStr = "4625 5322 7514"

wl = wStr.split(" ")
nl = [int(i) for i in nStr.split(" ")]
# print(wl)
# print(nl)
w = WordBank()
w.solveCode(wl, nl)
