def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    words = file_contents.split()
    word_count = len(words)   
     
    character_counts = char_count(file_contents)

    char_list = []
    for char, count in character_counts.items():
            char_list.append({"char": char, "count": count})

    def sort_on(dict):
        return dict["count"]
    
    char_list.sort(reverse=True, key=sort_on)
      
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    for item in char_list:
        print(f"The {item['char']} character was found {item['count']} times")
    print("--- End report ---")

def char_count(file_contents):
    count = {}
    characters = list(file_contents.lower())
    for i in characters: 
        if i.isalpha():
            if i in count:
                count[i] += 1
            else: 
                count[i] = 1
    return count 

def sort_on(dict):
    return dict["count"]
    
main()

