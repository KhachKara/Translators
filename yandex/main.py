from yandex_translator import get_translation   # загружаем яндекс translate api


def main(text, lang):
    """ Функция приниает текстовый блок как аргумент text и в зависимости от lang делает перевод """
    with open('output.txt', 'w', encoding='utf-8') as f:
        print(*get_translation(text, lang)['text'], file=f)

if __name__ == '__main__':
    main(open('input.txt', encoding='utf-8'), 'ru')
