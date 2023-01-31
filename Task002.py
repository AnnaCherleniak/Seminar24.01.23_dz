# 2. Напишите функцию encrypt_caesar(msg, shift), которая кодирует сообщение шифром
# Цезаря и возвращает его. Шифр Цезаря заменяет каждую букву в тексте на букву, которая
# отстоит в алфавите на некоторое фиксированное число позиций.
# В функцию передается сообщение и сдвиг алфавита. Если сдвиг не указан, то пусть ваша
# функция кодирует сдвиг алфавита на 3 позиции:


def encrypt_caesar(msg, shift=3):
    new_msg = ''
    alphabet = [chr(i) for i in range(ord('а'), ord('я') + 1)]
    Alphabet = [chr(i) for i in range(ord('А'), ord('Я') + 1)]
    for el in msg:
        if el in alphabet:
            new_msg += chr(ord(el) + shift)
        elif el in Alphabet:
            new_msg += chr(ord(el) + shift)
        else:
            new_msg += el        
    return new_msg


def decrypt_caesar(msg, shift=3):
    new_msg = ''
    alphabet = [chr(i) for i in range(ord('а'), ord('я') + 1)]
    Alphabet = [chr(i) for i in range(ord('А'), ord('Я') + 1)]
    for el in msg:
        if el in alphabet:
            new_msg += chr(ord(el) - shift)
        elif el in Alphabet:
            new_msg += chr(ord(el) - shift)
        else:
            new_msg += el        
    return new_msg


msg = 'Да здравструет салат Цезарь!'
encrypt = encrypt_caesar(msg)
print(encrypt)
decrypt = decrypt_caesar(encrypt)
print(decrypt)