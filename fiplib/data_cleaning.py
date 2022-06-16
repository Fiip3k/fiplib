import pandas as pd


def missing_values(df: pd.DataFrame):
    result = df.isna().sum()
    return result


def duplicates(df: pd.DataFrame, column: str):
    result = df[df[column].duplicated()]
    return result


def categorical_columns(df: pd.DataFrame):
    s = (df.dtypes == "object")
    result = s[s].index()
    return result


def info(df: pd.DataFrame, column: str):  # TODO
    # print("Missing values:\n{0}\n".format(missing_values(df)))
    # print("Duplicates:\n{0}\n".format(
    #    pd.DataFrame(duplicates(df, column))))
    return
