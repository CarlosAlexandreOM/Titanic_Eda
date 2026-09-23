# Titanic - Análise Exploratória de Dados

Este projeto apresenta uma **análise exploratória dos dados de passageiros do Titanic**, com foco na identificação de padrões associados à sobrevivência. A análise investiga como características como sexo, classe, idade, tamanho da família e tarifa se relacionam com a sobrevivência dos passageiros, utilizando **Python, Pandas, Matplotlib e Seaborn**.

## 1. Objetivo

Identificar os principais fatores associados à sobrevivência dos passageiros do Titanic por meio de **análise exploratória, estatística descritiva e visualização de dados**.

A análise busca compreender como características dos passageiros se relacionam com a sobrevivência, identificando padrões e diferenças entre os grupos analisados.

Os resultados indicam **associações observadas nos dados**, não relações de causalidade.

## 2. Perguntas de Análise

1. Qual foi a taxa geral de sobrevivência dos passageiros?
2. Como a sobrevivência varia entre homens e mulheres?
3. Qual a relação entre classe e sobrevivência?
4. Como a idade está relacionada à sobrevivência?
5. Como o tamanho da família está relacionado à sobrevivência?
6. Existe relação entre o valor da tarifa e a sobrevivência?
7. Como diferentes características combinadas ajudam a explicar os padrões observados?

## 3. Dados

O projeto utiliza o dataset público **Titanic: Machine Learning from Disaster**, disponibilizado pelo Kaggle.

* **Registros:** 891 passageiros
* **Granularidade:** um registro por passageiro
* **Variável principal:** `Survived`
* **Principais características utilizadas:** sexo, idade, classe, tarifa e informações familiares.

### Fonte dos dados

**[Titanic: Machine Learning from Disaster - Kaggle](https://www.kaggle.com/competitions/titanic)**

## 4. Metodologia

### 4.1 Preparação dos dados

* Inspeção da estrutura e dos tipos de dados
* Identificação e tratamento de valores ausentes
* Remoção de informações que não seriam utilizadas na análise
* Criação de variáveis relacionadas à idade e ao tamanho da família

### 4.2 Análise

Foram utilizadas **estatísticas descritivas e análises comparativas** para investigar a relação entre as características dos passageiros e a variável de sobrevivência.

A **taxa de sobrevivência** foi utilizada como principal métrica para comparar os diferentes grupos analisados.

### 4.3 Visualização

Os resultados foram explorados por meio de gráficos utilizando **Matplotlib e Seaborn**, facilitando a identificação de padrões, diferenças e possíveis relações entre as variáveis.

## 5. Ferramentas

* Python
* Pandas
* Matplotlib
* Seaborn
* Jupyter Notebook

## 6. Principais Insights

### Sexo

A taxa de sobrevivência das mulheres foi superior a 70%, enquanto a dos homens ficou próxima de 20%.

**Interpretação:** sexo apresentou uma forte associação com a sobrevivência no conjunto de dados analisado.

### Classe

Passageiros da primeira classe apresentaram taxa de sobrevivência superior a 60%, enquanto na terceira classe o valor ficou próximo de 25%.

**Interpretação:** a classe do passageiro apresentou uma associação relevante com a sobrevivência.

### Idade

A sobrevivência apresentou tendência de queda conforme a idade aumentou, com crianças apresentando taxas superiores às observadas em grupos mais velhos.

**Interpretação:** idade apresentou uma associação com a sobrevivência, com diferenças observadas principalmente entre passageiros mais jovens e grupos de maior idade.

### Tamanho da família

Passageiros que viajavam em grupos familiares pequenos, especialmente entre 2 e 4 pessoas, apresentaram maiores taxas de sobrevivência. Passageiros que viajavam sozinhos e aqueles pertencentes a famílias muito grandes apresentaram taxas menores.

**Interpretação:** a relação entre tamanho da família e sobrevivência não foi linear, indicando diferenças entre passageiros sozinhos, grupos familiares pequenos e famílias maiores.

### Tarifa

Passageiros que pagaram tarifas mais altas apresentaram maiores taxas de sobrevivência.

**Interpretação:** a tarifa apresentou associação com a sobrevivência, mas esse resultado deve ser analisado em conjunto com a classe do passageiro, pois as duas características estão relacionadas.

## 7. Limitações

* Os dados representam um único evento histórico e uma população específica de passageiros.
* As análises são observacionais e indicam associações, não causalidade.
* Existem valores ausentes em algumas variáveis do dataset.
* Algumas características possuem forte relação entre si, como classe e tarifa.
* A análise exploratória não controla simultaneamente todos os fatores que podem estar relacionados à sobrevivência.

## 8. Conclusão

A análise identificou diferenças relevantes nas taxas de sobrevivência de acordo com características como **sexo, classe, idade, tamanho da família e tarifa**.

Entre os padrões observados, sexo e classe apresentaram algumas das maiores diferenças nas taxas de sobrevivência. Também foram identificadas associações entre idade, tamanho da família e tarifa e o resultado analisado.

O projeto demonstra a aplicação de **Python, Pandas, estatística descritiva e visualização de dados** em uma análise exploratória, utilizando dados reais para identificar padrões e relações entre diferentes características.

## 9. Estrutura do Projeto

```text
Titanic_Eda/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── analise.ipynb
│
├── reports/
│   └── figures/
│
├── src/
│   ├── cleaning.py
│   ├── features.py
│   ├── statistics.py
│   └── visualization.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

## 10. Como Executar

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/CarlosAlexandreOM/Titanic_Eda.git
cd Titanic_Eda
pip install -r requirements.txt
```

Depois, abra e execute o notebook localizado em:

```text
notebooks/analise.ipynb
```
