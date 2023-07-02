# Parte prática da prova 2 do módulo 6 de Engenharia de Computação

## Enunciado

Para o funcionamento correto do codigo acima, primeiro instale a lib do open cv e depois rode os 2 scripts na sequencia

### retira_frames

Nesse script, primeiramente é feito a leitura de cada frame do video e armazenado na pasta "saida/frames/". Não subi os frames retirados para facilitar, por isso ela atualmente esta apenas com um txt vazio

### edita_video

Nesse script lemos cada frame que retiramos previamente e rodamos o algortimo Haar Cascade do opencv. Foi modificado alguns parametros para que acerte o maior numero de frames possiveis, ````scaleFactor=1.25, minNeighbors=6 e maxSize=[150,150]````, esse ultimo parametro diminui a quantidade de quadrados vazios achados, garantido que apenas retangulos pequenos sejam validos, suficiente para os rostos. 
Para previnir erros de faces não encontradas, apenas desenhamos eles se o tamanha do array de faces for maior que 0 ```if len(faces):```

No final todos os frames são convertidos em um unido video que se encontra na pasta __saida__



