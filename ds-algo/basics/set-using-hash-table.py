# Q: Implement set using hash table
class MySet:
    def __init__(self):
        self.size = 10  # Initial size of the hash table
        self.table = [[] for _ in range(self.size)]  # List of lists for chaining

    def _hash(self, key):
        return hash(key) % self.size

    def add(self, key):
        index = self._hash(key)
        for item in self.table[index]:
            if item == key:
                return  # Key already exists, do nothing
        self.table[index].append(key)  # Add the key

    def remove(self, key):
        index = self._hash(key)
        for i, item in enumerate(self.table[index]):
            if item == key:
                del self.table[index][i]  # Remove the key
                return True
        return False  # Key not found

    def contains(self, key):
        index = self._hash(key)
        for item in self.table[index]:
            if item == key:
                return True
        return False  # Key not found

    def __str__(self):
        return str({item for bucket in self.table for item in bucket})

# Example usage:
my_set = MySet()
my_set.add(1)
my_set.add(2)
print(my_set)  # Output: {1, 2}
print(my_set.contains(1))  # Output: True
my_set.remove(2)
print(my_set)  # Output: {1}

# Runtimes:
# add/remove/contains = O(1) avg time, O(n) worst case (in case of my collisions)