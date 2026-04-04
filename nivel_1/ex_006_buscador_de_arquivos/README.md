# 🔎 Buscador de Arquivos

## 🧠 Objetivo
Criar um script em Python que permite buscar arquivos dentro de um diretório com base em nome ou extensão.

---

## ⚙️ Funcionalidades
- [x] Percorrer diretórios e subdiretórios
- [x] Buscar arquivos por nome
- [x] Buscar arquivos por extensão (ex: `.txt`, `.jpg`)
- [x] Exibir caminho completo dos arquivos encontrados
- [ ] Buscar conteúdo dentro dos arquivos
- [ ] Exportar resultados para arquivo `.txt`
- [ ] Interface interativa no terminal

---

## 🧪 Tecnologias utilizadas
- Python 3
- Biblioteca `os`

---

## ▶️ Como executar

1. Navegue até a pasta do exercício:

```bash
cd ex_006_buscador_arquivos
```

---

Execute o script:

```Bash
python main.py
```

---

## 💡 Exemplo de uso

```Bash
Digite o termo de busca: relatorio

Arquivos encontrados:
- /home/user/docs/relatorio.txt
- /home/user/downloads/relatorio_final.pdf
```

---

## 📂 Exemplo de busca por extensão

```Bash
Digite o termo de busca: .jpg

Arquivos encontrados:
- /imagens/foto1.jpg
- /downloads/imagem2.jpg
```

---

## 🔧 Como funciona

* O usuário informa um termo de busca
* O programa percorre os diretórios com os.walk()
* Compara o termo com o nome dos arquivos
* Exibe os resultados encontrados com caminho completo

---

## 🚀 Melhorias futuras

* Buscar conteúdo dentro de arquivos .txt
* Filtrar por tamanho de arquivo
* Filtrar por data de modificação
* Interface com menu interativo
* Criar versão com interface gráfica

---

## 📌 Observações

* A busca não diferencia maiúsculas e minúsculas (pode ser ajustado)
* O desempenho depende da quantidade de arquivos
* Ideal para diretórios organizados

---

## 🎯 Aprendizados

* Neste exercício foram praticados:
* Percorrer diretórios com os.walk
* Manipulação de caminhos de arquivos
* Busca e filtragem de dados
* Automação de tarefas de sistema
