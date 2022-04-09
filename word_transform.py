# Codewriting
# words transformation

def solution(beginWord, endWord, wordList):

    wordPath = []
    cnt = 0
    tranCnt = 0
    tmpWord = ""

    for i in range(len(wordList)):
        if (i==0):
            oldWord = beginWord
            newWord = wordList[i]
            cnt = charCmp(oldWord, newWord)
            if (cnt == 1):
                tmpWord = newWord
                print (oldWord, "->", newWord)
                wordPath.append(tmpWord)
                tranCnt += 1
            else:
                tmpWord = newWord
                wordPath.append(tmpWord)
        else:
            oldWord = tmpWord
            newWord = wordList[i]
            cnt = charCmp(oldWord, newWord)
            if (cnt == 1):
                tmpWord = newWord
                print (oldWord, "->", newWord)
                wordPath.append(tmpWord)
                tranCnt += 1
    print("Word Path:" , wordPath)
    return tranCnt

def charCmp(wla, wlb):
    la = list(wla)
    lb = list(wlb)
    cnt = 0
    for i in range(len(la)):
        #print (la[i], lb[i])
        if (la[i] != lb[i]) :
            cnt += 1
    return cnt

def main():

    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    beginWord = "hit"
#    wordList = ["a", "b", "c"]
    #beginWord = "a"

    endWord = "cog"
    tranCnt = 0
    print("Word List:", wordList)
    tranCnt = solution(beginWord, endWord, wordList)
    print("Transformation Time:", tranCnt)

if __name__ == "__main__":
    main()
