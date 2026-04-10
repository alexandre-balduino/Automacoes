
import os
import re
from datetime import datetime

def nome_valido(nome, prefixo, ext):
    ext = re.escape(ext)
    padrao = rf"^{prefixo}_\d{{4}}-\d{{2}}-\d{{2}}_\d{{3}}{ext}$"
    return re.match(padrao, nome) is not None


def renomear_arquivos(caminho, *formatos):
    """
    Renomeia arquivos de uma pasta
        
    Padrão:
        prefixo_data_numero.formato
        
    Exemplo:
        foto_2026-04-07_001.jpg
        
    Args:
        caminho (str): Pasta onde estão os arquivos
        formatos (str): Formato de arquivo que será renomeado
        
    Returns:
        None
    """
    
    # Formatos em minúsculo
    formatos = tuple(f.lower() for f in formatos)
    
    # Tipos de arquivo → prefixo
    tipos = {
        "foto": (".jpg", ".jpeg", ".png"),
        "audio": (".mp3",),
        "video": (".mp4",),
        "documento": (".txt", ".doc", ".docx", ".pdf")
    }

    # Lista de arquivos ordenados por data
    arquivos = [
        arq for arq in os.listdir(caminho)
        if os.path.isfile(os.path.join(caminho, arq))
    ]
    arquivos.sort(key=lambda x: os.path.getmtime(os.path.join(caminho, x)))

    contador = 1
    ultimo_dia = None

    for arq in arquivos:
        caminho_arquivo = os.path.join(caminho, arq)
        nome_arquivo = os.path.basename(caminho_arquivo)

        _, ext = os.path.splitext(nome_arquivo)
        ext = ext.lower()

        # Filtra pelos formatos desejados
        if ext not in formatos:
            continue

        # Descobre o prefixo automaticamente
        prefixo = None
        for tipo, exts in tipos.items():
            if ext in exts:
                prefixo = tipo
                break

        if prefixo is None:
            continue

        # Obtem a data do arquivo
        timestamp = os.path.getmtime(caminho_arquivo)
        data_obj = datetime.fromtimestamp(timestamp)
        data = data_obj.strftime("%Y-%m-%d")

        # Reseta contador por dia
        if data != ultimo_dia:
            contador = 1
            ultimo_dia = data

        # Pula se já estiver no padrão
        if nome_valido(nome_arquivo, prefixo, ext):
            print(f"Pulo (já organizado): {nome_arquivo}")
            continue

        # Gera novo nome
        novo_nome = f"{prefixo}_{data}_{contador:03d}{ext}"
        novo_caminho = os.path.join(caminho, novo_nome)

        # Evita conflito de nomes
        while os.path.exists(novo_caminho):
            contador += 1
            novo_nome = f"{prefixo}_{data}_{contador:03d}{ext}"
            novo_caminho = os.path.join(caminho, novo_nome)

        # Segurança extra
        if caminho_arquivo == novo_caminho:
            continue

        # Renomear
        try:
            os.rename(caminho_arquivo, novo_caminho)
        except Exception as e:
            print(f"Erro ao renomear {nome_arquivo}: {e}")
        else:
            print(f"Renomeando {nome_arquivo} -> {novo_nome}")
            contador += 1


pasta_alvo = os.path.join(os.path.dirname(__file__), "dados")

if __name__ == "__main__":
    renomear_arquivos(pasta_alvo, ".jpg", ".jpeg", ".png")
