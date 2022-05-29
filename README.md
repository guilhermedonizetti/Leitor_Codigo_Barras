<h1 align="center">Leitor de Código de Barras</h1>
<p align="center">Um programa para capturar e abstrair um código de barras padrão EAN13 :computer:<br>

<b>Objetivo: </b>Um programa que receba como entrada uma imagem de um código de barras EAN13 através de uma foto registrada no momento, e identifique o valor (💲) associado ao código.

<b>Desenvolvimento e Ferramentas:</b> criei uma interface onde o usuário pode abrir/fechar a câmera e capturar uma imagem, nessa interface deve aparecer a image registrada (foto do código de barras) e embaixo o valor associado a ele. Utilizei a biblioteca OpenCV para controle da câmera e Pyzbar para manipulação do código de barras. Todo o desenvolvimento foi realizado no ambiente Python! :snake:

<img align="center" src="https://github.com/guilhermedonizetti/Leitor_Codigo_Barras/blob/master/images/codigo_barras.png" >

O fluxo da execução é:
<ul>
  <li>Abrir câmera</li>
  <li>Registrar foto do código de barras</li>
  <li>Visualizar o valor ($) atribuído ao código</li>
</ul>
Se a imagem não for um código de barras, ou não for padrão EAN13, a resposta será "Não identificado".

<br><br>

<p align="center">
<b>Python, OpenCV, Streamlit, Pyzbar</b><br>Guilherme Donizetti - 2022.
</p>
