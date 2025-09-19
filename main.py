from stats import words_count, character_counter, key_value
import sys
def get_book_text(path_of_file: str):
    with open(path_of_file) as f:
        return f.read()
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = get_book_text(sys.argv[1])
        count_words = words_count(book)
        count_char = character_counter(book)
        alph = key_value(count_char)
        # print düzeni
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {count_words} total words")
        print("--------- Character Count -------")
        for result in alph:
            if result["char"].isalpha():
                print(f"{result["char"]}: {result["num"]}")

main()