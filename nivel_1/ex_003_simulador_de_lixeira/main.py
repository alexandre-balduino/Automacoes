
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
        
        opcoes = ["sair", "voltar"]
        arquivos = os.listdir()
        arquivos.sort()
        opcoes.extend(arquivos)
        
        opcao = select(
            *opcoes
        )
        
        if opcao == "sair":
            break
        elif opcao == "voltar":
            os.chdir("..")
        else:
            if os.path.isdir(opcao):
                os.chdir(opcao)
            else:
                opcoes = ["ignorar", "mover para a lixeira", "excluir permanentemente"]
                opcao = select(*opcoes)


if __name__ == "__main__":
    main()