# Passo a passo do projeto

# Passo 1 - Entrar no sistema da empresa
    # # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time


# Passo 5 - Repetir isso até acabar a base de dados

# Deixar a automação mais lenta 
pyautogui.PAUSE = 2
# apertar a tecla do Windows (command + Barra de espaço)
pyautogui.press("win")
# Dugitar o nome do programa (chrome)
pyautogui.write('chrome')
# apertar enter
pyautogui.press("enter")
# digitar o link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
# apertar enter
pyautogui.press("enter")

# espera 5 segundos
time.sleep(4)

# Passo 2 - Fazer login
pyautogui.click(x=832, y=556)

# digitar o e-mail
pyautogui.write("acesso@acesso.com.br")
# passar para o campo de senha 
pyautogui.press("tab")   
# digitar senha
pyautogui.write("senha!@#$P!73r")

pyautogui.click(x=898, y=818)
time.sleep(1)

# Passo 3 - Importar a base de dados
# pip install pandas numpy openyxl
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:

    # Passo 4  - Cadastrar um produto
    pyautogui.click(x=942, y=376)
    # Digitar código do produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    # Digitar a marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    # Digitar Tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    # preco
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    # obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)  
    # enviar o produto 
    pyautogui.press("tab")
    pyautogui.press("enter")       
    pyautogui.click(x=844, y=612)

    pyautogui.scroll(5000)


    
