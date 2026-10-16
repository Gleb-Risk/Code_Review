import random

def shuffle_word(word):
    """Переставляет буквы слова в случайном порядке"""
    letters = list(word)
    random.shuffle(letters)
    return ''.join(letters)

def main():
    # Ввод слова с клавиатуры
    word = input("Введите слово: ")
    original_word = word
    
    # Счётчик попыток
    attempts = 0
    
    # Генерируем случайные перестановки, пока не получим исходное слово
    while True:
        word = shuffle_word(word)
        attempts += 1
        print(word)
        
        if word == original_word:
            break
    
    print(f"{attempts} попыток")

if __name__ == "__main__":
    main()