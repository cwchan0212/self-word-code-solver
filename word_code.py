# Find word code with permutations
# cwzchan
# 5 April 2022
# Reference:
# http://www.11plusforparents.co.uk/Verbal/worksheets/VRTypeNpractice.pdf

from itertools import permutations

def findWordCode():

    wl = input("Enter word list: ").strip()
    print ("\n")
    nl = input("Enter number list: ").strip()
    print ("\n")

    wList = wl.split(" ")
    nList = nl.split(" ")

    nStr = list2Str(nList)
    wStr = ""
    p = permutations(wList,3)
    wnDict = {}
    aDict = {}
    wTmp = ""
    code = ""

    for i in list(p):
        wStr = list2Str(i)
        wnDict = wnStr2Dict(wStr, nStr)
        wTmp = dict2Str(wnDict, wStr)
        if (wTmp == nStr):
            #print(wStr, nStr)
            aDict = sortDict(wStr, nStr)
            print ("Solve: " + str(aDict) + "\n")
            break

    if aDict == {}:
        print ("No Solution. \n")
        exit
    else:
        code = input("Enter word code: ").strip()
        print ("\n")
        findCode(aDict, code)

def findCode(aDict, code):
    sTmp = ""
    lStr = ""
    spDict = {}
    #print(code)
    if (code.isnumeric() == False):
        for i in range(len(code)):
            sTmp = str(code[i])
            if sTmp in aDict:
                lStr = lStr +  aDict[sTmp]
    elif (code.isnumeric() == True):
        spDict = swapDict(aDict)
        for i in range(len(code)):
            sTmp = str(code[i])
            if sTmp in spDict:
                lStr = lStr +  spDict[sTmp]
    if len(lStr) != len(code):
        print ("No Solution. [2]\n")
    else:
        print (lStr)

def swapDict(aDict):
    bDict = {}
    bKey = ""
    for key in aDict:
        bKey = str(aDict[key])
        bDict[bKey] = str(key)
    return bDict

def sortDict(wStr, nStr):
    aDict = wnStr2Dict(wStr, nStr)
    sDict = sorted(aDict.items(), key=lambda d: d[0])
    wDict = {}
    for i in range(len(sDict)):
        wDict[sDict[i][0]] = sDict[i][1]
    return wDict

def dict2Str(wnDict, wStr):
    wTmp = wStr
    for k in wnDict:
        wTmp = wTmp.replace(k, wnDict[k])
    return wTmp

def wnStr2Dict(wStr, nStr):
    wnDict = {}
    for i in range(len(wStr)):
        wnDict[wStr[i:i+1]] = nStr[i:i+1]
    return wnDict

def list2Str(lst):
    lngStr = ""
    for i in range(len(lst)):
        lngStr = lngStr + str(lst[i])
    return lngStr

def main():
    findWordCode()

if __name__ == "__main__":
    main()
