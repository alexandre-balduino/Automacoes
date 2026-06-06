
import os
import readchar
from rich import print
from rich.panel import Panel

def select(*opcoes, msg="Selecione a opção", tam=32):
    pos = 0
    teclas_cima = (readchar.key.UP, "w", "\x1b[A")
    teclas_baixo = (readchar.key.DOWN, "s", "\x1b[B")
    teclas_enter = (readchar.key.ENTER, "\r", "\n")
    
    while True:
        os.system("clear")
        conteudo = ""
        for i, opcao in enumerate(opcoes):
            abert = "[black on white]" if i == pos else ""
            fecha = "[/]\n" if abert else "\n"
            conteudo += f"{abert} {opcao:<{tam-4}}{fecha}"
        menu = Panel(
            conteudo,
            title=msg,
            width=tam
        )
        print(menu)
        tecla = readchar.readkey()
        if tecla in teclas_cima:
            pos = (pos - 1) % len(opcoes)
        elif tecla in teclas_baixo:
            pos = (pos + 1) % len(opcoes)
        elif tecla in teclas_enter:
            return opcoes[pos]


def select_id(*opcoes, msg="Selecione a opção", tam=32):
    pos = 0
    teclas_cima = (readchar.key.UP, "w", "\x1b[A")
    teclas_baixo = (readchar.key.DOWN, "s", "\x1b[B")
    teclas_enter = (readchar.key.ENTER, "\r", "\n")
    
    while True:
        os.system("clear")
        conteudo = ""
        for i, opcao in enumerate(opcoes):
            abert = "[black on white]" if i == pos else ""
            fecha = "[/]\n" if abert else "\n"
            conteudo += f"{abert} {opcao['nome']:<{tam-4}}{fecha}"
        menu = Panel(
            conteudo,
            title=msg,
            width=tam
        )
        print(menu)
        tecla = readchar.readkey()
        if tecla in teclas_cima:
            pos = (pos - 1) % len(opcoes)
        elif tecla in teclas_baixo:
            pos = (pos + 1) % len(opcoes)
        elif tecla in teclas_enter:
            return opcoes[pos]["id"]
