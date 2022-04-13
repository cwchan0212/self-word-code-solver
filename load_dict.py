dict = open("dict.txt", "r")

ln = ""
pos = -1

for x in dict:
    ln = x.strip()
    #print(ln)
    try:
        pos = ln.index("W=")
        if (pos > -1):
            print (ln)
    except ValueError:
        pos = -1


    #if (ln.index("W=")> 0) :
    #    print (ln)
