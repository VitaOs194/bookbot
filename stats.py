def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count = {}
    
    for char in text:
        char = char.lower()
        
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count

def sort_on(dict):
    return dict["count"]

def chars_to_sorted_list(char_count):
    char_list = []
    
    for char, count in char_count.items():
        char_list.append({"char": char, "count": count})
    char_list.sort(reverse=True, key=sort_on)

    return char_list
