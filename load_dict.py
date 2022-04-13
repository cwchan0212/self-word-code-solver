dict = open("dict.txt", "r")

ln = ""
pos = -1
codeList = []
cnt = 0

wl = ""
nl = ""
q1 = ""

for x in dict:
    ln = x.strip()

    try:
        if (ln.index(str(cnt+1) + ".") >=0):
            pos = ln.index("=")
            print (ln[pos+1:len(ln)])
            #print(ln, pos)


    except ValueError:
        pos = -1
    #print(ln)
    # try:
    #     pos = ln.index("1)
    #     if (pos > -1):
    #         print (ln)
    # except ValueError:
    #     pos = -1


    #if (ln.index("W=")> 0) :
    #    print (ln)
