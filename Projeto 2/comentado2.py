import cv2 # Importa a biblioteca OpenCV para Python, que será usada para manipulação de imagens.

# Carrega a imagem "Eita.jpg" do diretório "fotos" e armazena-a na variável imagem.
imagem = cv2.imread('fotos/Eita.jpg')

# Extrai os valores dos componentes de cor (azul, verde e vermelho) do primeiro pixel (0, 0) da imagem carregada.
(b, g, r) = imagem[0, 0] #veja que a ordem BGR e não RGB

# Imprimem na tela os valores dos componentes de cor do primeiro pixel da imagem, mostrando que a ordem dos canais é BGR.
print('O pixel (0, 0) tem as seguintes cores:')
print('Vermelho:', r, 'Verde:', g, 'Azul:', b)

# Percorrendo cada pixel da imagem e definem a cor de cada pixel como azul puro (255, 0, 0), alterando assim toda a imagem para a cor azul.
imagem = cv2.imread('fotos/Eita.jpg')
for y in range(0, imagem.shape[0]): #percorre linhas
 for x in range(0, imagem.shape[1]): #percorre colunas
    imagem[y, x] = (255,0,0)
cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)

# Percorrendo cada pixel da imagem e definem a cor de cada pixel com base nas coordenadas x e y do pixel, resultando em um padrão de cores que muda gradualmente com base na posição do pixel.
imagem = cv2.imread('fotos/Eita.jpg')
for y in range(0, imagem.shape[0]): #percorre linhas
 for x in range(0, imagem.shape[1]): #percorre colunas
    imagem[y, x] = (x%256,y%256,x%256)
cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)

# Percorrendo cada pixel da imagem e definem a cor de cada pixel com base no produto das coordenadas x e y do pixel, resultando em um padrão de cores que varia com base na posição dos pixels.
imagem = cv2.imread('fotos/Eita.jpg')
for y in range(0, imagem.shape[0], 1): #percorre as linhas
 for x in range(0, imagem.shape[1], 1): #percorre as colunas
    imagem[y, x] = (0,(x*y)%256,0)
cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)

# Percorrem a imagem em incrementos de 10 pixels e definem a cor de uma região de 5x5 pixels em amarelo (255, 255, 0) em cada posição percorrida.
imagem = cv2.imread('fotos/Eita.jpg')
for y in range(0, imagem.shape[0], 10): #percorre linhas
 for x in range(0, imagem.shape[1], 10): #percorre colunas
    imagem[y:y+5, x: x+5] = (0,255,255)

# Exibe a imagem modificada em uma janela com o título "Imagem modificada" e espera até que uma tecla seja pressionada antes de continuar a execução do programa.
cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)