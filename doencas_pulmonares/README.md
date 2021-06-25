### Previsão do faturamento de uma empresa em novos bairros do Rio de Janeiro [<img align="left" alt="Python" width="30px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" />]()

---

O objetivo deste projeto era a utilização de Redes Neurais Convolucionais do tipo ResNet para a classificação de doenças pulmonares através do processamento de imagens.
As imagens eram rotulados de acordo com as 4 categorias abaixo:

* Healthy (Saudável)
* Covid - 19
* Pneumonia Viral
* Pneumonia Bacteriana

Abaixo, uma das imagens que foram utilizadas (pertencente a categoria Covid - 19):

![alt text](https://github.com/Pedro-Farah/portfolio-datascience/blob/main/doencas_pulmonares/download%20(1).png)

Primeiramente foram gerados os datasets de treinamento e teste com a divisão das imagens. Na sequência, foi feita a estrutura da Rede Neural que seria utilizada para fazer o treinamento.

É importante salientar que as Redes Neurais Convolucionais do tipo ResNet são Redes pré-treinadas disponibilzadas pela biblioteca TensorFlow. Seu treinamento não precisa ser 
feito "do zero", de modo que isso proporciona um ganho de tempo muito grande. Apenas é necessário adequar esse pré-treinamento com alguns ajustes e transferir o aprendizado 
para o problema atual (Transfer Learning).

Abaixo, uma imagem da taxa de erro e acerto durante o treinamento:

![alt text](https://github.com/Pedro-Farah/portfolio-datascience/blob/main/doencas_pulmonares/download.png)

---
