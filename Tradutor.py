import tkinter as tk
import googletrans
from googletrans import Translator

def traduzir_texto():
    texto_original = texto_input.get("1.0", tk.END).strip()
    idioma_destino = idioma_selecionado.get()

    translator = Translator()
    traducao = translator.translate(texto_original, dest=idioma_destino)
    texto_traduzido.delete("1.0", tk.END)
    texto_traduzido.insert(tk.END, traducao.text)

# Configuração da janela principal
janela = tk.Tk()
janela.title("Tradutor")
janela.geometry("400x300")

# Rótulo e entrada de texto para o texto original
texto_label = tk.Label(janela, text="Texto original:")
texto_label.pack()

texto_input = tk.Text(janela, height=4)
texto_input.pack()

# Rótulo e caixa de seleção para o idioma de destino
idioma_label = tk.Label(janela, text="Idioma de destino:")
idioma_label.pack()

idiomas_disponiveis = googletrans.LANGUAGES
idioma_selecionado = tk.StringVar()
caixa_selecao = tk.OptionMenu(janela, idioma_selecionado, *idiomas_disponiveis.keys())
caixa_selecao.pack()

# Botão para realizar a tradução
traduzir_button = tk.Button(janela, text="Traduzir", command=traduzir_texto)
traduzir_button.pack()

# Rótulo e área de texto para o texto traduzido
texto_traduzido_label = tk.Label(janela, text="Texto traduzido:")
texto_traduzido_label.pack()

texto_traduzido = tk.Text(janela, height=4)
texto_traduzido.pack()

# Executa a janela principal
janela.mainloop()
