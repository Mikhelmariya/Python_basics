D = {}
print(D)
D ={"name":"MIKHEL","AGE": 21}
print(D)
print(D["name"])
D["gender"]="female"
print(D)
D["marks"] = 90
print(D)
del D["marks"]
print(D)
for i in D:
    print(i,D[i])
    
print(D.keys())
print(D.values())
print(max(D))
print(min(D))
print(sorted(D))
