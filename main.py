from utils import read_excel, to_excel, remove_accents
import numpy as np
import re


def is_abbreviated(name1, name2):
    tokens1 = set(name1.split(" "))
    tokens2 = set(name2.split(" "))
    different_tokens = list(tokens1.symmetric_difference(tokens2))

    abbreviation_pattern = r"[a-z]."

    if (
        len(different_tokens) == 2
        and (
            bool(re.fullmatch(abbreviation_pattern, different_tokens[0]))
            or bool(re.fullmatch(abbreviation_pattern, different_tokens[1]))
        )
        and different_tokens[0][0] == different_tokens[1][0]
    ):
        return True

    return False


def jaccard_similarity(name1, name2):
    tokens1 = set(name1.split(" "))
    tokens2 = set(name2.split(" "))

    common_tokens = tokens1.intersection(tokens2)
    all_tokens = tokens1.union(tokens2)

    try:
        return len(common_tokens) / len(all_tokens)
    except ZeroDivisionError:
        return 0


df_names = read_excel("nombres.xlsx")
df_names["Nombre_Transformado"] = df_names["Nombre"].apply(
    lambda name: remove_accents(name.lower())
)
df_names["Clasificacion"] = np.nan

classification_number = 1

while df_names["Clasificacion"].isna().sum() > 0:
    comparison_name = df_names[df_names["Clasificacion"].isna()][
        "Nombre_Transformado"
    ].values[0]

    df_names["Clasificacion"] = df_names.apply(
        lambda row: (
            classification_number
            if jaccard_similarity(comparison_name, row["Nombre_Transformado"]) > 0.5
            or is_abbreviated(comparison_name, row["Nombre_Transformado"])
            else row["Clasificacion"]
        ),
        axis=1,
    )

    classification_number += 1

df_names.drop(columns="Nombre_Transformado", inplace=True)
df_names.sort_values("Clasificacion", inplace=True)

print(
    """
============================================================
                 CLASIFICACIÓN DE NOMBRES
============================================================
"""
)

print(df_names)

print(
    """
------------------------------------------------------------
       SE HA GENERADO UN EXCEL EN LA CARPETA: 'results'
------------------------------------------------------------
"""
)
to_excel(df_names, "clasificacion_de_nombres.xlsx")
