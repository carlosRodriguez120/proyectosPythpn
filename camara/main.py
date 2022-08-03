import cv2, time

#1. Crear objeto
video=cv2.VideoCapture (0)
#3. Crear un objeto frame
check, frame =video.read ()
print (check)
print (frame) #representar la imagen
gray =cv2.cvtColor
#4. mostrar el frame
cv2.imshow ('Rubén', frame)
#5. par precionar cualquier tecla
cv2.waitKey (0)
#2. apagar la camara
video.release ()