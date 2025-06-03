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
