import pyautogui as pag
import pandas as pd
from time import sleep

navegador = 'Navegador Opera GX'
linkDoSistema = r'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
email = 'exemplo@gmail.com'
senha = 'esqueciasenha'

pag.PAUSE = 0.2 # espera um tempo para executar o codigo seguinte

# abrir o operagx
pag.press('win')
pag.write(navegador)
pag.press('enter')
sleep(1)

# Clicar na parte de digitar o link e entrar no site
pag.hotkey('ctrl', 'l') # Ir para a barra de tarefas
pag.write(linkDoSistema)
pag.press('enter')

# esperar um tempo pra paginar carregar, em caso da conexão esta lenta
sleep(3)

# Fazer o login
campos = [email, senha]
pag.press('tab')
for campo in campos:
    pag.write(campo)
    pag.press('tab')

pag.press('enter')

sleep(3)

# Importar a base de dados dos produtos
tabela = pd.read_csv('AutomatizacaoPyautogui\produtos.csv')

for linha in tabela.index:
    pag.click(690, 201)
# preencher os campos
    dados = {
    'codigo': tabela.loc[linha, 'codigo'],
    'marca': tabela.loc[linha, 'marca'],
    'tipo': tabela.loc[linha, 'tipo'],
    'categoria': tabela.loc[linha, 'categoria'],
    'preco': tabela.loc[linha, 'preco_unitario'],
    'custo': tabela.loc[linha, 'custo'],
    'obs': tabela.loc[linha, 'obs']
    }
    
    for chave, valor in dados.items():
        if not pd.isna(valor):  # Verificar se o valor não é NaN
            pag.write(str(valor)) 
        pag.press('tab')
        
    # envio do produto
    pag.press('enter')
    pag.press('home') # volta para o topo da pagina caso ele de um scroll pra baixo