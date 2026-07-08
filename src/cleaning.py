import pandas as pd


def limpar_dados(df: pd.DataFrame) -> pd.DataFrame:
    """Remove colunas não utilizadas e trata valores ausentes da base do Titanic."""
    df = df.copy()

    df = df.drop(["Ticket", "Cabin"], axis=1, errors="ignore")

    df["Age"] = df["Age"].fillna(
        df.groupby(["Pclass", "Sex"])["Age"].transform("median")
    )

    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

    return df
