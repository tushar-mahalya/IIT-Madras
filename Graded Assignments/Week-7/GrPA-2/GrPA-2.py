# The basic idea is to write the code for priority equal to "first"
# When priority is "second", we can just reverse the order of the dicts
def merge(D1, D2, priority):
    if priority == 'second':
        return merge(D2, D1, 'first')
    D = dict()
    # First copy all key-value pairs in D1 to D
    for key in D1:
        value = D1[key]
        D[key] = value
    # Copy all those key-value pairs in D2 to D
    # where the key is not already present in D
    for key in D2:
        value = D2[key]
        if key not in D:
            D[key] = value
    return D
