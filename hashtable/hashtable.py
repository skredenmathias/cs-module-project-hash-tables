class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity, count=0):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.count = count
        # self.storage = [LinkedList()] * capacity


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.storage)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Elements in hash table / number of slots
        if (self.count / self.capacity) > 0.7:
            self.resize(2*self.capacity)
        # if > 0.7:
        if (self.count / self.capacity) < 0.2:
            if (self.capacity / 2) >= MIN_CAPACITY:
                self.resize(0.5*self.capacity)
            # use resize



    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        FNV_prime = 1099511628211
        FNV_offset_basis = 14695981039346656037
        hash = FNV_offset_basis

        for s in key:
            hash = hash * FNV_prime
            hash = hash ^ ord(s)
        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here

    def hash_index(self, key): # get_slot(s)
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Find the slot for the key
        slot = self.hash_index(key)
        # Search the linked list (at the slot) for the key
        if self.storage[slot] == None:
            self.storage[slot] = HashTableEntry(key, value)
            self.count += 1
        # elif self.storage[slot] is not None:
        else:
            current = self.storage[slot]
            # True loop so that we can finish loop at the last node.
            while True:
                # If keys match, update the value
                if current.key == key:
                    current.value = value
                    break
                # If reach end of LL without finding key, insert the key, value.
                if current.next is None:
                    current.next = HashTableEntry(key, value)
                    self.count += 1
                    break
                # traverse
                current = current.next

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Find the slot for the key
        slot = self.hash_index(key)
        # Set current
        current = self.storage[slot]
        prev = None

        # Search the linked list for the key
        while current.key != key and current.next is not None:
            prev = current
            current = current.next

        if current.key == key and prev is not None:
            prev.next = current.next
            self.count -= 1

        elif current.key == key:
            self.storage[slot] = current.next
            self.count -= 1

        else:
            return 'key not found.'

    def get(self, key): # find
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Find the slot for the key
        slot = self.hash_index(key)
        # Search the linked list for the key
        current = self.storage[slot]
        while current is not None:
            if current.key == key:
                return current.value
            else:
                current = current.next
        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Create new storage
        new_storage = [None] * new_capacity
        # store the old storage
        old_storage = self.storage
        # Set new storage
        self.storage = new_storage
        # Set new capacity
        self.capacity = new_capacity
        # reset count
        self.count = 0

        # traverse each element in old hash table
        for element in old_storage:
            current = element
            # rehash to new array
            while current is not None:
                self.put(current.key, current.value)
            # Check if empty
                current = current.next


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
