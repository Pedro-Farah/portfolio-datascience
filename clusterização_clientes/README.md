### Agrupamento de clientes de um banco [<img align="left" alt="Python" width="30px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" />]()

---

Este projeto se encontra na categoria de "Aprendizado Não-Supervisionado". Enquanto os outros possuem os chamados "labels", isto é, rótulos que classificam os registros, 
a base de dados utilizada aqui não possui essa característica. Isso porque o objetivo do projeto não era fazer a classificação ou prever um determinado valor numérico,
mas sim, agrupar os registros por grau de similaridade em determinados grupos (clusters). 

Para este projeto, além da limpeza e processamento dos dados, os algortimos utilizados para o agrupamento foram:

* K-Means
* Elbow Method (para determinar o número ideal de clusters)
* PCA (redução de dimensionalidade)
* Auto Encoder (redução de dimensionalidade)

Exemplo da clusterização com o uso de PCA e Auto Encoder para redução de dimensionalidade e do K-Means para agrupar os dados:

![alt text](https://github.com/Pedro-Farah/portfolio-datascience/blob/main/clusteriza%C3%A7%C3%A3o_clientes/clusters.png)

Isso é interessante pois permite à empresa (nesse caso, ao banco) tomar providências em relação aos grupos. Por exemplo, o grupo 1 podem ser clientes mais abastados que podem 
ter seu limite de crédito aumentado.

---
