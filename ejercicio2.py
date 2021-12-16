def sumCuadradoPer(n: int):
    lst = [];
    sop = 1;

    while (sop * sop <= n):
        cp = sop*sop;
        lst.append(cp);
        sop+=1;

    valMin = [float("inf") for _ in range(n+1)];
    valMin[0] = 0;

    for i in range(n+1):
        for j in lst:
            if(i-j >= 0):
                valMin[i] = min(valMin[i],valMin[i-j]+1);
    
    return valMin[n];

print(sumCuadradoPer(12));
