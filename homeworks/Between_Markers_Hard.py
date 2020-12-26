"""
Вам дана строка и два маркера (начальный и конечный).
Вам необходимо найти текст, заключенный между двумя этими маркерами.
Но есть несколько важных условий:

Начальный и конечный маркеры всегда разные
Если нет начального маркера, то началом считать начало строки
Если нет конечного маркера, то концом считать конец строки
Если нет ни конечного, ни начального маркеров, то просто вернуть всю строку
Если конечный маркер стоит перед начальным, то вернуть пустую строку
Input: Три аргумента. Все строки. Второй и третий аргументы это начальный и конечный маркеры.

Output: Строка.

Предусловия: не может быть более одного маркера одного типа
"""
def between_markers(text: str, begin: str, end: str) -> str:
    """
    еще одно решение данной задачи

    b = text.find(begin)
    e = text.find(end)
    if b != -1:
        b += len(begin)
    else:
        b = 0
    if e == -1:
        e = len(text)
    return text[b:e]
    """
    # your code here
    if begin not in text and end not in text:
        return text

    elif begin not in text:
        return text[:text.index(end)]

    elif end not in text:
        return text[text.index(begin) + len(begin):]

    else:
        return text[text.index(begin) + len(begin):text.index(end)]


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
