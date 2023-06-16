import cv2

# guarda a captura do video nessa variavel
cap = cv2.VideoCapture("../assets/arsene.mp4")
while not cap.isOpened():

    cv2.waitKey(1000)


# define o proximo frame que sera capturado
pos_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)

# count zerado
count = 0

while True:
    # le o frame
    flag, frame = cap.read()
    if flag:
        # caso o frame ja tenha sido paturado
        cv2.imshow('video', frame)
        pos_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
        print (str(pos_frame)+" frames")
    else:
        # caso o proximo frame ainda n esteja pronto tenta ler novamente
        cap.set(cv2.CAP_PROP_POS_FRAMES, pos_frame-1)
        print ("frame is not ready")
        # aguarda
        cv2.waitKey(1000)

    # escreve o frame na pasta frames com o numero do frame na frente

    cv2.imwrite("./saida/frames/frame%d.jpg" % count, frame)
    count = count + 1

    if cv2.waitKey(10) == 27:
        break
    # Quando o numero de frames capturados é o mesmo da contagem total de frames o codigo para
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
    
        break