def stocasticModel(p13,p31,p32,p23,p14):
    Pi=[]

    D=(p23*(p13+p31*(1+p14))+p32*p13)
    P1=(p23*p31)/D
    P2=(p32*p13)/D
    P3=(p23*p13)/D
    P4=(p23*p31*p14)/D
    
    Pi.append(P1)
    Pi.append(P2)
    Pi.append(P3)
    Pi.append(P4)

    return Pi

#print(stocasticModel(0.3,0.3,0.3,0.3,0.3))
