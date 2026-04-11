
import os
import shutil

'''
def mover_para_lixeira(arquivo)

def listar_arquivos(arquivo)

def restaurar_arquivo(arquivo)
'''

def menu(caminho_inicial=None):
    caminho_atual = caminho_inicial or os.getcwd()
    
    while True:
        print(f"\n📁 Diretório atual: {caminho_atual}")

        try:
            itens = [i for i in os.listdir(caminho_atual) if not i.startswith(".")]
        except PermissionError:
            print("Sem permissão para acessar essa pasta.")
            caminho_atual = os.path.dirname(caminho_atual)
            continue

        itens.sort()
        
        for i, item in enumerate(itens):
            print(f"[{i}] {item}")

        escolha = input("\nDigite o número (ou 'sair', 'voltar', 'escolher'): ").strip().lower()

        if escolha == "sair":
            break

        elif escolha == "voltar":
            novo_caminho = os.path.dirname(caminho_atual)

            # evita loop infinito na raiz
            if novo_caminho == caminho_atual:
                print("Você já está na raiz.")
            else:
                caminho_atual = novo_caminho

        elif escolha.isdigit():
            indice = int(escolha)

            if indice < 0 or indice >= len(itens):
                print("Índice inválido.")
                continue

            selecionado = os.path.join(caminho_atual, itens[indice])

            if os.path.isdir(selecionado):
                caminho_atual = selecionado
            else:
                print("Isso é um arquivo.")

        else:
            print("Entrada inválida.")



menu()