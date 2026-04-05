
import os
import shutil


def organizar_pasta(caminho, destino=os.path.dirname(__file__)):
    for arq in os.listdir(caminho):
        caminho_arquivo = os.path.join(caminho, arq)
        nome_arquivo = os.path.basename(caminho_arquivo)
        # Verifica se é um arquivo
        if os.path.isfile(caminho_arquivo):
            # Pega os nomes e extensões dos arquivos
            nome, ext = os.path.splitext(nome_arquivo)
            # Verifica se é uma foto
            if ext.lower() in (".jpg", ".jpeg", ".png"):
                # Cria a pasta imagens/ caso não exista
                os.makedirs(os.path.join(destino, "imagens"), exist_ok=True)
                # Move o arquivo para a pasta imagens/
                print(f"Movendo {nome_arquivo} para imagens/")
                shutil.move(caminho_arquivo, os.path.join(destino, "imagens", nome_arquivo))
            # Verifica se é um audio
            elif ext.lower() in (".mp3"):
                # Cria a pasta audios/ caso não exista
                os.makedirs(os.path.join(destino, "audios"), exist_ok=True)
                # Move o arquivo para a pasta audios/
                print(f"Movendo {nome_arquivo} para audios/")
                shutil.move(caminho_arquivo, os.path.join(destino, "audios", nome_arquivo))
            # Verifica se é um arquivo de texto
            elif ext.lower() in (".pdf", ".txt", ".doc", ".docx"):
                # Cria a pasta documentos/ caso não exista
                os.makedirs(os.path.join(destino, "documentos"), exist_ok=True)
                # Move o arquivo para a pasta imagens/
                print(f"Movendo {nome_arquivo} para documentos/")
                shutil.move(caminho_arquivo, os.path.join(destino, "documentos", nome_arquivo))
            # Verifica se é uma planilha
            elif ext.lower() in (".xls", ".xlsx", ".csv", ".ods"):
                # Cria a pasta planilhas/ caso não exista
                os.makedirs(os.path.join(destino, "planilhas"), exist_ok=True)
                # Move o arquivo para a pasta planilhas/
                print(f"Movendo {nome_arquivo} para planilhas/")
                shutil.move(caminho_arquivo, os.path.join(destino, "planilhas", nome_arquivo))
            # Verifica se é um vídeo
            elif ext.lower() in (".mp4"):
                # Cria a pasta videos/ caso não exista
                os.makedirs(os.path.join(destino, "videos"), exist_ok=True)
                # Move o arquivo para a pasta videos/
                print(f"Movendo {nome_arquivo} para videos/")
                shutil.move(caminho_arquivo, os.path.join(destino, "videos", nome_arquivo))
            # Se for um arquivo diferente
            else:
                # Cria a pasta outros/ caso não exista
                os.makedirs(os.path.join(destino, "outros"), exist_ok=True)
                # Move o arquivo para a pasta outros/
                print(f"Movendo {nome_arquivo} para outros/")
                shutil.move(caminho_arquivo, os.path.join(destino, "outros", nome_arquivo))


pasta_alvo = os.path.join(os.path.dirname(__file__), "dados")
organizar_pasta(pasta_alvo, pasta_alvo)
