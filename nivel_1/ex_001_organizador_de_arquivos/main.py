
import os
import shutil
import logging


logging.basicConfig(
    filename=os.path.join(os.path.dirname(__file__), "log.txt"),
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    encoding="utf-8",
    force=True
)

def evitar_duplicados(caminho_destino):
    """
    Verifica se um arquivo já existe no destino e, se existir,
    gera um novo nome adicionando um contador.

    Exemplo:
        foto.jpg -> foto (1).jpg

    Args:
        caminho_destino (str): Caminho completo do arquivo de destino.

    Returns:
        str: Caminho final disponível (sem conflito de nome).
    """
    if not os.path.exists(caminho_destino):
        return caminho_destino
    else:
        pasta, nome_arquivo = os.path.split(caminho_destino)
        nome, ext = os.path.splitext(nome_arquivo)
        
        contador = 1
        
        while True:
            novo_nome = f"{nome} ({contador}){ext}"
            novo_caminho = os.path.join(pasta, novo_nome)
            
            if not os.path.exists(novo_caminho):
                return novo_caminho
            
            contador += 1


def organizar_pasta(caminho, destino=None):
    """
    Organiza arquivos de uma pasta em subpastas baseadas no tipo.

    Categorias:
        - imagens
        - audios
        - documentos
        - planilhas
        - videos
        - outros

    Args:
        caminho (str): Pasta onde estão os arquivos.
        destino (str, opcional): Pasta onde os arquivos serão organizados.
                                 Se None, usa o próprio caminho.

    Returns:
        None
    """
    if destino is None:
        destino = caminho
    
    # Dicionário com as pastas e as extensões equivalentes
    tipos = {
        "documentos": (".txt", ".pdf", ".doc", ".docx"),
        "planilhas": (".csv", ".ods", ".xls", ".xlsx"),
        "imagens": (".jpg", ".jpeg", ".png", ".gif"),
        "audios": (".mp3",),
        "videos": (".mp4",)
    }
    
    # Percorre todos os arquivos e pastas do caminho
    for arq in sorted(os.listdir(caminho)):
        # Caminho até o arquivo
        caminho_arquivo = os.path.join(caminho, arq)
        # Nome do arquivo
        nome_arquivo = os.path.basename(caminho_arquivo)
        
        # Verifica se é um arquivo
        if os.path.isfile(caminho_arquivo):
            # Pega a extensõo dos arquivos
            _, ext = os.path.splitext(nome_arquivo)
            ext = ext.lower()
            # Define a pasta destino padrão
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
            destino_final = os.path.join(pasta_final, nome_arquivo)
            destino_final = evitar_duplicados(destino_final)
            
            shutil.move(caminho_arquivo, destino_final)
            
            mensagem = f"{nome_arquivo} -> {pasta_destino }"
            _, nome_final = os.path.split(destino_final)
            if nome_final != nome_arquivo:
                mensagem += f"(renomeado para '{nome_final}')"
            print(mensagem)
            logging.info(mensagem)


pasta_alvo = os.path.join(os.path.dirname(__file__), "dados")

if __name__ == "__main__":
    organizar_pasta(pasta_alvo)
