import cv2
import numpy as np
import os
from matplotlib import pyplot as plt


# def setSimilaridadeMinima():
#     print('informe a similaridade mínima desejada \n(mínima: 0.01 e máxima: 1.00)')
#     similaridade_minima = input()

#     return similaridade_minima


# def setQuantidadeObjetos():
#     print('informe a quantidade de objetos que deseja retornar \n(mínimo: 1)')
#     quantidade_objetos = input()

#     return quantidade_objetos


# def busca(query, similaridade_minima, quantidade_objetos):
#     similaridade_minima = setSimilaridadeMinima()
#     quantidade_objetos = setQuantidadeObjetos()
#     caminho_banco_de_imagens = 'imagem'
#     query = "serie_face_4.jpg"


#     # Quando o Template é uma imagem
#     if query.endswith(".jpg"):
#         template = cv2.imread(query, 0)
#         buscaImagem(query)

# def buscaImagem(template, base_dados):
#     w, h = template.shape[::-1]
#     methods = ['cv2.TM_CCOEFF_NORMED']

#     for meth in methods:
#         img = img2.copy()
#         method = eval(meth)
#         for arquivo in os.listdir(base_dados):
#             if arquivo.endswith(".jpg"):
#                 catual = "{}-CImagem".format(arquivo)
#                 img = cv2.imread('{}/{}'.format(base_dados, arquivo), 0)
#                 img2 = img.copy()
#                 buscaSimilaridade(img, template, method, meth)


# def buscaSimilaridade(img, template, method, meth, similaridade_minima):
#     res = cv2.matchTemplate(img,template,method)

#         #Recupera a similaridade entre o template e o conteúdo da Imagem de busca
#         min_val, similaridade, min_loc, max_loc = cv2.minMaxLoc(res)
#         texto = 'Similaridade com {0} entre Imagens é {1}%'.format(meth,round(similaridade*100,2))

#         resultado = []

#         if similaridade > similaridade_minima:
#             resultado.append((self.tatual, self.catual, similaridade))


# resultado = []


def ImagemOuVideo(arquivo):
    if arquivo.endswith('.jpg'):
        return True
    elif arquivo.endswith('.mp4'):
        return False


def percorreBancoDeImagens(template, similaridadeMinima):
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
                    aux = "{}-AFrame{}".format(arquivo, similaridade)
                    matches.append((aux, similaridade))
            # else:

    matches.sort(key=lambda x: x[1], reverse=True)

    print(*matches, sep='\n')


def afereSimilaridade(similaridadeMinima, img, template, method, meth):
    res = cv2.matchTemplate(img, template, method)

    # Recupera a similaridade entre o template e o conteúdo da Imagem de busca
    min_val, similaridade, min_loc, max_loc = cv2.minMaxLoc(res)
    texto = 'Similaridade com {0} entre Imagens é {1}%'.format(
        meth, round(similaridade*100, 2))
    return similaridade


def busca(arquivoTemplate, similaridadeMinima):

    if ImagemOuVideo(arquivoTemplate):
        template = cv2.imread(arquivoTemplate, 0)
        percorreBancoDeImagens(template, similaridadeMinima)

    # else:


arquivoTemplate = 'imagem/serie_face_4.jpg'
similaridadeMinima = 0.5

busca(arquivoTemplate, similaridadeMinima)
