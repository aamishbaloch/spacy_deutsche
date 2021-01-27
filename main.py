import spacy


def spacy_playground():
    nlp = spacy.load("de_core_news_sm")
    text = nlp("Ich bin Aamish!")

    for token in text:
        print(
            f'Token: {token}, '
            f'Ids: {token.idx}, '
            f'Punctuation: {token.is_punct}, '
            f'Alpha: {token.is_alpha}, '
            f'Stop: {token.is_stop}'
        )


if __name__ == '__main__':
    spacy_playground()
