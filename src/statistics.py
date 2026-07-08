import pandas as pd


def calcular_taxa_sobrevivencia(df: pd.DataFrame, coluna: str) -> pd.DataFrame:
    """Calcula a taxa de sobrevivência percentual por categoria de uma coluna."""
    return (
        df.groupby(coluna)["Survived"]
        .mean()
        .mul(100)
        .reset_index(name="taxa_sobrevivencia")
    )


def calcular_quantidade(df: pd.DataFrame, coluna: str) -> pd.DataFrame:
    """Calcula a quantidade de registros por categoria de uma coluna."""
    return (
        df[coluna]
        .value_counts()
        .reset_index(name="quantidade")
    )


def calcular_quantidade_por_situacao(df: pd.DataFrame, coluna: str) -> pd.DataFrame:
    """Calcula a quantidade de sobreviventes e não sobreviventes por categoria."""
    return (
        df.groupby(coluna)["situacao"]
        .value_counts()
        .reset_index(name="quantidade")
    )


def calcular_taxa_sobrevivencia_grupo(
    df: pd.DataFrame, coluna1: str, coluna2: str
) -> pd.DataFrame:
    """Calcula a taxa de sobrevivência percentual por combinação de duas colunas."""
    return (
        df.groupby([coluna1, coluna2])["Survived"]
        .mean()
        .mul(100)
        .reset_index(name="taxa_sobrevivencia")
    )


def calcular_quantidade_grupo(
    df: pd.DataFrame, coluna1: str, coluna2: str
) -> pd.DataFrame:
    """Calcula a quantidade de registros por combinação de duas colunas."""
    return (
        df[[coluna1, coluna2]]
        .value_counts()
        .reset_index(name="quantidade")
    )


def calcular_quantidade_por_situacao_grupo(
    df: pd.DataFrame, coluna1: str, coluna2: str
) -> pd.DataFrame:
    """Calcula a quantidade de sobreviventes e não sobreviventes por combinação de duas colunas."""
    return (
        df.groupby([coluna1, coluna2])["situacao"]
        .value_counts()
        .reset_index(name="quantidade")
    )


def calcular_estatisticas_sobrevivencia(
    df: pd.DataFrame, coluna: str
) -> dict[str, pd.DataFrame]:
    """Retorna quantidade, taxa de sobrevivência e quantidade por situação para uma coluna."""
    return {
        "quantidade": calcular_quantidade(df, coluna),
        "taxa": calcular_taxa_sobrevivencia(df, coluna),
        "quantidade_situacao": calcular_quantidade_por_situacao(df, coluna),
    }


def calcular_estatisticas_sobrevivencia_grupo(
    df: pd.DataFrame, coluna1: str, coluna2: str
) -> dict[str, pd.DataFrame]:
    """Retorna estatísticas de sobrevivência para a combinação de duas colunas."""
    return {
        "quantidade": calcular_quantidade_grupo(df, coluna1, coluna2),
        "taxa": calcular_taxa_sobrevivencia_grupo(df, coluna1, coluna2),
        "quantidade_situacao": calcular_quantidade_por_situacao_grupo(df, coluna1, coluna2)
    }
