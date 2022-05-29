from cv2 import imread
from pyzbar.pyzbar import decode

def ler_codigo(nome_imagem):
    codigo_barras = imread(nome_imagem)
    conteudo = decode(codigo_barras)
    print("\n\nCONTEUDO:\n{}".format(conteudo))
    print(conteudo)

    if len(conteudo) > 0:
        conteudo = (conteudo[0].data).decode("utf-8")
        return conteudo
    
    return "00"

def ler_precificacao(conteudo):
    conteudo = conteudo[:-1]
    preco = float(conteudo) / 100
    preco = "{:.2f}".format(preco)

    return float(preco)
