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
        ans = ""
        if (isinstance(query, int)):
            #print ("it is number!", query, dit)
            nl = [int(i) for i in list(str(query))]
            dit = dict((v,k) for k,v in dit.items())
            for k in dit:
                for i in nl:
                    if (i == k):
                        ans += dit[k]
        else:
            #print ("it is NOT number!", query, dit)
            nl = list(query)
            for k in dit:
                for i in nl:
                    if (i == k):
                        ans += str(dit[k])
        return ans

def joinList2Dict(wnList):
    n = w = []
    dit = {}
    if wnList != []:
        w = list(wnList[0])
        n = [int(x) for x in list(wnList[1])]
        #print("wn", w, n)

        for i in range(len(w)):
            dit[w[i]] = n[i]
        #for i in sorted (dit.keys()) :
        #    print (dit[i], i)
        sorted(dit.items(), key = lambda kv:(kv[1], kv[0]))
        #dit = sorted(dit.items(), key = lambda kv:(kv[0], kv[1]))
        #print("dit", dit)
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
#print ("out", dit)
s = w.puzzle(dit, "TALE")
print(s)
