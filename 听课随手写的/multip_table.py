def cengfa():
    for i in range(1,10):
        for s in range(1,i+1):
            print("%d * %d =%2d"%(s,i,i*s), end="\t")
        print()

