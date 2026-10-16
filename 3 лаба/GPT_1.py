import random

def shuffle_word(word):
    letters = list(word)
    random.shuffle(letters)
    return ''.join(letters)

def main():
    word = input("Введите слово: ")
    attempts = 0

    while True:
        shuffled = shuffle_word(word)
        print(shuffled)
        attempts += 1

        if shuffled == word:
            break

    print(f"{attempts} попыток")

if __name__ == "__main__":
    main()
