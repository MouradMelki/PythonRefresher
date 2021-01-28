l = ["Bon", "Rolf", "Anne"] #variables can be eddited, added and removed | order is important
t = ("Bob", "Rolf", "Anne") #can't edit the tupple how so ever | order is important
s = {"Bob", "Rolf", "Anne"} #variables can be eddited, added and removed but can't add duplicates | order isn't important

print(l[0])
print(t[2])

l[0] = "Smith"

print(l)

l.append("Mourad")

print(l)

l.remove("Mourad")

print(l)

s.add("Mourad")

print(s)

s.add("Mourad")

print(s)