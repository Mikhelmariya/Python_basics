s = "hELLO MY name is {} and my age IS {}".format ("Mike",20)
print(s)
s2 = "hELLO MY name is {name} and my age IS {age}".format (age=20,name="Mikhel")
print(s2)
s2 = "hELLO MY name is {1} and my age IS {0}".format ("Mikhel",21)
print(s2)

# print(s.capitalize())
# print(s2.title())
# print(s2.upper())
# print(s2.lower())
# print(s.swapcase())

print("it is raining".count("i"))
s3 ="dcba"
print(sorted(s3))

print("12abc".isidentifier())
print("abc".isidentifier())

s ="Who is the prime minster of india"
print(s.split())
s4 = s.split()
print(s.split("prime"))
print(" ".join(s4))
print(" /".join(s4))

# remove trailing and loading spaces
s = "     mik   "
print(s)
print(s.strip())