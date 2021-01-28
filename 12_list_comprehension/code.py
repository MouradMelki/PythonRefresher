numbers = [1, 3, 5]
doubled = [x * 2 for x in numbers]

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = [friend for friend in friends if friend.startswith("S")]

print(starts_s)

print("friends: ", id(friends), "start_s: ", id(starts_s))