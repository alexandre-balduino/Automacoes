# 🧹 Limpador de Arquivos Vazios

## 🧠 Objetivo
Criar um script em Python capaz de identificar e remover arquivos vazios (com 0 bytes) de um diretório, ajudando a manter o sistema organizado.

---

## ⚙️ Funcionalidades
- [x] Percorrer arquivos de uma pasta
- [x] Identificar arquivos com tamanho 0 bytes
- [x] Listar arquivos vazios encontrados
- [x] Permitir exclusão manual (com confirmação)
- [ ] Remover automaticamente arquivos vazios
- [ ] Gerar relatório das remoções
- [ ] Suporte a múltiplos diretórios

---

## 🧪 Tecnologias utilizadas
- Python 3
- Biblioteca `os`

---

## ▶️ Como executar

1. Navegue até a pasta do exercício:

```bash
cd ex_004_limpador_arquivos_vazios
```

2. Execute o script:

```Bash
python main.py
```

---

## 📂 Estrutura esperada

Antes da execução:

```Bash
pasta/
├── arquivo1.txt
├── vazio.txt
├── dados.csv
├── vazio2.log
```

Depois da execução:

```Bash
pasta/
├── arquivo1.txt
├── dados.csv
```
*(arquivos vazios removidos)*

---

## 💡 Exemplo de saída

```Bash
Arquivos vazios encontrados:
- vazio.txt
- vazio2.log

Deseja deletar esses arquivos? (s/n): s

Removendo vazio.txt...
Removendo vazio2.log...

✔ Limpeza concluída!
```

---

## 🔧 Como funciona

* O script percorre todos os arquivos do diretório
* Verifica o tamanho de cada arquivo com `os.path.getsize()`
* Identifica arquivos com tamanho igual a 0
* Exibe os arquivos encontrados
* Solicita confirmação do usuário
* Remove os arquivos selecionados

---

## 🚀 Melhorias futuras

* Remover arquivos automaticamente sem confirmação
* Criar logs das exclusões em JSON
* Permitir escolha do diretório via input
* Interface interativa no terminal
* Ignorar tipos específicos de arquivos

---

## 📌 Observações

* Apenas arquivos são considerados (pastas são ignoradas)
* A exclusão é permanente (não passa pela lixeira)
* Recomenda-se usar com cautela em diretórios importantes

---

## 🎯 Aprendizados

* Neste exercício foram praticados:
* Verificação de tamanho de arquivos
* Manipulação de arquivos com `os`
* Interação com usuário no terminal
* Automação de limpeza de diretórios