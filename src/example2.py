import numpy as np
import cv2

def showImage(img):
    from matplotlib import pyplot as plt

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()

def getColor(img, x, y):
    return img.item(y, x, 0), img.item(y, x, 1), img.item(y, x, 2)


def setColor(img, x, y, b, g, r):
    img.itemset((y, x, 0), b)
    img.itemset((y, x, 1), g)
    img.itemset((y, x, 2), r)
    return img

def main():
    obj_img = cv2.imread("ada.jpg")
    altura, largura, canais_de_cor = obj_img.shape
    print("Dimensões da Imagem: " + str(largura) + "X" + str(altura))
    print("Canais de cor: ", canais_de_cor)

    for y in range(0, altura):
        for x in range(0, largura):
            #print("[" + str(x) + "," + str(y) + "] = " + str(obj_img[y][x]))
           # input()

            azul, verde, vermelho = getColor(obj_img, x, y)
            obj_img = setColor(obj_img, x, y, 0, 0, vermelho)


    showImage(obj_img)

main()
