def get_word_count(string):
    return len(string.split())

# Determines the count of each character present in string
# Returns a dict with char: count pairs
def get_char_counts(string):
    lower = string.lower()
    counts = {}
    for char in lower:
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1
    return counts

# Converts a dict with char: count pairs into a list of {"char": char, "count": count} entries
def create_count_list_from_dict(char_counts):
    count_dicts = []
    for key in char_counts:
        count_dicts.append({
            "char": key,
            "count": char_counts[key]
        })
    return count_dicts

# Returns the value of "count" key from dict.
# To be used for sorting a list of {"char": char, "count": count} entries
def get_char_count_from_list_elem(char_list_elem):
    return char_list_elem["count"]

# Returns a copy of char_counts sorted by descending "count" keys
def sort_counts(char_counts):
    count_list = create_count_list_from_dict(char_counts)
    count_list.sort(key=get_char_count_from_list_elem, reverse=True)
    return count_list
