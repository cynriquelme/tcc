import cv2
from pyzbar.pyzbar import decode
from PIL import Image

d = decode(Image.open("registers/qrprueba.png"))
print(d[0].data.decode("ascii"))