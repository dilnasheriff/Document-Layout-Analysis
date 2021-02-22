from scanner import ExtractImage
import cv2
import imutils



image=cv2.imread('card28.jpg')
ratio = image.shape[0] / 500.0
original=image.copy()
image=imutils.resize(image, height = 500)
img=ExtractImage(image,ratio,original)
edged=img.canny_edge_detector()
img.contouring(edged)
img.transformed()

