def stocasticModel(p12,p21):
    
    #p11=1-p12
    #p22=1-p21
    
    #P=[[p11,p12],[p21,p22]]

    # Stocastic Solution
    # Pi*P=Pi
    # sum(Pi)=1

    Pi=[]
    Pi.append(p21/(p21+p12))
    Pi.append(p12/(p21+p12))

    return Pi

print(stocasticModel(0.9,0.4))

