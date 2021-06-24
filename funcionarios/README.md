### Previsão de funcionários que deixarão uma empresa [<img align="left" alt="Python" width="30px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" />]()

--- 

#### Descrição 

O objetivo deste projeto foi desenvolver um modelo classificador para fornecer informações sobre a possível saída de alguns funcionários de uma determinada empresa. A base de dados era formada pela avaliação dos funcionários em relação e determinados aspectos da empresa (Satisfação com o trabalho, tempo de contribuição, distância para casa etc). Isso é útil, pois a partir das respostas do funcionário, é possível prever se há chance do mesmo deixar a empresa, permitindo que a empresa toma as devidas providências para evitar a situação. 

#### Desenvolvimento 

Ao longo do desenvolvimento do projeto, alguns passos tiveram que ser realizados para a melhor construção do modelo classificador. Entre eles estão:

* Geração de medidas estatísticas sobre os dados
* Visualização do conjunto total
* Visualização dos subconjuntos separados pelas classes
* Correlação enter os atributos
* Processamento de variáveis categóricas

Na construção do modelo em si, foram utilizados os seguintes algoritmos:

* Regressão Logística
* Random Forest
* Redes Neurais

#### Resultados 

|                     | Acurácia | Precisão | Recall | F1-Score |
|---------------------|----------|----------|--------|----------|
| Regressão Logística |   0.86   |   0.79   |  0.62  |   0.70   |
| Random Forest       |   0.84   |   0.79   |  0.56  |   0.56   |
| Redes Neurais       |   0.85   |   0.75   |  0.70  |   0.71   |

