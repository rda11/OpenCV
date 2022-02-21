import cv2

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 480)


for _ in range (10):
    _, frame = cam.read()
frame = cv2.resize(frame, (640, 480))
frame = cv2.flip(frame, 1)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray,(25,25),0)
last_frame = gray

#cv2.imshow("cam", gray)

while True:
    _, frame = cam.read()
    frame = cv2.resize(frame, (640, 480))
    frame = cv2.flip(frame, 1)


    gray2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.GaussianBlur(gray2, (25, 25), 0)
    #foreground = gray2 - gray
    abs_diff = cv2.absdiff(last_frame,gray2)
    last_frame = gray

    _, abs_mask = cv2.threshold(abs_diff,15,255,cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(abs_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour)<1000:
            continue

        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y),(x+w, y+h),(0, 0, 255), 2)

    cv2.imshow("cam", frame)
    cv2.imshow("motion_detection", abs_mask)


    if cv2.waitKey(1) == ord('q'):
        break




