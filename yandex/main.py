from yandex_translator import get_translation


print(*get_translation(input(':> '),'en')['text'])