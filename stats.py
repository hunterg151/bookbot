def count_words(text):
    words = text.split()
    total_words = len(words)
    return total_words

def num_of_characters(text):
    text = text.lower()
    char_count = {}

    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def sort_on(char_dict):
    return char_dict["count"]

def chars_to_sorted_list(char_count_dict):
    result = []

    for char, count in char_count_dict.items():
        char_dict = {"char": char, "count": count}
        result.append(char_dict)

    result.sort(reverse=True, key=sort_on)

    return result
