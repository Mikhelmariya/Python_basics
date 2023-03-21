s= "Iammikhel"
s2=s.replace(" "," *")
if "*" not in s2:
    s2="$"+s2+"$"
print(s2)