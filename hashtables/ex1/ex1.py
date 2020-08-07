def get_indices_of_item_weights(weights, length, limit):
    """
    Given a package with a weight limit limit and a list weights of item weights,
    implement a function get_indices_of_item_weights that finds two items whose
    sum of weights equals the weight limit limit. Your function will return a tuple
    of integers that has the following form:

    (zero, one)

    where each element represents the item weights of the two packages. The higher
    valued index should be placed in the zeroth index and the smaller index should
    be placed in the first index. If such a pair doesn’t exist for the given inputs,
    your function should return None.

    Your solution should run in linear time.

    Example:

    input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
    output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum
    equals 21
    """
    # Your code here

    # can use cache instead of brute force
    cache = {}

    # using the index loop to search for the key and include each value in the
    # dict
    for i in range(length):

        # find the target weight using get ->
        # https://www.geeksforgeeks.org/get-method-dictionaries-python/
        target = cache.get(limit - weights[i])

        # handle "None" special case
        if target is not None:
            return i, target

        # set at the index 'th value
        cache[weights[i]] = i

    return None


if __name__ == "__main__":

    weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
    answer_4 = get_indices_of_item_weights(weights_4, 9, 7)

    print(answer_4[0])  # > 6
    print(answer_4[1])  # > 2
