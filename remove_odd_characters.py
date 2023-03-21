s = input("Enter string")
print("Entered string is "+s)
length = len(s)
ns =""
i=0
print(s[i])
for i in range(length):
    if(i%2!=0):
        ns=ns+s[i]
    
    
print("output string :  "+ns)