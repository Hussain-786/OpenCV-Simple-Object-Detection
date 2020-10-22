import cv2

img = cv2.imread('shape.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(imgray, 210, 255, cv2.THRESH_BINARY)
contours,_ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [approx], 0, (0,0,0), 5)
    x1= approx.ravel()[0]
    y1= approx.ravel()[1] - 10
    if len(approx) == 3:
        cv2.putText(img, 'Triangle', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
    elif len(approx) == 4:
        x,y,w,h = cv2.boundingRect(approx)
        aspectRatio = float(w)/h
        print(aspectRatio)
        if aspectRatio>=0.95 and aspectRatio<=1.05:
            cv2.putText(img, 'Square', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
        else:
            cv2.putText ( img, 'Rectangle', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
    elif len(approx) == 5:
        cv2.putText(img, 'Pentagon', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
    elif len(approx) == 10:
        cv2.putText(img, 'Star', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
    else:
        cv2.putText(img, 'Circle', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()