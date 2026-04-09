
import os
import re
from datetime import datetime

def nome_valido(nome, prefixo, ext):
    padrao = rf"^{prefixo}_\d{{4}}-\d{{2}}-\d{{2}}_\d{{3}}{ext}$"
    return re.match(padrao, nome) is not None


def renomear_arquivos(caminho, formato):
    """
    Renomeia arquivos de uma pasta
        
    Padrão:
        prefixo_data_numero.formato
        
    Exemplo:
        foto_2026-04-07_001.jpg
        
    Args:
        caminho (str): Pasta onde estão os arquivos
        formato (str): Formato de arquivo que será renomeado
        
    Returns:
        None
    """
    
    # Define um contador
    contador = 1
    
    # Escolhe o prefixo com base na extensão do arquivo
    if formato in (".jpg", ".jpeg", ".png"):
        prefixo = "foto"
    elif formato in (".mp3",):
        prefixo = "audio"
    elif formato in (".mp4",):
        prefixo = "video"
    elif formato in (".txt", ".doc", ".docx", ".pdf"):
        prefixo = "documento"
    else:
        return
    
    # Lista de arquivos ordenados por data
    arquivos = [
        arq for arq in os.listdir(caminho)
        if os.path.isfile(os.path.join(caminho, arq))
    ]
    arquivos.sort(key=lambda x: os.path.getmtime(os.path.join(caminho, x)))
    
    # Percorre todos os arquivos e pastas
    for arq in arquivos:
        # Caminho completo até o arquivo
        caminho_arquivo = os.path.join(caminho,  arq)
        # Nome do arquivo
        nome_arquivo = os.path.basename(caminho_arquivo)
        # Pega a extensão dos arquivos
        _, ext = os.path.splitext(nome_arquivo)
        ext = ext.lower()
        
        # Obtem a data de criação
        timestamp = os.path.getmtime(caminho_arquivo)
        data_obj = datetime.fromtimestamp(timestamp)
        data = data_obj.strftime("%Y-%m-%d")
        
        # Se a extensão não for o formato desejado, vai para o próximo
        if ext != formato:
            continue
        
        # Se o nome atual do arquivo já estiver no padrão, pula para o próximo arquivo
        if nome_valido(nome_arquivo, prefixo, ext):
            continue
            
        # Define o novo nome
        novo_nome = f"{prefixo}_{data}_{contador:03d}{ext.lower()}"
        # Define o novo caminho
        novo_caminho = os.path.join(caminho, novo_nome)
                
        # Evita renomear um arquivo que já tem o nome esperado
        if caminho_arquivo == novo_caminho:
            continue
                
        # Renomear
        try:
            os.rename(caminho_arquivo, novo_caminho)
        except FileExistsError:
            print(f"Pulo: {novo_nome} já existe no diretório.")
        else:
            print(f"{nome_arquivo} -> {novo_nome}")
            contador += 1


pasta_alvo = os.path.join(os.path.dirname(__file__), "dados")

if __name__ == "__main__":
    renomear_arquivos(pasta_alvo, ".jp")
