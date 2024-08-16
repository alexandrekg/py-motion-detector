import cv2

cap = cv2.VideoCapture(0)


if not cap.isOpened():
    print('Ops, aconteceu um erro e a camera não está ligada!')
    exit()


while True:
    ret, frame = cap.read()
    if not ret:
        print('Failed to grab frame')
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    cv2.imshow('Grayscale Webcam', gray_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
# import opencv

# ligar a camera do notebook e mostrar algo

# capturar movimentos
