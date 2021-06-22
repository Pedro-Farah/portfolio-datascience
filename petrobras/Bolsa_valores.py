import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Dropout,LSTM
import numpy as np 
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

base = pd.read_csv ('Petrobras_treinamento.csv')

#TIRANDO OS VALORES NULOS

base = base.dropna ()

#O INTERESSE É PREVER O PREÇO DE ABERTURA, LOGO, AS OUTRAS COLUNAS SERÃO EXCLUÍDAS 

base_treinamento = base.iloc [:,1:2].values

normalizador = MinMaxScaler (feature_range = (0,1))
base_treinamento_normalizada = normalizador.fit_transform (base_treinamento)

#PARA FAZER A PREVISÃO DE UM CERTO DIA, SERÁ UTILIZADO OS PREÇOES DOS 90 DIAS ANTERIORES.
#PARA ISSO SERÁ UTILIZADO UM 'FOR' PARA IR ATUALIZANDO OS VALORES. O FOR DEVE COMEÇAR NO REGISTRO 90 PARA QUE SEJA
#POSSÍVEL UTILIZAR 90 VALORES ANTERIORES 

previsores =[]
preco_real =[]

for i in range (90, 1242):
    previsores.append (base_treinamento_normalizada[i-90:i, 0])
    preco_real.append (base_treinamento_normalizada[i,0])

previsores,preco_real = np.array(previsores), np.array(preco_real)

#AGORA É PRECISO DEMONSTRAR QUAL O BATCH SIZE (PREVISORES.SHAPE [0]->QTD DE REGISTROS) O TIME_STEPS (NO CASO 90, PREVISORES.SHAPE[1])E O INPUT_DIMS->1 (OPENVALUE)

previsores = np.reshape(previsores, (previsores.shape[0], previsores.shape[1], 1))

rede_neural = Sequential ()
#UNITS->CELULAS DE MEMÓRIA, RETURN_SEQUENCES-> SEMPRE QUE PUVER OUTRA CAMADA
rede_neural.add (LSTM (units = 100,return_sequences = True, input_shape = (previsores.shape[1],1)))
rede_neural.add(Dropout(0.3))

rede_neural.add (LSTM (units = 50,return_sequences = True))
rede_neural.add(Dropout(0.3))

rede_neural.add (LSTM (units = 50,return_sequences = True))
rede_neural.add(Dropout(0.3))

rede_neural.add (LSTM (units = 50))
rede_neural.add(Dropout(0.3))

rede_neural.add (Dense (units = 1, activation = 'linear'))

rede_neural.compile (optimizer = 'rmsprop', loss = 'mean_squared_error',
                     metrics = ['mean_absolute_error'])
rede_neural.fit (previsores, preco_real, epochs = 100, batch_size = 32)


base_teste = pd.read_csv ('Petrobras_teste.csv')

preco_real_teste = base_teste.iloc[:,1:2].values

 #COMO O TREINAMENTO FOI FEITO A PARTIR DE 90 VALORES ANTERIORES, É NECESSÁRIO CONCATENAR AS DUAS BASES DE DADOS PARA ACESSAR OS VALORES DE ANTES 
 
base_completa = pd.concat((base['Open'], base_teste['Open']),axis = 0)
 
#PARA PREVER O PRIMEIRO VALOR DA BASE DE TESTE QUE ESTÁ NA BASE COMPLETA É PRECISO FAZER O SEGUINTE
#PEGAR OS 90 VALORES ANTES DO PRIMEIRO VALOR QUE DEVE SER TESTADO (112 registros )
entradas = base_completa[len(base_completa)-len(base_teste)-90:].values 
entradas = entradas.reshape (-1,1)
entradas = normalizador.transform (entradas)

X_teste =[]

for i in range (90,112):
    X_teste.append(entradas[i-90:i, 0])
    
X_teste = np.array(X_teste)
#AGORA É PRECISO DEMONSTRAR QUAL O BATCH SIZE (PREVISORES.SHAPE [0]->QTD DE REGISTROS) O TIME_STEPS (NO CASO 90, PREVISORES.SHAPE[1])E O INPUT_DIMS->1 (OPENVALUE)
X_teste = np.reshape(X_teste,(X_teste.shape[0],X_teste.shape[1],1))


#PREVISÕES E DESNORMALIZAÇÃO

previsoes = rede_neural.predict(X_teste)
previsoes = normalizador.inverse_transform (previsoes)


previsoes.mean ()
preco_real_teste.mean ()




plt.plot (preco_real_teste, color ='red', label = 'Preço real')
plt.plot (previsoes, color ='green', label = 'Previsões Rede Neural')
plt.title ('Previsões preço das ações')
plt.xlabel ('Tempo')
plt.ylabel ('Valor')
plt.legend()
plt.show ()




