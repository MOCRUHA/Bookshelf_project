import cv2

from pyzbar.pyzbar import decode

def img_to_code(path):

    dec = decode(cv2.imread(f'{path}'))

    return (dec[0].data.decode())
