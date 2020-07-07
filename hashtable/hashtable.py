class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        
    def find(self, value): # get
      #start at the head
      #loop through the list
      #find value
      #return the node
        cur = self.head

        while cur is not None:
            if cur.value == value:
                return cur
            cur = cur.next

        return None

    def delete(self, value):
        # go to index
        cur = self.head

        # what if the value is at the head?
        if cur.value == value:
            self.head = cur.next
            return cur
        # make prev.next skip
        prev = cur
        cur = cur.next

        while cur is not None:
            if cur.value == value:
                prev.next = cur.next
                return cur
            else:
                prev = cur
                cur = cur.next

        return None
      
    def insert_at_head(self, node):
        node.next = self.head
        self.head = node


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
        # if > 0.7:
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
        # Search the linked list (at the slot?) for the key
        if self.storage[slot] == None:
            self.storage[slot] = HashTableEntry(key, value)
            self.count += 1
        # elif self.storage[slot] is not None:
        else:
            current = self.storage[slot]
            while True:
                if current.key == key:
                    current.value = value
                    break
                if current.next is None:
                    current.next = HashTableEntry(key, value)
                    self.count += 1
                    break
                current = current.next
            #   Somehow traverse "LL" and check if key = key
            # if so: update value to new value
            # else (we reach the end of "LL"): insert value

        # increment the load count

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Find the slot for the key
        self.put(key, None)

        slot = self.hash_index(key)
        # Search the linked list for the key
        at self.storage[slot]:
            LinkedList.find(___)
        # If found, delete it from the linked list, then return the deleted value

        # If not found, return None


        # decrement the load count

    def get(self, key): # find
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Find the slot for the key
        slot = self.hash_index(key)
        # Search the linked list for the key
        at self.storage[slot]:
            LinkedList.find()
        # If found, return the value
        # If not found, return None
        return self.storage[slot]


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Create new array double the size
        # traverse each element in old hash table
            # for each:
                # rehash to new array
                    # put it there



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
