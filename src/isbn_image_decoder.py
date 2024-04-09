import cv2

path = r"C:\Users\gusta\Pictures\barcode_00.jpg"

def img_to_code(path):

    img = cv2.imread(path)

    bd = cv2.barcode.BarcodeDetector()

    decoded_info = bd.detectAndDecode(img)

    return decoded_info[0]

isbn = img_to_code(path)

print(isbn)