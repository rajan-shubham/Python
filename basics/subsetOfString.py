import itertools

def find_subsets(string):
    # Get all possible combinations of characters in the string
    combinations = []
    for i in range(len(string) + 1):
        combinations += itertools.combinations(string, i)
    # Filter out the ones that are not subsets of the original string
    subsets = []
    for c in combinations:
        subset = ''.join(c)
        if subset != '':
            subsets.append(subset)
    return subsets

# Test the function
string = 'abc'
subsets = find_subsets(string)
print(subsets)
