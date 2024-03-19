import re
import logging
import joblib

from pymystem3 import Mystem

vectorizer = [
    joblib.load("app/models/cv-ngram-13.bin"),
    joblib.load("app/models/tfidf-ngram-23.bin"),
]

clf = [
    joblib.load("app/models/lr-cv-ngram-13.bin"),
    joblib.load("app/models/lr-tfidf-ngram-23.bin"),
]

mystem_analyzer = Mystem()

label2name = {
    0: "А.Пушкин",
    1: "Д.Мамин-Сибиряк",
    2: "И.Тургенев",
    3: "А.Чехов",
    4: "Н.Гоголь",
    5: "И.Бунин",
    6: "А.Куприн",
    7: "А.Платонов",
    8: "В.Гаршин",
    9: "Ф.Достоевский",
}


def clean_sentence(sentence):
    sentence = re.sub(r"[^а-яА-ЯёЁ \-\"!'(),.:;?]", "", sentence)
    return sentence


def make_punkt(sentence):
    repl = [
        (".", " POINT "),
        (",", " COMMA "),
        ("?", " QST "),
        ("!", " EXCL "),
        (":", " COLON "),
        (";", " SEMICOL "),
        (",", " DASH "),
    ]
    for p, r in repl:
        sentence = sentence.replace(p, r)
    sentence = re.sub(
        r"\s?-\s|\s-\s?", " DASH ", sentence
    )  # не трогать тире в слове (как-то)
    return sentence


def make_grams(sentence):
    morph = mystem_analyzer.analyze(sentence)

    ret = []
    for lex in morph:
        if lex["text"] in ["POINT", "COMMA", "QST", "EXCL", "COLON", "SEMICOL", "DASH"]:
            ret.append(lex["text"])
            continue

        try:
            if "analysis" in lex.keys() and "gr" in lex["analysis"][0].keys():
                ret.append(lex["analysis"][0]["gr"])
        except KeyError:
            logging.warning('wrong lex:', lex)
            continue
    return " ".join(ret)


def prepare_text(Text_corp):
    res = []
    for text in Text_corp:
        text = clean_sentence(text)
        text = make_punkt(text)
        text = make_grams(text)
        res.append(text)
    return res


def infer(text: str, model :int = 0) -> [int, str, int | float]:

    X_infer = prepare_text([text])
    X_infer = vectorizer[model].transform(X_infer)
    predict_proba = clf[model].predict_proba(X_infer)

    logging.info("\n" + str(text) + "\n")
    logging.info(predict_proba)

    res = sorted(zip(range(len(label2name)), label2name.values(), predict_proba[0]), key=lambda x: x[2], reverse=True)
    return res[0]

if __name__ == "__main__":
    print(infer_one("""успешный успех!"""))


