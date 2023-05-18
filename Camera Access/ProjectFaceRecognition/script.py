import cv2

cap = cv2.VideoCapture(0)

if not(cap.isOpened()):
    print("Could not open Video Device")

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

while(True):
    ret, frame = cap.read()

    cv2.imshow('preview', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()