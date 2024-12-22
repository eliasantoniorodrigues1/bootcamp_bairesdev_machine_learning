def treino(modelo,


           trainloader,


           device):


    # define a politca de atualização dos
otimizador = optim.SGD(modelo.parameters(), lr-0.01, momentum=0.5)
inicio = time()  # timer para sabermos quanto tempo levou o treino


e da bias


0s


pesos


criterio = nn.NLLLoss()  # definindo o criterio para calcular a perda
EPOCHS = 10  # numero de epochs que o algoritmo rodará
modelo.train()  # ativando o modo de treinamento do modelo


for epoch in range(EPOCHS):
perda_acumulada = 0  # inicialização da perda acumulada da epoch em questão


for imagens,


etiquetas in trainloader:


imagens = imagens.view(imagens.shape[0], -1)  # convertendo as imagens para
otimizador.zero_grad()  # zerando os gradientes por conta do ciclo anterior


"vetores"


de 28*28


casas


pal


com


output = modelo(imagens.to(device))  # colocando os dados no modelo
LA I
..
17
