# load dictionary.txt

def load_dict():
    lines = []
    path = "D:/Users/cwcha/Documents/GitHub/"
    pos = -1
    cnt = 0
    wordBank =[]
    strw = strn = strq = ""
    with open(path + "dict.txt", "rt") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            if (lines[i].find(str(cnt+1) + ".W=") >=0):
                pos = lines[i].index(".W=")
                strw = lines[i][pos+3:len(lines[i])].strip()
            elif (lines[i].find(str(cnt+1) + ".N=") >=0):
                pos = lines[i].index(".N=")
                #print (lines[i][pos+3:len(lines[i])].strip())
                strn = lines[i][pos+3:len(lines[i])].strip()
            elif (lines[i].find(str(cnt+1) + ".Q=") >=0):
                pos = lines[i].index(".Q=")
                #print (lines[i][pos+3:len(lines[i])].strip())
                strq = lines[i][pos+3:len(lines[i])].strip()
                cnt+=1
                wordBank.append([strw, strn, strq])

    for i in range(len(wordBank)):
        print (i, wordBank[i])

def main():
    load_dict()

if __name__ == "__main__":
    main()
