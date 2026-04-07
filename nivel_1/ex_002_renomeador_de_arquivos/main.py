
import os

def renomear_arquivos(caminho, formato):
    """
    Renomeia arquivos de uma pasta
        
    Padrão:
        prefixo_data_número-sequencial.formato
        
    Exemplo:
        foto_2026-04-07_001.jpg
        
    Args:
        caminho (str): Pasta onde estão os arquivos
        formato (str): Formato de arquivo que será renomeado
        
    Returns:
        None
    """
    prefixo = {
        "documento": (".txt", ".pdf", ".doc", ".docx"),
        "planilha": (".csv", ".ods", ".xls", ".xlsx"),
        "foto": (".jpg", ".jpeg", ".png", ".gif"),
        "audio": (".mp3",),
        "video": (".mp4",)
    }
    # Percorre todos os arquivos e pastas do caminho, ordenando por data
    for arq in sorted(os.listdir(caminho), key=lambda x: os.path.getctime(os.path.join(caminho, x))):
        # Caminho completo até o arquivo
        caminho_arquivo = os.path.join(caminho,  arq)
        # Nome do arquivo
        nome_arquivo = os.path.basename(caminho_arquivo)
        
        # Verifica se é um arquivo
        if os.path.isfile(caminho_arquivo):
            # Pega a extensão dos arquivos
            _, ext = os.path.splitext(nome_arquivo)
            ext = ext.lower()
            
            
            if ext == formato:
                print(arq)


pasta_alvo = os.path.join(os.path.dirname(__file__), "dados")

if __name__ == "__main__":
    renomear_arquivos(pasta_alvo, ".jpg")
