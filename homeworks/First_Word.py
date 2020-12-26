"""
Дана строка и нужно найти ее первое слово.

При решении задачи обратите внимание на следующие моменты:

В строке могут встречатся точки и запятые
Строка может начинаться с буквы или, к примеру, с пробела или точки
В слове может быть апостроф и он является частью слова
Весь текст может быть представлен только одним словом и все
Входные параметры: Строка.

Выходные параметры: Строка.

Precondition: text can contain a-z A-Z , . '
"""


def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    # your code here
    my_text = text.replace('.', ' ')
    new_my_text = my_text.replace(',', ' ')
    #print(new_my_text)

    return new_my_text.split()[0]
    # return text.replace('.',' ').replace(',',' ').split()[0] - вариант решения


if __name__ == '__main__':
    print("Example:")
    print(first_word(" a word "))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")