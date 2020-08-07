# Hash Tables Sprint Challenge

For the hash tables portion of the sprint challenge, you'll be working
through some algorithm problems that are amenable to being solved
efficiently using a hash table. You know the drill at this point.
Navigate into each exercise's directory, read the instructions for the
exercise laid out in the README, implement your solution in the `.py`
skeleton file, then make sure your code passes the tests by running the
test script with `-v`.


## Hint

Remember: the hashtable key should be the thing you want to search
quickly on! The value is what you want to get back from that search.

---

# Interview Questions

Be prepared to demonstrate your understanding of this week's concepts by answering questions on the following topics. You might prepare by writing down your answers beforehand.

1. **Hashing functions**
- *A hasing function returns a hash value of an object, if applicable. The has value itself will be an integer, and this could be used as an index to a corresponding hash table or dictionary for quick value retrieval, lookup, etc.*
2. **Collision resolution**
- *Collision resolution would be the process for handling duplicate values/overwriting in a hash table. For example, if I have the key `foo` with a value `1`, then a collision would occur once I added another value for `foo`. The programmer ultimately gets to decide how collisions are handled, but using different data structures inside of the hash table (like Linked Lists or arrays) can help manage these collisions.*
3. **Performance of basic hash table operations**
- *I would say the common operations would be `get`, `put` and `delete` and from the hash table itself, these would be `O(1)` runtimes because hash table can simply retrieve value stored at a given key. Having said that, these will each involve `O(n)` somewhere along the line to either create/input data into the hash table, OR to iterate through a given structure to compare values to what's stored in the hash table*
4. **Load factor**
- *This is the number of keys stored / capacity*
5. **Automatic resizing**
- *Automatic resize is a way to reconstruct a hash table based on its load factor. In process, this would involve rehashing each item in hash table to get new index based on new capacity, and then `put`ting the item in the re-sized hash table at its new index*
6. **Various use cases for hash tables**
- *One of the main use cases would be searching for something in a dataset, particularly on large sets with lots of searches. Hash tables are good for this because they're much faster than linear, and they can be implemented over and over again. Another use case would be things like getting word counts, or any computation that could benefit from "memory" of previous calculations.*

We expect you to be able to answer questions in these areas. Your responses contribute to your Sprint Challenge grade.