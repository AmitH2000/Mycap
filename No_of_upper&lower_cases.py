def countupperandlower(sentence):
    m=n=0
    for i in sentence:
        if i>='A' and i<='Z':
            m+=1
        elif i>='a' and i<='z':
            n+=1
    print(m)
    print(n)
countupperandlower("You know nothing,Jon Snow")
