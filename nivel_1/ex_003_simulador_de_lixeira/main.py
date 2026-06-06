
import os
import shutil
from menu import select


def menu_escolha(arquivo):
    pass

def mover_para_lixeira(arquivo):
    pass

def excluir_permanentemente(arquivo):
    pass

def restaurar_da_lixeira(arquivo):
    pass

def main(caminho_inicial=None):
    caminho_atual = caminho_inicial or os.getcwd()
    
    while True:
        print(f"\n📁 Diretório atual: {caminho_atual}")
        select(
            "sair",
            "voltar"
        )


if __name__ == "__main__":
    main()