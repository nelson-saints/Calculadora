import tkinter as tk


cor1 = "#3b3b3b" # black/preta
cor2 = "#feffff" # white/branca
cor3 = "#38576b" # Azul carregado
cor4 = "#ECEFF1" # Cizenta
cor5 = "#FFAB40" # Orange/Laranja


def janela() -> tk.TK:
    janela.title("Calculadora")
    janela.geometry("235x310")
    janela.config(bg=cor1)