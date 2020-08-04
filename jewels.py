import collections
def jewels(J,S):
    
    
    c=collections.Counter(S)
    print(c)
    count =0
    for js in J:
        count+=c[js]
    return count

J='aA'
S='aAAd'

print(jewels(J = "z", S = "ZZ"))
