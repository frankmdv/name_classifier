import pandas as pd
import unicodedata
import os
from path import DATASET_PATH, RESULTS_PATH


def read_excel(filename, sheet_name=0):
    filepath = os.path.join(DATASET_PATH, filename)
    return pd.read_excel(filepath, sheet_name=sheet_name)


def to_excel(df, filename):
    df.to_excel(os.path.join(RESULTS_PATH, filename), index=False)


def remove_accents(text):
    normalized = unicodedata.normalize("NFD", text)
    without_accents = "".join(
        char for char in normalized if unicodedata.category(char) != "Mn"
    )

    return without_accents
