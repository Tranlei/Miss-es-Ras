import cv2
import mediapipe as mp

video = cv2.VideoCapture(0)

hands = mp.solutions.hands
Hand = hands.Hands(max_num_hands=1)
mpDwaw = mp.solutions.drawing_utils

while True:
    check, img = video.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = Hand.process(imgRGB)
    handsPoints = results.multi_hand_landmarks
    h, w, _ = img.shape
    pontos = []
    if handsPoints:
        for points in handsPoints:
            
            mpDwaw.draw_landmarks(img, points, hands.HAND_CONNECTIONS)

            for id, cord in enumerate(points.landmark):
                cx, cy = int(cord.x*w), int(cord.y*h)
                pontos.append((cx, cy))

        dedos = [8, 12, 16, 20]
        contador = 0
        if points:
            if pontos[4][0] > pontos[2][0]:
                contador += 1
            for x in dedos:
                if pontos[x][1] < pontos[x-2][1]:
                    contador += 1
        cv2.rectangle(img,(80,10),(200,100),(255,0,0),-1)
        cv2.putText(img,str(contador),(100,100),cv2.FONT_HERSHEY_SIMPLEX,4,(255,255,255),5)
    cv2.imshow("image", img)
    cv2.waitKey(1)