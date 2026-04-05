# 📄 Função `open()` em Python

Guia prático para leitura e escrita de arquivos.

---

# 🔹 O que é `open()`?

A função `open()` é usada para **abrir arquivos** em Python, permitindo:

- Ler dados de arquivos
- Escrever dados em arquivos
- Criar arquivos

👉 Pense assim:
> `open()` cria uma conexão entre seu programa e um arquivo

---

# 🔹 Sintaxe básica

```python
arquivo = open("nome_do_arquivo.txt", "modo")
```

Exemplo:

```Python
f = open("dados.txt", "r")
```

# 🔹 Modos de abertura

### 📖 "r" — leitura (read)

Abre o arquivo para leitura

Dá erro se o arquivo não existir

```Python
open("dados.txt", "r")
```

### ✍️ "w" — escrita (write)

Cria o arquivo se não existir

Apaga todo o conteúdo existente ⚠️

```Python
open("dados.txt", "w")
```

### ➕ "a" — adicionar (append)

Adiciona conteúdo ao final do arquivo

Não apaga o conteúdo existente

```Python
open("dados.txt", "a")
```

### 🔄 "r+" — leitura e escrita

Permite ler e escrever no mesmo arquivo

### 📦 "b" — modo binário

Usado para arquivos como:
* imagens
* vídeos
* PDFs

```Python
open("imagem.jpg", "rb")
```

# 🔹 Leitura de arquivos

📌 Ler todo o conteúdo

```Python
with open("dados.txt", "r") as f:
    conteudo = f.read()
    print(conteudo)
```

📌 Ler linha por linha

```Python
with open("dados.txt", "r") as f:
    for linha in f:
        print(linha)
```

📌 Ler todas as linhas em lista

```Python
with open("dados.txt", "r") as f:
    linhas = f.readlines()
```

# 🔹 Escrita em arquivos

```Python
with open("dados.txt", "w") as f:
    f.write("Olá mundo\n")
    f.write("Nova linha")
```

# 🔹 Fechamento de arquivos

Forma manual:

```Python
f = open("dados.txt", "r")
f.close()
```

⚠️ Problemas se não fechar:

* vazamento de memória
* dados não salvos corretamente

# 🔹 Forma recomendada (profissional)

Use with:

```Python
with open("dados.txt", "r") as f:
    conteudo = f.read()
```

👉 Vantagens:

* Fecha automaticamente
* Mais seguro
* Padrão do mercado

# 🔹 Cursor do arquivo

O Python mantém um "cursor" que indica a posição de leitura.

Exemplo:

```Python
with open("dados.txt", "r") as f:
    print(f.read(5))  # lê os primeiros 5 caracteres
```

# 🔹 Codificação (encoding)

Para evitar erros com acentos:

```Python
with open("dados.txt", "r", encoding="utf-8") as f:
    print(f.read())
```

👉 Use sempre utf-8 no Brasil

# 🔹 Exemplos práticos

✔️ Criar log

```Python
with open("log.txt", "a") as f:
    f.write("Programa iniciado\n")
```

✔️ Processar linhas

```Python
with open("nomes.txt", "r") as f:
    for linha in f:
        print(linha.strip())
```

✔️ Copiar arquivo

```Python
with open("origem.txt", "r") as origem:
    with open("copia.txt", "w") as destino:
        destino.write(origem.read())
```

# 🔹 Tratamento de erros

```Python
try:
    with open("dados.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("Arquivo não encontrado")
```

# 🔥 Erros comuns

❌ Esquecer de fechar arquivo

❌ Usar "w" sem querer (apaga tudo)

❌ Não usar encoding

❌ Tentar abrir arquivo inexistente sem tratar erro

# 🔥 Resumo rápido
| Modo | Descrição |
| :--- | :--- |
| `"r"` | Ler |
| `"w"` | Escrever (apaga) |
| `"a"` | Adicionar |
| `"b"` | Binário |

# 💡 Dica final

* Sempre use `with open(...)`
* Use `utf-8` para evitar problemas
* Combine com `os` para automações
