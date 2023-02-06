# importar o tkinter
from tkinter import *
from tkinter import ttk


# cores
cor1 = "#3b3b3b" # black/preta
cor2 = "#feffff" # white/branca
cor3 = "#38576b" # Azul carregado
cor4 = "#ECEFF1" # Cizenta
cor5 = "#FFAB40" # Orange/Laranja

janela = Tk()
janela.title("Calculadora")
janela.geometry("335x418")
janela.config(bg=cor1)

frame_tela = Frame(janela, width=335, height=50)
frame_tela.grid(row=0, column=0)

janela.mainloop()