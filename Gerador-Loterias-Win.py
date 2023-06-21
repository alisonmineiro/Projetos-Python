import random
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Dicionário contendo as loterias disponíveis e suas respectivas configurações
# O primeiro valor da lista é a quantidade de números por aposta
# O segundo valor da lista é o maior número possível na aposta
loterias = {
    "Mega-Sena": [6, 60],
    "Quina": [5, 80],
    "Lotofácil": [15, 25],
    "Lotomania": [20, 100]
}

def gerar_aposta(loteria, quantidade):
    """
    Função para gerar apostas para uma determinada loteria.

    :param loteria: string contendo o nome da loteria
    :param quantidade: int contendo a quantidade de apostas a serem geradas
    :return: lista de listas contendo as apostas geradas
    """
    # Inicializa a lista de apostas
    numeros = []
    # Gera a quantidade especificada de apostas
    for i in range(quantidade):
        # Gera uma aposta aleatória e ordenada
        numeros.append(sorted(random.sample(range(1, loterias[loteria][1] + 1), loterias[loteria][0])))
    # Retorna a lista de apostas geradas
    return numeros

def salvar_apostas(loteria, apostas):
    """
    Função para salvar as apostas em um arquivo de texto.

    :param loteria: string contendo o nome da loteria
    :param apostas: lista de listas contendo as apostas a serem salvas
    """
    # Obtém o caminho do diretório onde o script está localizado
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Abre o arquivo de texto para escrita
    with open(os.path.join(script_dir, f"{loteria}.txt"), "w") as f:
        # Salva cada aposta no arquivo de texto
        for aposta in apostas:
            f.write(f"{aposta}\n")

def gerar_apostas():
    # Obtém a opção escolhida pelo usuário
    opcao = loteria_combobox.current()
    # Obtém o nome da loteria escolhida pelo usuário
    loteria = list(loterias.keys())[opcao]
    # Pergunta ao usuário quantas apostas ele deseja gerar
    quantidade = int(quantidade_entry.get())

    # Gera as apostas
    apostas = gerar_aposta(loteria, quantidade)
    # Salva as apostas em um arquivo de texto
    salvar_apostas(loteria, apostas)
    messagebox.showinfo("Apostas Geradas", f"Apostas geradas e salvas no arquivo {loteria}.txt")
    apostas_text.delete(1.0, END)
    # Exibe as apostas geradas na tela
    for aposta in apostas:
        apostas_text.insert(END, str(aposta) + "\n")

def sair():
    if messagebox.askyesno("Sair", "Deseja realmente sair?"):
        root.destroy()

# Cria a janela principal
root = Tk()
root.title("Gerador de Apostas")
root.geometry("400x300")

loteria_label = Label(root, text="Escolha uma loteria:")
loteria_label.pack()

# Cria uma combobox para selecionar a loteria
loteria_combobox = ttk.Combobox(root, values=list(loterias.keys()))
loteria_combobox.pack()

quantidade_label = Label(root, text="Quantidade de apostas:")
quantidade_label.pack()

# Cria uma entrada para inserir a quantidade de apostas
quantidade_entry = Entry(root)
quantidade_entry.pack()

gerar_button = Button(root, text="Gerar Apostas", command=gerar_apostas)
gerar_button.pack()

apostas_label = Label(root, text="Apostas geradas:")
apostas_label.pack()

# Cria uma área de texto para exibir as apostas geradas
apostas_text = Text(root)
apostas_text.pack()

sair_button = Button(root, text="Sair", command=sair)
sair_button.pack()

# Inicia o loop principal da interface gráfica
root.mainloop()
