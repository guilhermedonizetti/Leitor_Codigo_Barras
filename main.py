import cv2
import streamlit as st
from functions import *
from time import time
from os import remove

st.title("LEITURA DE CÓDIGO DE BARRAS")

run = st.checkbox("Abrir câmera")

FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)
nome_arquivo = str(time()).replace(".", "_") + ".png"
parar = ""

botao_captura = st.button("CAPTURAR CÓDIGO")

if botao_captura == True:
    parar = 's'

while run:
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)

    retval, img = camera.read()
    cv2.imshow('Foto',img)
     
    if parar == "s" :
        cv2.imwrite(nome_arquivo, img)
        run = False
        conteudo = ler_codigo(nome_arquivo)
        preco_valor = ler_precificacao(conteudo)

        remove(nome_arquivo)

        st.success("PREÇO: R$ {}".format(preco_valor))

