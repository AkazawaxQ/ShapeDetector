import cv2
import numpy as np

def detectColor(hsv, x, y):
    hue = hsv[y, x, 0]

    if 0 <= hue <= 15 or 160 <= hue <= 180:
        return "Red"
    elif 16 <= hue <= 34:
        return "Yellow"
    elif 35 <= hue <= 85:
        return "Green"
    elif 86 <= hue <= 110:
        return "Blue"
    elif 111 <= hue <= 179:
        return "Purple"
    else:
        return "Not Defined"

def detectShape(approx, area, peri):
    sides = len(approx)
    if sides == 3:
        return "Triangle"
    elif sides == 4:
        _, _, w, h = cv2.boundingRect(approx)
        aspectRatio = float(w) / h
        if 0.95 <= aspectRatio <= 1.05:
            return "Square"
        else:
            return "Rectangle"
    elif sides == 5:
        return "Pentagon"
    elif sides == 6:
        return "Hexagon"
    else:
        return "Circle"


def getContours(img, imgContour, hsv):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    height, width = imgContour.shape[:2]
    min_area = (height * width) * 0.001 
    cv2.putText(imgContour, '20MISY1035', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > min_area:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 255), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
            
            shape = detectShape(approx, area, peri)
            color = detectColor(hsv, x + w // 2, y + h // 2)
            
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(imgContour, f"{shape}, {color}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            cv2.putText(imgContour, f"Area: {int(area)}", (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            cv2.putText(imgContour, f"Perimeter: {int(peri)}", (x, y + h + 40), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)


cap = cv2.VideoCapture(0)

#frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#out = cv2.VideoWriter('Testing.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0, (frame_width, frame_height))

while True:
    ret, img = cap.read()
    if not ret:
        break

    imgContour = img.copy()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
    imgCanny = cv2.Canny(imgBlur, 50, 150)

    getContours(imgCanny, imgContour, imgHSV)

    cv2.imshow("Shape", imgContour)

#    out.write(imgContour)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
#out.release()
cv2.destroyAllWindows()
