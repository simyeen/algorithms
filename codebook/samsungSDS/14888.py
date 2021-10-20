def permutations(prefix, k, arr, r):
    if len(prefix) == r:
        yield prefix
    else:
        for i in range(k, len(arr)):
            arr[i], arr[k] = arr[k], arr[i]
            for next in permutations(prefix + [arr[k]] ,k+1 , arr, r):
                yield next
            arr[i], arr[k] = arr[k], arr[i]


