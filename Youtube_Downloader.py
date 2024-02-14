# Importando as bibliotecas necessárias
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from pytube import YouTube
from threading import Thread

# Função para baixar o vídeo
def baixar_video():
    # Obtendo a URL do campo de entrada
    url = url_entry.get()
    # Abrindo uma janela de diálogo para o usuário escolher o diretório de download
    save_path = filedialog.askdirectory()
    # Criando um objeto YouTube com a URL e a função de progresso
    yt = YouTube(url, on_progress_callback=progress_function)
    # Obtendo a stream selecionada pelo usuário
    stream = yt.streams.get_by_itag(int(quality_var.get().split(',')[0].strip(" '()")))  # Modifique esta linha
    # Baixando a stream para o diretório escolhido
    stream.download(save_path)
    # Limpando o campo de entrada
    url_entry.delete(0, 'end')
    # Informando ao usuário que o download foi concluído
    messagebox.showinfo("Download concluído", "O vídeo foi baixado com sucesso!")

# Função para atualizar a barra de progresso
def progress_function(stream, chunk, bytes_remaining):
    # Obtendo o tamanho total do arquivo
    size = stream.filesize
    # Calculando o progresso como uma porcentagem do tamanho total
    progress = (float(abs(bytes_remaining-size)/size))*float(100)
    # Atualizando a variável de progresso
    progress_var.set(progress)

# Criando a janela principal
root = tk.Tk()
root.title("Baixador de vídeos do YouTube Avançado")

# Adicionando um rótulo para o campo de entrada da URL
url_label = tk.Label(root, text="Insira o URL do vídeo:")
url_label.pack()

# Adicionando o campo de entrada da URL
url_entry = tk.Entry(root, width=50)
url_entry.pack()

# Adicionando um menu suspenso para selecionar a qualidade do vídeo
quality_var = tk.StringVar(root)
quality_var.set(("22", "MP4 720p"))  # Valor padrão
quality_menu = ttk.OptionMenu(root, quality_var, ("22", "MP4 720p"), ("18", "MP4 480p"), ("36", "3GP 240p"), ("17", "3GP 144p"))
quality_menu.pack()

# Adicionando o botão de download, que chama a função baixar_video em uma nova thread quando pressionado
download_button = tk.Button(root, text="Baixar", command=lambda: Thread(target=baixar_video).start())
download_button.pack()

# Criando a variável de progresso
progress_var = tk.DoubleVar()
# Adicionando a barra de progresso, que usa a variável de progresso para determinar seu preenchimento
progress_bar = ttk.Progressbar(root, length=200, variable=progress_var)
progress_bar.pack()

# Iniciando o loop principal da interface gráfica
root.mainloop()
