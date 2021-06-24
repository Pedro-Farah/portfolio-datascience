### Previsão do faturamento de uma empresa em novos bairros do Rio de Janeiro [<img align="left" alt="Python" width="30px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" />]()

---

Esse projeto foi realizado para um processo seletivo . O objetivo era, a partir de uma base de dados com informações sobre o faturamento de uma empresa em bairros do 
Rio de Janeiro, gerar informações interessantes sobre o público alvo e construir um modelo regressor para prever o faturamento em novos bairros.

Abaixo, uma explicação das categorias da base de dados:

* codigo - Código do Bairro
* nome - Nome do Bairro
* cidade - Cidade
* estado - Estado
* população - População Total
* popAte9 - População até 9 anos
* popDe10a14 - População de 10 a 14 anos
* popDe15a19 - População de 15 a 19 anos
* popDe20a24 - População de 20 a 24 anos
* popDe25a34 - População de 25 a 34 anos
* popDe35a49 - População de 35 a 49 anos
* popDe50a59 - População de 50 a 59 anos
* popMaisDe60 - População de 60 anos ou mais
* domiciliosA1 - Quantidade de Domicílios de Renda A1
* domiciliosA2 - Quantidade de Domicílios de Renda A2
* domiciliosB1 - Quantidade de Domicílios de Renda B1
* domiciliosB2 - Quantidade de Domicílios de Renda B2
* domiciliosC1 - Quantidade de Domicílios de Renda C1
* domiciliosC2 - Quantidade de Domicílios de Renda C2
* domiciliosD - Quantidade de Domicílios de Renda D
* domiciliosE - Quantidade de Domicílios de Renda E
* rendaMedia - Renda Média por Domicílio
* faturamento - Faturamento Total no Bairro

A abordagem neste projeto foi dividí-lo em 2 partes. A primeira com a limpeza, análise e visualização dos dados e a segunda com a construção dos modelos regressores. 
A primeira parte consistiu principalmente em :

1. Preenchimento de valores nulos
2. Detecção e remoção de outilers
3. Visualização de histogramas dos atributos
4. Estatísticas da base de dados
5. Correlação entre os atributos 


Na segunda parte, as etapas foram as seguintes:

* Comparação entre a acurácia (r2) e RMSE dos seguintes algortimos<br />

      1. Random Forest
      2. Gradient Boosting Regressor
      3. Adaboost Regressor
      4. XG Boost
      
     
 * Escolha do melhor modelo
 * Melhora dos parâmetros através de Grid Search
 * Previsão do faturamento em novos bairros

Abaixo, uma demosntração dos resultados previstos e reais para os bairros:

<br />
<br />
<br />

![alt text](https://github.com/Pedro-Farah/portfolio-datascience/blob/main/previsao_faturamento/im.png)

---









