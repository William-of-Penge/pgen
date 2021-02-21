def generate_words_8192():
    with open('corncob_lowercase.txt', 'r') as f:
        words = f.read().split()
        shortwords = [w for w in words if len(w) < 6]
        medwords = [w for w in words if len(w) == 6]
        words_8192 = sorted(shortwords+medwords[0:8192-len(shortwords)])
        words_8192 = list(map(str.capitalize, words_8192))
        with open('words_8192.txt', 'w', encoding='utf-8') as f:
            for w in words_8192:
                f.write(w+'\n')

