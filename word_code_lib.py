# word_code library

from itertools import permutations

class WordBank():
    def __init__(self):
        pass

    def solveCode(self, wl, nl):
        print(wl)
        print(nl)
        wnList = []
        nlStr = "".join(str(x) for x in nl)
        wStrList = []
        p = permutations(wl, 3)
        for i in list(p):
            #lnStr = ''.join(str(e) for e in p[i])
            lnStr = "".join(i)
            wStrList.append(lnStr)
        wnList = compare(wStrList, nlStr)
        dit = joinList2Dict(wnList)
        #print("d", dit)
        return dit

    def puzzle(self, dit, query):
        if (query.isnumeric()):
            dit = dict((v,k) for k,v in dit.items())
            nl = [int(x) for i in list(query)]
            print ("it is number!")

def joinList2Dict(wnList):
    n = w = []
    dit = {}
    if wnList != []:
        w = list(wnList[0])
        n = [int(x) for x in list(wnList[1])]
        for i in range(len(w)):
            dit[w[i]] = n[i]
        dit = sorted(dit.items(), key = lambda kv:(kv[0], kv[1]))
        #print(dit)

    return dit

def compare(wStrList, nlStr):
    wnList = []
    temp = ""
    nl = [int(i) for i in list(nlStr)]#
    for i in range(len(wStrList)):
        temp = wStrList[i]
        for j in range(len(nl)):
            temp = temp.replace(temp[j:j+1], str(nl[j]))
        if (temp == nlStr):
#            print(wStrList[i], nlStr)
            wnList = [wStrList[i], nlStr]
            break
    return wnList


def str2List(wStr):
    wl = wStr.split(" ")
    return wl


wStr = "TALE STAB BELT TILL"
nStr = "4625 5322 7514"
wl = wStr.split(" ")
nl = [int(i) for i in nStr.split(" ")]
w = WordBank()
dit = w.solveCode(wl, nl)
print (dit)
w.puzzle(dit, "7354")
