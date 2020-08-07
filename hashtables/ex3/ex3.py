def intersection(arrays):
    """
    Find the intersection between multiple lists of integers.
    Do not use numpy or sets to solve this; use dict or hashtables, please.

    And we need to compute the intersection, that is, numbers that exist in all lists.

    (Output can be in any order.)

    Limits:
        - There can be up to 10 lists in the list of lists.
        - The lists can contain up to roughly 1,000,000 elements each.
    """
    # Your code here

    # breakpoint()

    # caching
    cache = {}

    # storage for intersections
    out_list = []

    # # enumerate to get access to indexes
    # for i, arr in enumerate(arrays):

    #     if i not in cache:
    #         # storing key as string to prevent any conflicts
    #         # not sure there would be any, but feels awkward having
    #         # ints as keys
    #         cache[str(i)] = arr

    # iterate through initial arrays
    for x in arrays:
        # iterate through sub-arrays
        for v in x:
            # if number not in cache, add it (value doesn't really matter here)
            if v not in cache:
                cache[v] = 1

            # otherwise, number is in cache, so add it to out_list
            else:
                # add logic to check if number is already in out_list
                if v not in out_list:
                    out_list.append(v)

    return out_list


if __name__ == "__main__":
    # arrays = []

    # arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    # arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    # arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    # print(intersection(arrays))

    arrays = []
    arrays.append([1, 2, 3])
    arrays.append([2, 4, 6])
    arrays.append([9, 8, 2])
    print(intersection(arrays))  # > 2
