from chardet import detect
import cv2
import webbrowser


cap = cv2.VideoCapture(0)
dec = cv2.QRCodeDetector()
while True:
    _,img = cap.read()
    parse_data,one, _= dec.detectAndDecode(img)
    if parse_data:
        result = parse_data
        break
    cv2.imshow("QR Scanner", img)
    if cv2.waitKey(1) == ord("q"):
        break
web_open = webbrowser.open(result)
cap.release()
cv2.destroyAllWindows()