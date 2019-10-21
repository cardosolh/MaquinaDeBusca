import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('imagem/serie.jpg', 0)
img2 = img.copy()
template = cv2.imread('imagem/serie_face_4.jpg', 0)
w, h = template.shape[::-1]

methods = ['cv2.TM_CCOEFF_NORMED']

for meth in methods:
    img = img2.copy()
    method = eval(meth)

    # Aplicando o template Matching
    res = cv2.matchTemplate(img, template, method)

    # Recupera a similaridade entre o template e o conteúdo da Imagem de busca
    min_val, similaridade, min_loc, max_loc = cv2.minMaxLoc(res)
    texto = 'Similaridade com {0} entre Imagens é {1}%'.format(
        meth, round(similaridade*100, 2))

    if similaridade > 0.55:
        plt.subplot(121), plt.imshow(template, cmap='gray')
        plt.title('Template'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(img, cmap='gray')
        plt.title('Imagem de Busca'), plt.xticks([]), plt.yticks([])
        plt.suptitle(meth)
        plt.show()
