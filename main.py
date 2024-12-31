def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    words = file_contents.split()
    word_count = len(words)   
     
    print(word_count)

    def char_count():
        count = {}
        characters = list(file_contents.lower())
        for i in characters:
           if i in count:
               count[i] += 1
           else: 
               count[i] = 1
        print(count)
            
    char_count()



main()

