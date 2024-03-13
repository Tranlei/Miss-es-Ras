import cv2 #Importa a biblioteca OpenCV para Python.

imagem = cv2.imread('fotos/Eita.jpg') #Carrega a imagem "Eita.jpg" do diretório "fotos" e armazena-a na variável imagem.

print('Largura em pixels: ', end='') #Imprime a string "Largura em pixels: " na tela.

print(imagem.shape[1]) #Imprime a largura da imagem, o valor da segunda dimensão da matriz imagem.shape.

print('Altura em pixels: ', end='') #Imprime a string "Altura em pixels: " na tela.

print(imagem.shape[0]) #Imprime a altura da imagem, o valor da primeira dimensão da matriz imagem.shape.

print('Qtde de canais: ', end='') #Imprime a string "Qtde de canais: " na tela.

print(imagem.shape[2]) #Imprime a quantidade de canais da imagem, o valor da terceira dimensão da matriz imagem.shape.

cv2.imshow("Nome da janela", imagem)
#Exibe a imagem em uma janela com o título "Nome da janela". A função imshow() exibe a imagem carregada.

cv2.waitKey(0) #Espera pressionar qualquer tecla
#Faz com que o programa espere até que qualquer tecla seja pressionada antes de continuar a execução.

cv2.imwrite("saida.jpg", imagem) #Salva a imagem carregada com o nome "saida.jpg" no disco. 
#A função imwrite() é usada para salvar a imagem.