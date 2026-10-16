import random

#FIXME: Неполный Docstring 
#TODO:
def get_plural_word(count):
    """
    Возвращает правильное склонение слова 'попытка' для заданного числа.

    :param count: Количество попыток
    :return: Строка с правильным склонением ('попытка', 'попытки' или 'попыток')
    """
    last_digit = count % 10
    last_two_digits = count % 100
    
    if last_digit == 1 and last_two_digits != 11:
        return "попытка"
    elif 2 <= last_digit <= 4 and not (12 <= last_two_digits <= 14):
        return "попытки"
    else:
        return "попыток"


def main():
    original_word = input("Введите слово: ").strip()
    
    if not original_word:
        print("Слово не может быть пустым.")
        return

    attempts = 0
#FIXME: Избыточные комментарии
#TODO:
    print("\nПроцесс перестановки:")
    while True:
        chars = list(original_word)
        
        random.shuffle(chars)
        
        shuffled_word = "".join(chars)
        
        attempts += 1
        print(shuffled_word)
        
        if shuffled_word == original_word:
            break
            
    plural = get_plural_word(attempts)
    print(f"\n{attempts} {plural}")

if __name__ == "__main__":
    main()