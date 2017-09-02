def plist(n):
    pls = []
    ls = []
    for i in range(2,n+1):
        ls.append(i)
    while(ls):
        tmp = ls[0]
        pls.append(ls.pop(0))
        if(tmp*tmp<=n):
            for i in ls:
                if(i%tmp==0):
                     ls.remove(i)
        else:
            pls.extend(ls)
            break
    return pls          #return list of prime
