import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Flatten, Dropout
from keras.utils import np_utils
from keras.layers import Conv2D, MaxPooling2D
from keras.layers.normalization import BatchNormalization

#A BASE DE DADOS MNIST JÁ VEM CARREGADA NO KERAS E DIVIDIDA EM TREINO E TESTE
(X_treinamento, y_treinamento), (X_teste, y_teste) = mnist.load_data ()

#VISUALIZAÇÃO DE UM REGISTRO EM UMA DETERMINADA BASE 

plt.imshow (X_treinamento [4])

#VISUALIZAÇÃO COM O TÍTULO DA CLASSE

plt.title ('Classe '+ str (y_treinamento[4]))

#MUDANÇA NOS DADOS PARA ADEQUAÇÃO AO TENSORFLOW E DEEFINIÇÃO DE 1 CANAL APENAS 

previsores_treinamento = X_treinamento.reshape (X_treinamento.shape[0], 28,28,1)

previsores_teste = X_teste.reshape (X_teste.shape[0], 28,28,1)

#É NECESSÁRIO QUE SEJA FEITA ESSA CONVERSÃO PARA FLOAT POIS ASSIM É POSSÍVEL DIVIDIR OS NÚMEROS POR 255
previsores_treinamento = previsores_treinamento.astype ('float32')
previsores_teste = previsores_teste.astype ('float32')

#NORMALIZAÇÃO DOS DADOS PARA FACILITAR O PROCESSAMENTO

previsores_treinamento /= 255
previsores_teste /= 255

#NECESSÁRIO FZER A CONVERSÃO DAS CLASSES PARA VARIÁVEIS DO TIPO DUMMY
classe_treinamento = np_utils.to_categorical (y_treinamento, 10)
classe_teste = np_utils.to_categorical (y_teste, 10)

#ETAPA 1 -> CONVOLUÇÃO (QTD DE KERNELS, TAMANHO DA MATRIZ E TAMANHO DA IMAGEM DE ENTRADA)

rede_neural = Sequential ()
rede_neural.add(Conv2D(32, (3,3), input_shape = (28,28,1), activation ='relu'))
rede_neural.add (BatchNormalization ()) #NORMALIZA OS VALORES DA MATRIZ PÓS CONVOLUÇÃO 

#ETAPA 2 -> POOLING (TAMANHO DA JANELA DE ANÁLISE)

rede_neural.add (MaxPooling2D (pool_size = (2,2)))

#ETAPA 3 -> FLATTEN (TRANSFORMAÇÃO EM VETOR )

 #rede_neural.add (Flatten ())

#MAIS UMA CAMADA DE TRATAMENTO DA IMAGEM (DEIXAR O FLATTEN SÓ POR ÚLTIMO)
rede_neural.add(Conv2D(32, (3,3), input_shape = (28,28,1),  activation ='relu'))
rede_neural.add (BatchNormalization ())
rede_neural.add (MaxPooling2D (pool_size = (2,2)))
rede_neural.add (Flatten())

#ETAPA 4-> REDE NEURAL (units colocar 128,256...)

rede_neural.add (Dense (units = 128,activation = 'relu'))
rede_neural.add (Dropout (0.2))
rede_neural.add (Dense (units = 128,activation = 'relu'))
rede_neural.add (Dropout (0.2))
rede_neural.add (Dense (units = 10,activation = 'softmax'))

rede_neural.compile(loss = 'categorical_crossentropy',
                    optimizer = 'adam', metrics = ['accuracy'])
rede_neural.fit(previsores_treinamento, classe_treinamento, batch_size = 128,
                epochs = 5, validation_data =  (previsores_teste, classe_teste))













