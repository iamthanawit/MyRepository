#


## Data Serialization and Deserialization with Pickle

import pickle

# Declaring a dictionary
friends = {"Dan": (20, "London", 12312312), "Maria": [25, "Madrid", 23423423]}

# Serializaing the dictionary to binary file called 'friend.dat' ----- dict/tuple to binary
with open ('friends.dat', 'wb') as f: # b -> binary mode
    pickle.dump(friends, f)

# Deserializaing into a Python Object ----- binary to dict/tuple
with open('friends.dat', 'rb') as f:
    obj = pickle.load(f)

    print(type(obj)) # => dict
    print(obj) # => {"Dan": (20, "London", 12312312), "Maria": [25, "Madrid", 23423423]}

