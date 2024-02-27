def main():
    fname = "frankenstein.txt"
    with open(f"./books/{fname}", "r") as f:
        content = f.read()
        word_counts = count_words(content)
        letter_counts = count_letters(content)
        sorted_dict = sort_dict(letter_counts)
        report(fname, word_counts=word_counts, sorted_dict=sorted_dict)


def count_words(content):
    words = content.split()
    return len(words)

def count_letters(content):
    alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                 "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                 "y", "z"]
    zeros = [0]*26
    result = dict(zip(alphabets, zeros))
    chars = []
    for c in content.lower():
        chars.append(c)

    for char in chars:
        if char in alphabets:
            result[char] += 1
    return result

def sort_on(d):
    return d["val"]

def sort_dict(char_dict):
    result = []
    for k, v in char_dict.items():
        result.append({"key": k, "val": v})

    result.sort(reverse=True, key=sort_on)
    return result

def report(fname, word_counts, sorted_dict):
    print(f"--- Begin report of books/{fname} ---")
    print(f"{word_counts} words found in the documnt")
    print()
    for i in sorted_dict:
        print(f"The {i['key']} character was found {i['val']}")
    print("--- End report ---")


if __name__ == "__main__":
    main()
