import re
import string
import emoji
import pandas as pd

from pyarabic import araby



punctuations_list = string.punctuation + "،؛؟«»ـ"


def remove_punctuations(text):
    translator = str.maketrans("", "", punctuations_list)
    return text.translate(translator)



def remove_emojis(text):
    return emoji.replace_emoji(text, replace="")



def remove_non_arabic(text):
    # Remove URLs
    text = re.sub(r"http\S+|www\S+", " ", text)

    # Remove English letters and numbers
    text = re.sub(r"[A-Za-z0-9]", " ", text)

    # Keep Arabic characters and whitespace
    text = re.sub(r"[^\u0600-\u06FF\s]", " ", text)

    return text


    # Remove Tashkeel (diacritics) from Arabic text
def remove_diacritics(text):
    return araby.strip_tashkeel(text)



def normalize_arabic(text):
    text = araby.normalize_alef(text)
    text = text.replace("ى", "ي")
    return text


#  Remove Repeating Characters (Tatweel)
def remove_repeating_characters(text):
    return re.sub(r"(.)\1{2,}", r"\1\1", text)


def remove_extra_spaces(text):
    return re.sub(r"\s+", " ", text).strip()

