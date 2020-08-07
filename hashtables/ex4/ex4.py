# Have to admit this one took me a little while!
# Left commented-out code here for my future reference ...

# Noticed from test case that you could actually solve this
# by simply turning the entire input array into all positives,
# and then just check for dupes : )

def has_negatives(a):
    """
    For an input list of integers, we wish to know which positive numbers
    have corresponding negative numbers in the list.

    Example input:

    ```python
    [ 1, -1, 2, 3, -4, -3, 4, -5, 6, 7 ]
    ```

    Input can be in any order.

    Example return value:

    ```python
    [ 1, 3, 4 ]
    ```

    Because 1, 3, and 4 are the positive numbers that have corresponding
    negative numbers in the list.

    Return value can be in any order.

    Solve this problem with a hash table.

    Limits:

    * The input list can contain approximately 5,000,000 elements.
    """
    # Your code here
    # breakpoint()

    # could start by only caching the positive numbers
    cache = {}

    # probably going to want storage for output
    out_store = []

    # array to hold positive numbers
    arr = [abs(x) for x in a]

    # # array to hold negative numbers
    # neg = []

    # # iterate through nums in list
    # for i, num in enumerate(a):
    #     # if number is positive but not in cache, add it
    #     if num >= 0:
    #         arr.append(num)
    #     else:
    #         neg.append(num)

    # This small for loop handles all of the logic!
    for num in arr:
        if num not in cache:
            cache[num] = num
        else:
            out_store.append(num)

    # for x in pos:
    #     # breakpoint()
    #     if x not in cache:
    #         cache[x] = x
    #         # # remove num from list using its index loc
    #         # # while num in a: a.remove(num) #> https://www.geeksforgeeks.org/python-list-remove/
    #         # del arr[i]

    # for num in neg:
    #     # breakpoint()
    #     # if number has a negative match in cache, append to output arr
    #     if  num == cache[-num]:
    #         out_store.append(cache[-num])

    return out_store


if __name__ == "__main__":
    # print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

    a = list(range(5000000))
    a += [-1, -2, -3]

    result = sorted(has_negatives(a))
    print(result)  # > [1,2,3]
