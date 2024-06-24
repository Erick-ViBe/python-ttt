nested_dict = {
    'clients': {
        'joe': 1,
        'tom': 2,
    },
    'vendors': {
        'creative_soft': 44,
        'office_space': 33,
    },
}

def flatten_dict(dictionary: dict, key_prefix='', separator='.'):
    result = []
    for k, v in dictionary.items():
        flattened_key = key_prefix + k
        if isinstance(v, dict):
            result.extend((
                flatten_dict(v, flattened_key + separator, separator).items()
            ))
        else:
            result.append((flattened_key, v))
    return dict(result)

print(flatten_dict(nested_dict))
