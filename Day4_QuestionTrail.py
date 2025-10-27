import random
friends = ["alice", "bob", "charlie", "david", "emanuel"]

#option 1
random_friend = random.choice(friends)
print(random_friend)

#option 2
random_index = random.randint(0, 4)
print(friends[random_index])