s = input("Enter string")
print("Entered string is "+s)
vowels = "aeiouAEIOU"
ns =""
for charecter in s:
    if charecter not in vowels:
        ns=ns+charecter
print("new string without vowels : " +"   " +ns)