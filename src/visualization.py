import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from typing import Optional

sns.set_theme(style="whitegrid")


def grafico_barras(
    data: pd.DataFrame,
    x: str,
    y: str,
    titulo: str,
    xlabel: str,
    ylabel: str,
    hue: Optional[str] = None,
    percentual: bool = False,
    nome_labels: Optional[list[str]] = None,
    mostrar_legenda: bool = False,
    salvar_em: str | None = None
) -> None:
    """
    Gera um gráfico de barras com opções de agrupamento,
    exibição de percentuais e personalização dos rótulos.
    """

    fig, ax = plt.subplots(figsize=(6, 5))

    sns.barplot(
        data=data,
        x=x,
        y=y,
        hue=hue,
        width=0.5,
        legend=mostrar_legenda,
        ax=ax,
    )

    # Exibe os valores acima das barras
    for container in ax.containers:
        ax.bar_label(
            container,
            fmt="%.1f%%" if percentual else "%.1f",
            padding=3,
        )

    ax.set_title(
        titulo,
        fontsize=14,
        fontweight="bold",
        pad=10,
    )

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    # Permite substituir os rótulos padrão do eixo X
    if nome_labels:
        ax.set_xticks(range(len(nome_labels)))
        ax.set_xticklabels(nome_labels)

    # Ajusta o eixo Y para gráficos percentuais
    if percentual:
        ax.set_ylim(0, 100)

    ax.grid(axis="y", linestyle="--", alpha=0.3)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()

    if salvar_em:
        plt.savefig(salvar_em, dpi=300, bbox_inches="tight")

    plt.show()
    