from src.cleaning_data import remove_punctuations, remove_non_arabic, remove_emojis, remove_diacritics, normalize_arabic,  remove_extra_spaces ,remove_repeating_characters
import pandas as pd


def preprocessing(data: pd.DataFrame) -> pd.DataFrame:

    data = data.copy()

    data["text"] = data["text"].astype(str)

    data["text"] = data["text"].apply(remove_emojis)
    data["text"] = data["text"].apply(remove_punctuations)
    data["text"] = data["text"].apply(remove_non_arabic)
    data["text"] = data["text"].apply(remove_diacritics)
    data["text"] = data["text"].apply(normalize_arabic)
    data["text"] = data["text"].apply(remove_repeating_characters)
    data["text"] = data["text"].apply(remove_extra_spaces)

    return data

def mapper(data: pd.DataFrame) -> pd.DataFrame:
    data = data.copy()
    data["label"] = data["label"].map({"egyptian": 0, "levantine": 1, "gulf": 2, "maghrebi": 3, "iraqi": 4})
    return data


def tokenize_text(data: pd.DataFrame) -> pd.DataFrame:
    data = data.copy()
    data["text"] = data["text"].apply(lambda x: x.split())
    return data