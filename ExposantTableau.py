def AlgoTableau(x,n):
    tab = []
    tab.append(x);
    for i in range(1,n):
        tab.append(x*tab[i-1])
    return tab[n-1]

print (AlgoTableau(2,1))
