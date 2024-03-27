#Importei as bibliotecas
import cv2
import mediapipe as mp
from cvzone.FaceDetectionModule import FaceDetector # Peguei apenas o FaceDetector da cvzone

detector = FaceDetector(minDetectionCon=0.5) # Criei a variável detector - com um limite de confiança para detectar a face

# Variáveis de configurações
video = cv2.VideoCapture(0)              # Cria um objeto de captura de vídeo que representa a câmera do computador. 
palmo = mp.solutions.hands               # palmo é o módulo de detecção de mãos.
pata = palmo.Hands(max_num_hands=1)      # pata é o objeto detector de mãos, apenas uma mão.
mpDwaw = mp.solutions.drawing_utils      # mpDraw é um módulo de utilitários para desenhar os resultados da detecção na imagem.

while True:                              # Laço infinito continuará capturando e processando frames da câmera.

    check, imagem = video.read()         # Lê um frame da câmera e armazena na variável imagem. 
    imagem,cord_face = detector.findFaces(imagem,draw=False) # Essa função vai encontra a face dentro da imagem
    imgRGB = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)  # Converte o frame de BGR (o padrão do OpenCV) para RGB.
    processado = pata.process(imgRGB)    # Processa o frame utilizando o modelo de detecção de mãos da MediaPipe.
    Pontos_palmo = processado.multi_hand_landmarks    # Extrai os pontos de referência das mãos detectadas no frame processado.
    altura, largura, _ = imagem.shape    # Obtêm as dimensões da imagem (altura e largura).
    pontos = []                          # Inicializa uma lista para armazenar os pontos de referência das mãos.

    if cord_face:                       # Esta condicional é verdadeira apenas se cord_face não estiver vazia.
        for bbox in cord_face:          # Percorrer as cordenadas da face e extraindo os Bounding boxes.
            cord_xx ,cord_yy, larguraa, alturaa = bbox['bbox'] # Buscando as coordenadas no dicionário retornado da 
                                                               #função   findFaces.
            recorte = imagem[cord_yy : cord_yy + alturaa, cord_xx : cord_xx + larguraa] # Extrair o recorte de onde está a face.
            recorte_borrado = cv2.blur(recorte,(30,30))                       # Borramos o recorte com a função blur e
                                                                              # definimos a matriz de vizinho.
            imagem[cord_yy : cord_yy + alturaa, cord_xx : cord_xx + larguraa] = recorte_borrado

    if Pontos_palmo:                     # Esta condicional é verdadeira apenas se Pontos_palmo não estiver vazia.

        for marcas in Pontos_palmo:      # loop percorre a variável Pontos_palmo e retornar as coordenadas para cada ponto.

           mpDwaw.draw_landmarks(imagem, marcas, palmo.HAND_CONNECTIONS)# Desenha os pontos de referência e as conexões da mão.

           for enumeracao, cord in enumerate(marcas.landmark):  # loop itera sobre cada ponto de referência (marcador) da mão.

                cordenada_x, cordenada_y = int(cord.x*largura), int(cord.y*altura)  # Converte as coordenadas normalizadas  
                                                                                    # dos  pontos de referência em coordenadas de pixels.
                pontos.append((cordenada_x, cordenada_y))   # Adiciona à lista de pontos.                

        dedos = [8, 12, 16, 20]           # inicializa uma lista com os índices dos pontos de referência dos dedos.
        contador = 0                      # Variável para contar o número de dedos estendidos.

        if marcas:                        # Esta condicional é verdadeira apenas se marcas não estiver vazia.

            if pontos[4][0] > pontos[2][0]: # Verifica se o dedo indicador está estendido comparando as coordenadas horizontais 
                                            # dos pontos de referência.
                contador += 1               # Se o dedo indicador estiver estendido, o contador é incrementado.

            for x in dedos:

                if pontos[x][1] < pontos[x-2][1]: # Verifica se os outros dedos estão estendido comparando as coordenadas 
                                                  # verticais dos pontos de referência.
                    contador += 1                 # Se o dedo indicador estiver estendido, o contador é incrementado.

        cv2.rectangle(imagem, (80, 10), (200, 100), (255, 0, 0), -1) # Desenha um retângulo azul na imagem
        cv2.putText(imagem, str(contador), (100, 100),cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 5) # Exibi o contador de 
                                                                                                       # dedos.
    cv2.imshow("Contador de dedos", imagem)  # Exibe o frame processado com o contador de dedos na janela com o título          
                                             # "Contador de dedos".
    cv2.waitKey(1)                           # Aguarda por 1 milissegundo antes de processar o próximo frame.

    if cv2.waitKey(1) & 0xFF == ord('q'):      # Pressionada a tecla "q" sai do loop, consequentemente fecho o "programa"
        break
