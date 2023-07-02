import cv2
import numpy as np
import glob     

out = cv2.VideoWriter('output_video.avi',cv2.VideoWriter_fourcc(*'DIVX'), 24, (1280,720))


for filename in glob.glob('./saida/frames/*.jpg'):
    img = cv2.imread(filename)
    out.write(img)


out.release()
# input_video.release()
cv2.destroyAllWindows()