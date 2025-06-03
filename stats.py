def get_word_count(string):
    return len(string.split())

def get_char_counts(string):
    lower = string.lower()
    counts = {}
    for char in lower:
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1
    return counts

def create_count_list_from_dict(char_counts):
    count_dicts = []
    for key in char_counts:
        count_dicts.append({
            "char": key,
            "count": char_counts[key]
        })
    return count_dicts

def get_char_count_from_list_elem(char_list_elem):
    return char_list_elem["count"]

def sort_counts(char_counts):
    count_list = create_count_list_from_dict(char_counts)
    count_list.sort(key=get_char_count_from_list_elem, reverse=True)
    return count_list
