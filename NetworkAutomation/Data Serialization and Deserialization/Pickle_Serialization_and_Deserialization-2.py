import pickle

friend1 = {"DAN": [20, "London", 123123123], "Maria": [25, "Madrid", 13123123]}
friend2 = {"Andrei": [20, "Bucharest", 1312312312], "Nina": [25, "Barcelona", 345345345]}
friends = (friend1, friend2)

with open('friend.dat', 'wb') as file1:
    pickle.dump(friends, file1) # dict/tuple to binary

with open('friend.dat', 'rb') as file2:
    obj = pickle.load(file2) # binary to dict/tuple
    print(type(obj))
    print(obj)