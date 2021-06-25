### Classificação de sentimentos dos clientes em relação a Amazon Alexa [<img align="left" alt="Python" width="30px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" />]()

---

A base de dados utilizada para este projeto consistia em reviews de clientes que possuíam produtos da linha Alexa, da Amazon. Ela era formada pela nota do cliente,
tipo de produto, comentário e feedback (1 -> positivo e 0 -> negativo).

Foram realizadas várias análises com os dados disponíveis. Uma técnica interessante foi dividir a base em dados com o feedback positivo e negativo e gerar a nuvem de 
palavras com as mais utilizadas. Por exemplo, para o feedback positivo foi observada a seguinte nuvem de palavras:

![alt text](https://github.com/Pedro-Farah/portfolio-datascience/blob/main/amazon_alexa/download%20(3).png)

Para o feedback negativo:

![alt text](https://github.com/Pedro-Farah/portfolio-datascience/blob/main/amazon_alexa/negative.png)

Isso por si só, já seria uma análise bem interessante para se fazer sobre um produto. Porém, outros processamentos foram realizados para que fosse possível a construção do 
algoritmo classificador. Na sequência, foi realizada a remoção da pontuação da coluna de reviews, bem como a remoção das chamadas "stop words". Essas, são palavras sem
conotação positiva ou negativa que são usadas geralmente em todos os tipos de frases ("I", "Have", "Me", "Myself" etc).

Na sequência foi realizada a chamada tokenização, onde é contabilizada a quantidade de vezes que uma determinada palavra aparece. 

Em seguida, foram construídos os algoritmos em si. Foram utilizados o Naive Bayes e a Regressão Logística. 

Exemplo da matriz de confusão alcançada com o Naive Bayes:

![alt text](https://github.com/Pedro-Farah/portfolio-datascience/blob/main/amazon_alexa/conf_matrix_nb.png)

---
