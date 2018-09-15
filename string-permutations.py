def flatten(l):
    return [item for sublist in l for item in sublist]

def stringPermutations(str_size, alphabet):
    if str_size == 0:
        return []
    elif str_size == 1:
        return alphabet
    else:
        return flatten(list(map(lambda permutation : 
                            list(map(lambda letter : letter + permutation, alphabet)), 
                            stringPermutations(str_size - 1, alphabet))))



print(stringPermutations(0, ['A', 'B', 'C']))
print(stringPermutations(1, ['A', 'B', 'C']))
print(stringPermutations(2, ['A', 'B', 'C']))
print(stringPermutations(3, ['A', 'B', 'C']))
