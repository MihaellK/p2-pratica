import cv2

# Carrega os classificadores em cascata
face_cascade = cv2.CascadeClassifier(
    filename=f"{cv2.data.haarcascades}/haarcascade_frontalface_default.xml"
)

frame = cv2.imread(filename="./saida/frames/frame0.jpg")
# gray_frame = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2GRAY)
# Passa o detector em cascata pelo método multi scale
# Esse método vai diminuindo a imagem a cada passada
# e testa o classificador em sequência
faces = face_cascade.detectMultiScale(
    image=frame, 
    scaleFactor=1.04, # Mudança de escala a cada passada
    minNeighbors=5, # Verifica os vizinhos antes de promover o ponto a ret
    maxSize=[50,50]
)
# Pega os dados do primeiro retangulo encontrado
x, y, w, h = faces[0]
# Desenha o retangulo
cv2.rectangle(
    img=frame,
    pt1=(x, y),
    pt2=(x+w, y+h),
    color=(0,0,255),
    thickness=2
)

# Exibe tudo
cv2.imshow('detecção facial', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()