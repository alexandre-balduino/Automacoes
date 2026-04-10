
import os
import re
import json
from datetime import datetime

def nome_valido(nome, prefixo, ext):
    """
    Verifica se um nome de arquivo já está no padrão esperado.

    O padrão considerado válido é:
        <prefixo>_YYYY-MM-DD_NNN.ext

    Exemplo:
        foto_2026-04-07_001.jpg

    Args:
        nome (str): Nome completo do arquivo (com extensão).
        prefixo (str): Prefixo esperado (ex: "foto", "video").
        ext (str): Extensão do arquivo (ex: ".jpg").

    Returns:
        bool: True se o nome estiver no padrão, False caso contrário.
    """
    ext = re.escape(ext)
    padrao = rf"^{prefixo}_\d{{4}}-\d{{2}}-\d{{2}}_\d{{3}}{ext}$"
    return re.match(padrao, nome) is not None


def renomear_arquivos(caminho, *formatos):
    """
    Renomeia arquivos em uma pasta com base na data de modificação.

    Os arquivos são renomeados seguindo o padrão:
        <prefixo>_YYYY-MM-DD_NNN.ext

    Onde:
        - prefixo é determinado automaticamente pelo tipo do arquivo
        - YYYY-MM-DD é a data de modificação do arquivo
        - NNN é um número sequencial por dia (001, 002, ...)

    Exemplo:
        foto_2026-04-07_001.jpg

    Funcionalidades:
        - Filtra arquivos pelos formatos informados
        - Identifica automaticamente o tipo do arquivo (foto, áudio, etc.)
        - Ordena os arquivos por data de modificação
        - Reinicia a numeração a cada novo dia
        - Evita sobrescrita de arquivos existentes
        - Ignora arquivos que já estão no padrão correto

    Args:
        caminho (str): Caminho da pasta contendo os arquivos.
        *formatos (str): Um ou mais formatos de arquivo (ex: ".jpg", ".png").

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
    
    log = []

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

        # Pula se já estiver no padrão
        if nome_valido(nome_arquivo, prefixo, ext):
            print(f"Pulo (já organizado): {nome_arquivo}")
            continue
        
        # Reseta contador por dia
        if data != ultimo_dia:
            contador = 1
            ultimo_dia = data

        # Gera novo nome
        novo_nome = f"{prefixo}_{data}_{contador:03d}{ext}"
        novo_caminho = os.path.join(caminho, novo_nome)

        # Evita conflito de nomes
        while os.path.exists(novo_caminho):
            contador += 1
            novo_nome = f"{prefixo}_{data}_{contador:03d}{ext}"
            novo_caminho = os.path.join(caminho, novo_nome)

        # Renomear
        try:
            os.rename(caminho_arquivo, novo_caminho)
        except Exception as e:
            print(f"Erro ao renomear {nome_arquivo}: {e}")
        else:
            print(f"Renomeando {nome_arquivo} -> {novo_nome}")
            contador += 1
            log.append({
                "antigo": caminho_arquivo,
                "novo": novo_caminho,
                "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
    caminho_log = os.path.join(os.path.dirname(__file__), "log.json")
    if os.path.exists(caminho_log):
        with open(caminho_log, "r") as f:
            log_existente = json.load(f)
    else:
        log_existente = []

    log_existente.extend(log)

    with open(caminho_log, "w") as f:
        json.dump(log_existente, f, indent=4, ensure_ascii=False)


def escolher_pasta(caminho_inicial=None):
    """
    Permite ao usuário navegar interativamente pelo sistema de arquivos
    via terminal para selecionar uma pasta.

    O usuário pode:
        - Digitar o número correspondente a um diretório para entrar nele
        - Digitar 'voltar' para subir um nível na hierarquia
        - Digitar 'escolher' para selecionar a pasta atual
        - Digitar 'sair' para cancelar a operação

    A navegação é feita a partir do diretório atual do programa
    (`os.getcwd()`), sendo possível explorar subpastas livremente.

    Returns:
        str | None:
            - Caminho absoluto da pasta selecionada, se confirmada
            - None, caso o usuário escolha sair
    """
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
            return None

        elif escolha == "voltar":
            novo_caminho = os.path.dirname(caminho_atual)

            # evita loop infinito na raiz
            if novo_caminho == caminho_atual:
                print("Você já está na raiz.")
            else:
                caminho_atual = novo_caminho

        elif escolha == "escolher":
            return caminho_atual

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

'''
pasta_alvo = os.path.join(os.path.dirname(__file__), "dados")
'''

if __name__ == "__main__":
    pasta_alvo = escolher_pasta()
    if pasta_alvo is not None:
        renomear_arquivos(pasta_alvo, ".jpg", ".jpeg", ".png")
