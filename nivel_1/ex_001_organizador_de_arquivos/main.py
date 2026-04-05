
import os
import shutil


def organizar_pasta(caminho, destino=None):
    if destino is None:
        destino = caminho
    
    tipos = {
        "documentos": (".txt", ".pdf", ".doc", ".docx"),
        "planilhas": (".csv", ".ods", ".xls", ".xlsx"),
        "imagens": (".jpg", ".jpeg", ".png", ".gif"),
        "audios": (".mp3"),
        "videos": (".mp4")
    }
    for arq in sorted(os.listdir(caminho)):
        caminho_arquivo = os.path.join(caminho, arq)
        nome_arquivo = os.path.basename(caminho_arquivo)
        # Verifica se é um arquivo
        if os.path.isfile(caminho_arquivo):
            # Pega a extensõo dos arquivos
            _, ext = os.path.splitext(nome_arquivo)
            # Define a pasta destino
            pasta_destino = "outros"
            # Descobre a categoria
            for pasta, extensoes in tipos.items():
                if ext in extensoes:
                    pasta_destino = pasta
                    break
            # Cria a pasta se não existir
            pasta_final = os.path.join(destino, pasta_destino)
            os.makedirs(pasta_final, exist_ok=True)
            # Move o arquivo
            print(f"Movendo {nome_arquivo} para {pasta_destino}/")
            shutil.move(caminho_arquivo, os.path.join(pasta_final, nome_arquivo))


pasta_alvo = os.path.join(os.path.dirname(__file__), "dados")
if __name__ == "__main__":
    organizar_pasta(pasta_alvo)
