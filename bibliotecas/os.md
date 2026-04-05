
# 📂 Biblioteca `os` em Python

Guia prático para manipulação de arquivos e diretórios.

---

# 🔹 O que é a biblioteca `os`?

A biblioteca `os` permite interagir com o sistema operacional, como:

- Trabalhar com arquivos e pastas
- Navegar entre diretórios
- Criar, remover e organizar arquivos

---

# 🔹 Importação

```python
import os
```

# 🔹 Conceito de caminhos (paths)

## 📍 Caminho absoluto

Caminho completo desde a raiz:

```Python
"/home/user/arquivo.txt"
"/storage/emulated/0/Download/arquivo.txt"
```

## 📍 Caminho relativo

Baseado no diretório atual:

```Python
"arquivo.txt"
"pasta/arquivo.txt"
```

# 🔹 Diretório atual

```Python
os.getcwd()
```

👉 Retorna o diretório atual do programa

# 🔹 Mudar de diretório
```Python
os.chdir("nome_da_pasta")
```

Subir um nível:

```Python
os.chdir("..")
```

# 🔹 Listar arquivos e pastas

```Python
os.listdir()
```

Listar conteúdo de outra pasta:

```Python
os.listdir("Downloads")
```

# 🔹 Verificar existência

```Python
os.path.exists("arquivo.txt")
```

# 🔹 Verificar tipo

Arquivo:

```Python
os.path.isfile("arquivo.txt")
```

Pasta:
```Python
os.path.isdir("pasta")
```

# 🔹 Montar caminhos corretamente

❌ Errado:
```Python
caminho = "pasta/" + "arquivo.txt"
```

✅ Correto:

```Python
caminho = os.path.join("pasta", "arquivo.txt")
```

# 🔹 Separar partes do caminho

Nome do arquivo:

```Python
os.path.basename("/pasta/arquivo.txt")
```

Diretório:

```Python
os.path.dirname("/pasta/arquivo.txt")
```

# 🔹 Dividir o caminho

```Python
caminho = "/home/usuario/documentos/projeto.txt"
diretorio, arquivo = os.path.split(caminho)

print(f"Diretório: {diretorio}")
print(f"Arquivo: {arquivo}")
```

Resultado:

```Bash
Diretório: /home/usuario/documentos
​Arquivo: projeto.txt
```

# 🔹 Trabalhar com extensão de arquivo

```Python
nome, extensao = os.path.splitext("foto.jpg")
```

Resultado:

```Python
nome = "foto"
extensao = ".jpg"
```

# 🔹 Exemplo: listar apenas arquivos
```Python
import os

for item in os.listdir():
    if os.path.isfile(item):
        print(item)
```

# 🔹 Exemplo: listar apenas pastas

```Python
import os

for item in os.listdir():
    if os.path.isdir(item):
        print(item)
```

# 🔹 Exemplo: explorador simples

```Python
import os

while True:
    print("\nDiretório atual:", os.getcwd())

    arquivos = os.listdir()

    for i, item in enumerate(arquivos):
        print(f"[{i}] {item}")

    escolha = input("Digite o número (ou 'sair'): ")

    if escolha == "sair":
        break

    if escolha.isdigit():
        item = arquivos[int(escolha)]

        if os.path.isdir(item):
            os.chdir(item)
        else:
            print("Isso é um arquivo")
```


# 🔹 Renomear ou mover um arquivo

```Python
os.rename("arquivo_antigo.txt", "arquivo_novo.txt")
```


# 🔹 Pegar apenas a pasta de um arquivo

```Python
os.path.dirname(caminho)
```

Saída:

```
/pasta/subpasta
```

✔ Remove o arquivo

✔ Fica só o diretório

### 🔥 Uso muito comum

```Python
os.path.dirname(__file__)
```

👉 Isso retorna a pasta onde está o arquivo Python atual


# 🔹 Pegar apenas o arquivo

```Python
print(os.path.basename(caminho))
```

Saída:

```
arquivo.txt
```

✔ Remove o caminho

✔ Fica só o arquivo


# 🔹 Pegar o caminho absoluto

```Python
print(os.path.abspath(caminho))
```

Saída (exemplo):

```
/data/data/com.termux/files/home/pasta/subpasta/arquivo.txt
```

✔ Resolve caminho relativo

✔ Mostra o caminho real no sistema


# 🔥 Resumo rápido

| Função | Descrição |
| :--- | :---: |
| `os.getcwd()` | Diretório atual |
| `os.chdir()` | Mudar de pasta |
| `os.listdir()` | Listar arquivos |
| `os.path.exists()` | Verificar existência |
| `os.path.isfile()` | Verificar se é arquivo |
| `os.path.isdir()` | Verificar se é pasta |
| `os.path.join()` | Montar caminhos |
| `os.path.splitext()` | Separar extensão |
| `os.path.rename()` | Renomear ou mover um arquivo |
| `os.path.dirname()` | Diretório |
| `os.path.basename()` | Nome do arquivo |
| `os.path.abspath()` | Caminho completo |


# 🔹 Resumo mental

`os.getcwd()` → onde estou

`os.listdir()` → o que tem aqui

`os.chdir()` → ir para outro lugar

`os.path.exists()` → existe?

`os.path.isfile()` → é arquivo?

`os.path.isdir()` → é pasta?

`os.path.join()` → montar caminho

`os.path.splitext()` → pegar extensão

`os.rename()` → renomear ou mover

`os.path.dirname()` → diretório

`os.path.basename()` → nome do arquivo

`os.path.abspath()` → caminho completo
