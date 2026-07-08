import pandas as pd


def engenharia_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cria novas variáveis para facilitar a análise exploratória dos dados.
    """
    
    df = df.copy()

    # Transforma a variável binária de sobrevivência em uma categoria descritiva
    df["situacao"] = df["Survived"].map({
        0: "Não sobreviveu",
        1: "Sobreviveu"
    })

    # Calcula o tamanho da família (incluindo o próprio passageiro)
    df["tamanho_familia"] = df["SibSp"] + df["Parch"] + 1

    # Agrupa os passageiros em faixas etárias para facilitar a análise
    df["faixa_etaria"] = pd.cut(
        df["Age"],
        # Limites das faixas etárias
        bins=[
            0, 12, 17, 24, 59, 100
        ],
        # Rótulos das categorias
        labels=[
            "Criança",
            "Adolescente",
            "Jovem",
            "Adulto",
            "Idoso"
        ]
    )

    # Agrupa os valores da tarifa em quartis para facilitar a comparação
    df["valor_tarifa"] = pd.qcut(
        df["Fare"],
        q=4,
        labels=[
            "Baixo",
            "Médio",
            "Alto",
            "Muito Alto"
        ],
        duplicates="drop"
    )

    # Traduz os valores da coluna de sexo
    df["Sex"] = df["Sex"].map({
        "female": "Mulher",
        "male": "Homem"
    })

    # Renomeia a coluna para português
    df = df.rename(columns={"Sex": "sexo"})

    return df
