# set is unordered and unindexed
sets = {"apple","Orange","1","6"}
print(sets)
#cannot access using index or key
print("apple" in sets)
print("Bananan" in sets)
print("Apple" in sets)
#adding items using add()

sets.add("Banana")
print(sets)

#using update method
# sets.update("hello","there") #wrong output
# print(sets)

sets.update(["hello","there"])
print(sets)

#finding length

print(len(sets))

# remove method

remv = sets.remove("apple")
print(remv)
print(sets)
# sets.remove("apple") # error since apple not present

sets.discard("1")
print(sets)

remv = sets.pop()
print(remv)
print(sets)
