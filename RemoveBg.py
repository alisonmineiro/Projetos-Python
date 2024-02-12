import tkinter as tk
from tkinter import filedialog, Canvas
from PIL import Image, ImageTk
from rembg import remove
import os

# Função para remover o fundo da imagem
def remove_background(image_path):
    image = Image.open(image_path)  # Carregar a imagem
    result = remove(image)  # Remover o fundo
    output_path = os.path.splitext(image_path)[0] + "_semfundo.png"
    result.save(output_path, 'PNG')  # Salvar a imagem
    return output_path

def select_image():
    global img_path
    img_path = filedialog.askopenfilename()
    load = Image.open(img_path)
    load = load.resize((200, 200), Image.ANTIALIAS)  # Redimensionar a imagem
    render = ImageTk.PhotoImage(load)
    canvas_orig.create_image(0, 0, anchor='nw', image=render)
    canvas_orig.image = render

def remove_bg():
    output_path = remove_background(img_path)
    load = Image.open(output_path)
    load = load.resize((200, 200), Image.ANTIALIAS)  # Redimensionar a imagem
    render = ImageTk.PhotoImage(load)
    canvas_no_bg.create_image(0, 0, anchor='nw', image=render)
    canvas_no_bg.image = render

root = tk.Tk()
root.geometry('500x500')

btn_rm = tk.Button(root, text="Remover fundo", command=remove_bg)
btn_rm.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")

btn = tk.Button(root, text="Selecionar imagem", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")

canvas_orig = Canvas(root, width=200, height=200)
canvas_orig.pack(side="left", padx="10", pady="10")

canvas_no_bg = Canvas(root, width=200, height=200)
canvas_no_bg.pack(side="right", padx="10", pady="10")

root.mainloop()
