import cv2


def img_to_code(path):

    img = cv2.imread(path) #read image from source

    bd = cv2.barcode.BarcodeDetector() #run de detector e decode isbn

    decoded_info = bd.detectAndDecode(img) #save isbn decode as tuple

    return decoded_info[0] #select only the isbn number

x = r"C:\Users\gusta\OneDrive\Imagens\bcd01.jpg"
print(img_to_code(x))

