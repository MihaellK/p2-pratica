import cv2

# Abre o arquivo de video
input_video = cv2.VideoCapture('../assets/arsene.mp4')

# Checa se foi possivel abrir o arquivo
if not input_video.isOpened():
    print("Error opening video file")
    exit(1)
    
# Como foi possível abrir o video de entrada, vamos agora utilizar 
# essa captura para definir o tamanho do video de saida
width  = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))   # float `width`
height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Cria a estrutura do video de saida
# Com formato e local do arquivo de saida
# Codec utilizado
# FPS do video e
# Tamanho do video
output_video = cv2.VideoWriter( './saida/out.avi',cv2.VideoWriter_fourcc(*'DIVX'), 24, (width, height))


count = 0

# Loop de leitura frame por frame
while True:
    # Le um frame do video e, guarda o resultado da leitura
    # Se nao houver mais frames disponiveis, ret sera falso
    ret, frame = input_video.read()

    # Se nao conseguiu ler o frame, para o laco
    if not ret:
        break


    # haarcascade
    face_cascade = cv2.CascadeClassifier(
        filename=f"{cv2.data.haarcascades}/haarcascade_frontalface_default.xml"
    )

    # Le o frame de numero igual a variavel count
    frame = cv2.imread(filename="./saida/frames/frame%d.jpg"%count)
    # escala de cinza
    gray_frame = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2GRAY)
    # add +1 ao count
    count +=1

    # Passa o detector em cascata pelo método multi scale
    # os parametros foram testados e escolhidos o de melhor resultado visto
    faces = face_cascade.detectMultiScale(
        image=gray_frame, 
        scaleFactor=1.25, # Mudança de escala a cada passada
        minNeighbors=6, # Verifica os vizinhos antes de promover o ponto a ret
        # minSize=[30,30],
        # Tamanhao maximo do retangulo para detecção
        # Foi setado esse valor por sem ele havia muito erro
        maxSize=[150,150] 
    )
    # Confere se no frame há alguma face
    if len(faces):
        # Armazena o valores desse retangulo
        x, y, w, h = faces[0]
        # Desenha o retangulo
        cv2.rectangle(
            img=frame,
            pt1=(x, y),
            pt2=(x+w, y+h),
            color=(0,0,255),
            thickness=2
        )
    # ==============



    # Exibe o frame
    cv2.imshow('Video Playback', frame)
    
    # Escreve o frame no output
    output_video.write(frame)

    # Se o usuario apertar q, encerra o playback
    # O valor utilizado no waiKey define o fps do playback
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
    
# Fecha tudo
output_video.release()
input_video.release()
cv2.destroyAllWindows()