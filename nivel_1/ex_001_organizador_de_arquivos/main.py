
import os
import shutil

# Define o caminho e entra na pasta
caminho_dados = os.path.join(os.path.dirname(__file__), "dados")
os.chdir(caminho_dados)

# Cria a pasta onde os dados serão organizados
os.makedirs("dados_organizados", exist_ok=True)

pastas_criadas = [] # Inicia uma lista vazia que conterá os nomes das pastas a serem criadas
# Percorre todos os arquivos e pastas no diretório atual
for arq in os.listdir():
    # Verifica se é um arquivo
    if os.path.isfile(arq):
        # Pega os nomes e extensões dos arquivos
        nome, ext = os.path.splitext(arq)
        # Se a extensão for de uma foto, adiciona "imagens" a lista pastas_criadas
        if ext.lower() in (".jpg", ".jpeg", ".png"):
            if "imagens" not in pastas_criadas:
                pastas_criadas.append("imagens")
        # Se a extensão for de um audio, adiciona "audios" a lista pastas_criadas
        elif ext.lower() in (".mp3"):
            if "audios" not in pastas_criadas:
                pastas_criadas.append("audios")
        # Se a extensão for de um arquivo de texto, adiciona "documentos" a lista pastas_criadas
        elif ext.lower() in (".pdf", ".txt"):
            if "documentos" not in pastas_criadas:
                pastas_criadas.append("documentos")
        # Se a extensão for de uma planilha, adiciona "planilhas" a lista pastas_criadas
        elif ext.lower() in (".xls", ".xlsx", ".csv", ".ods"):
            if "planilhas" not in pastas_criadas:
                pastas_criadas.append("planilhas")
        # Se a extensão for de um video, adiciona "videos" a lista pastas_criadas
        elif ext.lower() in (".mp4"):
            if "videos" not in pastas_criadas:
                pastas_criadas.append("videos")
        # Se for uma extensão diferente, adiciona "outros" a lista pastas_criadas
        else:
            if "outros" not in pastas_criadas:
                pastas_criadas.append("outros")

# Entra na pasta dados_organizados/
os.chdir("dados_organizados")
# Percorre a lista pastas_criadas
for p in pastas_criadas:
    # Se a pasta não existir
    if not os.path.exists(os.path.join(caminho_dados, "dados_organizados", p)):
        # Cria a pasta
        os.makedirs(p, exist_ok=True)
        print(f"pasta {p}/ criada com sucesso!")
    else:
        print(f"pasta {p}/ encontrada")
# Sai da pasta dados_organizados
os.chdir("..")

# Percorre os arquivos e pastas do diretório atual
for arq in os.listdir():
    # Se for um arquivo
    if os.path.isfile(arq):
        # Pega os nomes e extensões dos arquivos
        nome, ext = os.path.splitext(arq)
        # Se for uma imagem
        if ext.lower() in (".jpg", ".jpeg", ".png"):
            # Move para a pasta imagens/
            shutil.move(arq, os.path.join(caminho_dados, "dados_organizados", "imagens", arq))
        # Se a extensão for de um audio
        elif ext.lower() in (".mp3"):
            # Move para a pasta audios/
            shutil.move(arq, os.path.join(caminho_dados, "dados_organizados", "audios", arq))
        # Se a extensão for de um arquivo de texto
        elif ext.lower() in (".pdf", ".txt"):
            # Move para a pasta documentos/
            shutil.move(arq, os.path.join(caminho_dados, "dados_organizados", "documentos", arq))
        # Se a extensão for de uma planilha
        elif ext.lower() in (".xls", ".xlsx", ".csv", ".ods"):
            # Move para a pasta planilhas/
            shutil.move(arq, os.path.join(caminho_dados, "dados_organizados", "planilhas", arq))
        # Se a extensão for de um video
        elif ext.lower() in (".mp4"):
            # Move para a pasta videos/
            shutil.move(arq, os.path.join(caminho_dados, "dados_organizados", "videos", arq))
        # Se for uma extensão diferente
        else:
            # Move para a pasta outros/
            shutil.move(arq, os.path.join(caminho_dados, "dados_organizados", "outros", arq))
