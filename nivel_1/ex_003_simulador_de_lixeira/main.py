
import os
import shutil
from menu import select


diretorio_script = os.path.dirname(os.path.abspath(__file__))

def mover_para_lixeira(caminho_arquivo):
    caminho_lixeira = os.path.join(diretorio_script, "lixeira")
    os.makedirs(caminho_lixeira, exist_ok=True)
    
    nome_arquivo = os.path.basename(caminho_arquivo)
    destino_final = os.path.join(caminho_lixeira, nome_arquivo)
    
    shutil.move(caminho_arquivo, caminho_lixeira)

def excluir_permanentemente(arquivo):
    pass

def restaurar_da_lixeira(arquivo):
    pass

def menu_lixeira(caminho_lixeira=):
    caminho_lixeira = os.path.join(diretorio_script, "lixeira")
    os.makedirs(caminho_lixeira, exist_ok=True)
    os.chdir(caminho_lixeira)
    
    while True:
        caminho_atual = os.getcwd()
        
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
            caminho_item = os.path.join(caminho_atual, opcao)
            if os.path.isdir(caminho_item):
                os.chdir(caminho_item)
            else:
                sub_opcoes = ["ignorar", "restaurar", "excluir permanentemente"]
                sub_opcao = select(*sub_opcoes)
                
                if sub_opcao == "restaurar":
                    restaurar_da_lixeira()
                elif sub_opcao == "excluir permanentemente":
                    excluir_permanentemente()

def menu_arquivos(caminho_inicial=None):
    caminho_atual = caminho_inicial or diretorio_script
    os.chdir(caminho_atual)
    
    while True:
        caminho_atual = os.getcwd()
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
            caminho_item = os.path.join(caminho_atual, opcao)
            if os.path.isdir(caminho_item):
                os.chdir(caminho_item)
            else:
                sub_opcoes = ["ignorar", "mover para a lixeira", "excluir permanentemente"]
                sub_opcao = select(*sub_opcoes)
                
                if sub_opcao == "mover para a lixeira":
                    mover_para_lixeira(caminho_item)
                elif sub_opcao == "excluir permanentemente":
                    excluir_permanentemente()

def main():
    while True:
        menu = select(
            "Sair",
            "Escolher arquivos",
            "Ir para a lixeira"
        )
        
        if menu == "Sair":
            break
        elif menu == "Escolher arquivos":
            menu_arquivos(os.path.join(diretorio_script, "dados"))
        elif menu == "Ir para a Lixeira":
            menu_lixeira()

if __name__ == "__main__":
    main()