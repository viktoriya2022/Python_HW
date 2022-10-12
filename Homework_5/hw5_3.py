# --------------------------------------------------
# 3 Напишите программу, удаляющую из текста все слова, содержащие "абв".
# ---------------------------------------------------


def delete_words(input_text):    
    what_del = input('Что должны содержать удаляемые слова? ')
    words = input_text.split(" ")
    words = [word for word in words if not what_del in word]
    return words

input_text = input('Введите текст: ')
new_words = delete_words(input_text)
print(*new_words)