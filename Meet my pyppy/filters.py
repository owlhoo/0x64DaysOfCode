random_text = ['recenica', 'rec', 'tekst', 'paragraf']


def remove_me(word):
    return not word.startswith('re')


print(list(filter(remove_me, random_text)))
