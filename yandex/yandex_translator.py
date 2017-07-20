import requests


def get_html(url):
    """
        Получаем html
    """
    return requests.get(url).text


def save_file(url, name):
    r = requests.get(url, stream=True)
    with open(name, 'bw') as f:
        f.write(r.content)


def get_translation(text, lang):
    URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
    KEY = 'trnsl.1.1.20140730T123951Z.a5b1e775dc0ec361.ee256a09c220ba53be5290a14fe14d719664d450'
    TEXT = text
    LANG = lang

    r = requests.post(URL, data={'key': KEY, 'text': TEXT, 'lang': LANG})

    return eval(r.text)