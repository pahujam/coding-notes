class MyDict:
    def __init__(self):
        self.size = 10  # Initial size of the hash table
        self.table = [[] for _ in range(self.size)]  # List of lists for chaining

    def _hash(self, key):
        return hash(key) % self.size

    def set(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)  # Update existing key
                return
        self.table[index].append((key, value))  # Insert new key-value pair

    def get(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None  # Key not found

    def remove(self, key):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]  # Remove key-value pair
                return True
        return False  # Key not found

    def __str__(self):
        return str({k: v for bucket in self.table for k, v in bucket})

# Example usage:
my_dict = MyDict()
my_dict.set("apple", 1)
my_dict.set("banana", 2)
print(my_dict)  # Output: {'apple': 1, 'banana': 2}
print(my_dict.get("apple"))  # Output: 1
my_dict.remove("banana")
print(my_dict)  # Output: {'apple': 1}

# Notes:
# Runtimes of dict ops:
# 1. insert/update/get/remove -> O(1) avg case assuming good hash distribution, O(n) worst case