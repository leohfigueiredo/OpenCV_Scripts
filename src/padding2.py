import numpy as np
import cv2
from matplotlib import pyplot as plt

def showImageGrid(img2, title):
    fig, axis = plt.subplots()
    imgMPLIB = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    axis.imshow(imgMPLIB)
    axis.set_title(title)
    plt.show()

def plotTwoImageHorizontal():
    imgOriginal = cv2.imread("ada.jpg")
    imgReplicate = cv2.copyMakeBorder(imgOriginal, 200, 100, 50, 25, cv2.BORDER_REPLICATE)

def main2():
    img2 = cv2.imread("ada.jpg")
    showImageGrid(img2, "Foto da Ada")
    plt.imshow(img2)
    plt.show()

main2()
