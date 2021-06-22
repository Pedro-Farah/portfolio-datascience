# Portfolio de Data Science
Conjunto de projetos realizados na área de Ciência de Dados e Machine Learning

Os projetos foram realizados em sua maioria em  Python e os arquivos estão no formato .py ou no formato de notebook. Eles estão divididos em sub-categorias para que seja mais fácil o acesso. A seguintes sub-categorias são:

* Machine Learning
* Deep Learning


Dentro das categorias Machine Learning e Deep Learning, estão projetos de análise e visualização de dados, classificação binária, multiclasse, regressão, processamento de linguagem natural, séries temporais, processamento de imagens etc. Em Machine Learning estão modelos construídos com algoritmos que não sejam as Redes Neurais. Na pasta Deep Learning estão somente modelos de Redes Neurais. 


## Projetos

---

### Machine Learning

* Previsão de funcionários que deixarão a empresa: O principal objetivo do projeto era, a partir de uma base histórica do registros dos funcionários de uma empresa, construir um modelo classificador para separar os funcionários em duas classes:
Funcionários que provavelmente deixariam a empresa e Funcionários que continuariam na empresa.
* Clusterização de grupos de clientes de um banco: O objetivo desse projeto era fazer a clusterização dos clientes de um banco em determinados grupos para que fosse possível enviar promoções personalizadas para cada grupo.
* Classificação dos sentimentos dos clientes em relação a Amazon Alexa: A partir de uma base de dados textual com reviews de clientes sobre a linha de produtos da Amazon Alexa, foi possível fazer um processamento que permitiu a análise e classificação das reviews como positivas ou negativas a partir do algortimo Naive Bayes.
* Previsão do lucro de uma empresa ao abrir novas filiais em outros bairros: A partir de uma base de dados fictícia de uma empresa atuando no Rio de Janeiro, com informações histórica do faturamento gerado nos bairros, foi possível a criação de um modelo regressor para a previsão do faturamento em novos bairros.


### Deep Learning

* [Classificação de doenças pulmonares por imagens](https://nbviewer.jupyter.org/github/Pedro-Farah/portfolio-datascience/blob/main/doencas_pulmonares/DepartamentoMedico.ipynb): Utilização de Redes Neurais Convolucionais para o processamento de imagens e classificação em 4 tipos diferentes de doenças respiratórias (Healthy (Saudável),  Covid 19, Pneumonia Bacteriana, Pneumonia Viral)
* Detecção de Falhas na Linha de Produção através de Segmentação de Imagens: Neste projeto foram utilizados dois modelos de Redes Neurais. O primeiro modelo foi resposável por detectar se havia defeitos nas peças (ResNet). Tendo sido detectado o defeito, outro modelo foi usado para segmentar a imagem e localizar o defeito (ResUNet). 
* Previsão do preço das ações da Petrobrás: Utilização de uma base de dados histórica e Redes Neurais Recorrentes para a previsão do preço de abertura das ações da Petrobrás. 
* Classificação de digítos numéricos por imagens: Utilização de Redes Neurais Convolucionais para a classificação de imagens de dígitos numéricos escritos a mão. 

