
def word_counter(book_text):
    word_split = book_text.split()
    return len(word_split)

def character_counter(book_text):
    character_dict = {}
    for char in book_text:
        lower_char = char.lower()
        if lower_char in character_dict:
            character_dict[lower_char] = character_dict[lower_char] + 1
        else:
           character_dict[lower_char] = 1
    
    return character_dict
        
def sort_chars(character_dict):
    sorted_list = []
    for ch, count in character_dict.items():
        sorted_list.append(characters)
        if ch.isalpha():
            sorted_list.append({"char": ch, "num": count})
    print(sorted_list)
    return sorted_list
    