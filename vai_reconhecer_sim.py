import cv2 #Importando a biblioteca OPENCV
from cvzone.FaceDetectionModule import FaceDetector   # Importando cvzone

cap = cv2.VideoCapture(0) #Abrindo a camera 
detector = FaceDetector() #Usando a função face detector 

while True:
    sucess, img = cap.read() #Capturando a imagem
    img, bboxs = detector.findFaces(img) #Enviando a imagem para função que detecta rostos
    cv2.imshow("Video 1", img) #Cria uma janela com a palavra Video 1
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break
cv2.destroyAllWindows
