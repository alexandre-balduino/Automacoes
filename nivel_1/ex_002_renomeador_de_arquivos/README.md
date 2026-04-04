# 🏷️ Renomeador Inteligente de Arquivos

## 🧠 Objetivo
Criar um script em Python capaz de renomear arquivos automaticamente com base em informações do próprio arquivo, como data de criação e numeração sequencial.

---

## ⚙️ Funcionalidades
- [x] Listar arquivos de um diretório
- [x] Filtrar arquivos por extensão (ex: `.jpg`)
- [x] Obter data de criação do arquivo
- [x] Gerar novo nome padronizado
- [x] Renomear arquivos automaticamente
- [ ] Evitar sobrescrita de arquivos
- [ ] Permitir múltiplos tipos de arquivo
- [ ] Escolher diretório via input

---

## 🧪 Tecnologias utilizadas
- Python 3
- Biblioteca `os`
- Biblioteca `datetime`

---

## ▶️ Como executar

1. Navegue até a pasta do exercício:

```bash
cd ex_002_renomeador_inteligente
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
├── IMG_8392.jpg
├── IMG_1023.jpg
├── IMG_5551.jpg
```

Depois da execução:

```Bash
pasta/
├── foto_2026-04-04_001.jpg
├── foto_2026-04-04_002.jpg
├── foto_2026-04-04_003.jpg
```

## 💡 Exemplo de saída

```Bash
Renomeando IMG_8392.jpg → foto_2026-04-04_001.jpg
Renomeando IMG_1023.jpg → foto_2026-04-04_002.jpg
Renomeando IMG_5551.jpg → foto_2026-04-04_003.jpg
```

## 🔧 Como funciona

* O script percorre os arquivos do diretório
* Filtra apenas arquivos com extensão desejada
* Obtém a data de criação de cada arquivo
* Formata a data no padrão YYYY-MM-DD
* Gera um novo nome com:
> * prefixo (foto)
> * data
> * número sequencial
* Renomeia os arquivos

---

## 🚀 Melhorias futuras

* Ordenar arquivos por data antes de renomear
* Adicionar prefixos personalizados
* Trabalhar com múltiplas extensões
* Criar interface interativa no terminal
* Gerar log das alterações em JSON

---

## 📌 Observações

* O script considera apenas arquivos (ignora pastas)
* A numeração é sequencial e baseada na ordem de execução
* Dependendo do sistema, a "data de criação" pode variar

---

## 🎯 Aprendizados

* Neste exercício foram praticados:
* Manipulação de arquivos com os
* Uso de timestamps e datas com datetime
* Automação de renomeação em lote
* Padronização de nomes de arquivos
