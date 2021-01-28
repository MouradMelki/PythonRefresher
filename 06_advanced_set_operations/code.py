friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne", "Mourad"}

local_friends = friends.difference(abroad)

print(local_friends)


local = {"Emil", "Samer", "Ali"}
abroad = {"Sam", "Edy", "Jad"}

friends = local.union(abroad)
print(friends)

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

both = art.intersection(science)
print(both)