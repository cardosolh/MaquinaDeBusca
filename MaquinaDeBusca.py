import cv2
import numpy as np
import os
from matplotlib import pyplot as plt


def ImagemOuVideo(arquivo):
    extencoesVideo = set(['.mp4', '.avi', '.mpeg'])
    extencoesImagem = set(['.jpg', '.png', '.bmp'])
    if arquivo.endswith(tuple(extencoesImagem)):
        return True
    elif arquivo.endswith(tuple(extencoesVideo)):
        return False


def percorreBancoDeImagens(template, similaridadeMinima, quantidadeRetornos):
    bancoDeImagens = 'imagem'
    methods = ['cv2.TM_CCOEFF_NORMED']
    matches = []
    w, h = template.shape[::-1]

    for meth in methods:
        method = eval(meth)

        for arquivo in os.listdir(bancoDeImagens):
            if ImagemOuVideo(arquivo):
                img = cv2.imread('{}/{}'.format(bancoDeImagens, arquivo), 0)
                img2 = img.copy()
                similaridade = afereSimilaridade(
                    similaridadeMinima, img, template, method, meth)

                if similaridade >= similaridadeMinima:
                    aux = "Imagem: {} / Similaridade: {}".format(
                        arquivo, similaridade)
                    matches.append((aux, similaridade))

            else:
                cap = cv2.VideoCapture(
                    '{}/{}'.format(bancoDeImagens, arquivo), 0)
                i = 0
                while (cap.isOpened()):
                    ret, frame = cap.read()

                    if ret == True:
                        i += 1
                        nomeFrame = "{} / Frame: {}".format(arquivo, i)
                        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                        img = gray.copy()
                        similaridade = afereSimilaridade(
                            similaridadeMinima, img, template, method, meth)

                        if similaridade >= similaridadeMinima:
                            aux = "Video: {} / Similaridade: {}".format(
                                nomeFrame, similaridade)
                            matches.append((aux, similaridade))

                    else:
                        break

    # Ordena lista por similaridade
    matches.sort(key=lambda x: x[1], reverse=True)

    # Imprime lista
    print(*matches[:quantidadeRetornos], sep='\n')


def afereSimilaridade(similaridadeMinima, img, template, method, meth):
    res = cv2.matchTemplate(img, template, method)

    # Recupera a similaridade entre o template e o conteúdo da Imagem de busca
    min_val, similaridade, min_loc, max_loc = cv2.minMaxLoc(res)
    texto = 'Similaridade com {0} entre Imagens é {1}%'.format(
        meth, round(similaridade*100, 2))
    return similaridade


def busca(arquivoTemplate, similaridadeMinima, quantidadeRetornos):

    if ImagemOuVideo(arquivoTemplate):
        template = cv2.imread(arquivoTemplate, 0)
        percorreBancoDeImagens(
            template, similaridadeMinima, quantidadeRetornos)

    else:
        cap = cv2.VideoCapture(arquivoTemplate, 0)
        while (cap.isOpened()):
            ret, template = cap.read()
            if ret == True:
                gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
                img = gray.copy()
                percorreBancoDeImagens(
                    img, similaridadeMinima, quantidadeRetornos)


arquivoTemplate = 'HardhomeResume.mp4'
similaridadeMinima = 0.5
quantidadeRetornos = 15

busca(arquivoTemplate, similaridadeMinima, quantidadeRetornos)
