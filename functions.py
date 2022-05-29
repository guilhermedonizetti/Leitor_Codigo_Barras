from cv2 import imread
from pyzbar.pyzbar import decode

def ler_codigo(nome_imagem):
    codigo_barras = imread(nome_imagem)
    conteudo = decode(codigo_barras)
    conteudo = (conteudo[0].data).decode("utf-8")

    return conteudo

def ler_precificacao(conteudo):
    conteudo = conteudo[:-1]
    preco = float(conteudo) / 100
    preco = "{:.2f}".format(preco)

    return float(preco)
