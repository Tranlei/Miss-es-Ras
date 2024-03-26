import cv2
import mediapipe as mp

video = cv2.VideoCapture(0)
palmo = mp.solutions.hands
pata = palmo.Hands(max_num_hands=1)
mpDwaw = mp.solutions.drawing_utils

while True:

    check, imagem = video.read()
    imgRGB = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
    processado = pata.process(imgRGB)
    Pontos_palmo = processado.multi_hand_landmarks
    altura, largura, _ = imagem.shape
    pontos = []

    if Pontos_palmo:

        for marcas in Pontos_palmo:

            mpDwaw.draw_landmarks(imagem, marcas, palmo.HAND_CONNECTIONS)

            for id, cord in enumerate(marcas.landmark):

                cordenada_x, cordenada_y = int(cord.x*largura), int(cord.y*altura)
                pontos.append((cordenada_x, cordenada_y))

        dedos = [8, 12, 16, 20]
        contador = 0

        if marcas:

            if pontos[4][0] > pontos[2][0]:

                contador += 1

            for x in dedos:

                if pontos[x][1] < pontos[x-2][1]:

                    contador += 1

        cv2.rectangle(imagem, (80, 10), (200, 100), (255, 0, 0), -1)
        cv2.putText(imagem, str(contador), (100, 100),cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 5)
        
    cv2.imshow("Contador de dedos", imagem)
    cv2.waitKey(1)