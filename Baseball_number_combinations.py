from itertools import combinations_with_replacement
def combinations(n):
    A=[3,5,10]
    final=[]
    for i in range(2,10):
        B=list(combinations_with_replacement(A,i))
        for j in B:
            j=list(j)
            if(sum(j)==n):
                final.append(j)
    a=len(final)
    return final,a
print(combinations(14))
