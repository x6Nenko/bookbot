def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  num_words = get_num_words(text)

  characters = get_book_characters(text)

  sorted_characters = sort_on(characters)
  sorted_characters.sort(reverse=True, key=lambda d: d["num"])
  
  print(f"--- Begin report of books/frankenstein.txt ---")
  print(f"{num_words} words found in the document")
  print("")
  for char in sorted_characters:
    print(f"The '{char['char']}' character was found {char['num']} times")
  print("--- End report ---")

def get_num_words(text):
  words = text.split()
  return len(words)

def get_book_text(path):
  with open(path) as f:
    return f.read()

def get_book_characters(text):
  lowered_string = text.lower()
  char_count = {}
  for char in lowered_string:
    if char.isalpha():
      if char in char_count:
        char_count[char] += 1
      else:
        char_count[char] = 1

  return char_count

def sort_on(dict):
  char_list = [{"char": key, "num": value} for key, value in dict.items()]
  return char_list

main()