from yandex_translator import get_translation


def main(text, lang):
    with open('output.txt', 'w', encoding='utf-8') as f:
        print(*get_translation(text, lang)['text'], file=f)

if __name__ == '__main__':
    main(open('input.txt', encoding='utf-8'), 'ru')
