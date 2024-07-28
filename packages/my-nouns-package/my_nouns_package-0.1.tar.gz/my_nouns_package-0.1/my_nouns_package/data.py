def load_nouns(file_path='my_nouns_package/Nouns.txt'):
    with open(file_path, encoding='utf-8') as file:
        nouns = [line.strip() for line in file.readlines()]
    return nouns
