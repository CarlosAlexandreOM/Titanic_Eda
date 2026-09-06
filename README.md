# Titanic - Análise Exploratória de Dados

O projeto utiliza os dados de passageiros do Titanic para investigar padrões relacionados à sobrevivência e entender como características como sexo, classe, idade e tamanho da família se relacionam com esse resultado.

## Objetivo

Identificar os principais fatores associados à sobrevivência dos passageiros por meio de análise exploratória, estatística descritiva e visualização de dados.

A análise busca identificar **associações**, não estabelecer relações de causalidade.

## Perguntas de Análise

* Qual foi a taxa geral de sobrevivência?
* Como a sobrevivência varia entre homens e mulheres?
* Qual a relação entre classe e sobrevivência?
* Como a idade está relacionada à sobrevivência?
* Passageiros acompanhados tiveram maior sobrevivência?
* Existe relação entre valor da tarifa e sobrevivência?
* Como diferentes características combinadas ajudam a explicar os padrões encontrados?

## Dados

Dataset público do **Titanic: Machine Learning from Disaster**, disponibilizado pelo Kaggle.

* **891 passageiros**
* Granularidade: um registro por passageiro
* Variável principal: `Survived`
* Principais características analisadas: sexo, idade, classe, tarifa, porto de embarque e informações familiares.

## Metodologia

### Preparação dos dados

* Inspeção da estrutura e dos tipos de dados
* Identificação e tratamento de valores ausentes
* Remoção de informações que não seriam utilizadas na análise
* Criação de variáveis relacionadas à idade e ao tamanho da família

### Análise

Foram utilizadas estatísticas descritivas e análises comparativas para investigar a relação entre as características dos passageiros e a variável de sobrevivência.

A **taxa de sobrevivência** foi utilizada como principal métrica.

### Visualização

Os resultados foram explorados por meio de gráficos utilizando Matplotlib e Seaborn, facilitando a identificação de padrões e diferenças entre os grupos.

## Principais Insights

### Sexo

A taxa de sobrevivência das mulheres foi superior a 70%, enquanto a dos homens ficou próxima de 20%.

**Interpretação:** sexo apresenta uma forte associação com a sobrevivência no conjunto analisado.

### Classe

Passageiros da primeira classe apresentaram taxa de sobrevivência superior a 60%, enquanto na terceira classe o valor ficou próximo de 25%.

**Interpretação:** a classe do passageiro apresenta uma associação relevante com a sobrevivência.

### Idade

A sobrevivência apresentou tendência de queda conforme a idade aumentou, com crianças apresentando taxas superiores às observadas em grupos mais velhos.

### Tamanho da família

Passageiros que viajavam em grupos familiares pequenos, especialmente entre 2 e 4 pessoas, apresentaram melhores taxas de sobrevivência. Passageiros sozinhos e famílias muito grandes apresentaram taxas menores.

**Interpretação:** a relação entre tamanho da família e sobrevivência não é linear.

### Tarifa

Passageiros que pagaram tarifas mais altas apresentaram maiores taxas de sobrevivência, resultado consistente com a diferença de classes.

## Limitações

* Os dados representam um único evento histórico.
* As análises são observacionais e indicam associações, não causalidade.
* Existem valores ausentes em algumas variáveis.
* Algumas características possuem forte relação entre si, como classe e tarifa.
* A análise exploratória não controla simultaneamente todos os fatores.

## Conclusão

A análise identificou diferenças relevantes na sobrevivência de acordo com características como **sexo, classe, idade, tamanho da família e tarifa**.

Entre os padrões observados, sexo e classe apresentaram algumas das diferenças mais expressivas nas taxas de sobrevivência.

O projeto demonstra a aplicação de Python para **limpeza, transformação, análise exploratória, estatística descritiva e visualização de dados**.

## Ferramentas

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook

## Estrutura

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

## Como Executar

```bash
git clone https://github.com/CarlosAlexandreOM/Titanic_Eda.git
cd Titanic_Eda
pip install -r requirements.txt
```

Depois, execute o notebook localizado em `notebooks/analise.ipynb`.