# load dictionary.txt


def load_dict():
    lines = []
    path = "D:/Users/cwcha/Documents/GitHub/"
    pos = -1
    cnt = 0
    strw = strn = strq = ""

    with open(path + "dict.txt", "rt") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            if (lines[i].find(str(cnt+1) + ".W=") >=0):
                print (lines[i].strip())
            if (lines[i].find(str(cnt+1) + ".N=") >=0):
                print (lines[i].strip())
            if (lines[i].find(str(cnt+1) + ".Q=") >=0):
                print (lines[i].strip())
                cnt+=1

def main():
    load_dict()

if __name__ == "__main__":
    main()
