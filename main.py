def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    words = file_contents.split()
    word_count = len(words)   
     
    print(word_count)


main()