# 🏷️ Renomeador Inteligente de Arquivos

## 🧠 Objetivo
Criar um script em Python capaz de renomear arquivos automaticamente com base em informações do próprio arquivo, como data de criação e numeração sequencial.

---

## ⚙️ Funcionalidades
- [x] Listar arquivos de um diretório
- [x] Filtrar arquivos por uma ou múltiplas extensões
- [x] Obter data de modificação do arquivo
- [x] Ordenar arquivos por data
- [x] Gerar novo nome padronizado
- [x] Renomear arquivos automaticamente
- [x] Evitar sobrescrita de arquivos
- [x] Permitir múltiplos tipos de arquivo
- [x] Resetar numeração por data
- [x] Escolher diretório via input
- [x] Gerar log das renomeações em arquivo JSON

---

## 📝 Log de alterações

O script gera automaticamente um arquivo `log.json` contendo o histórico das renomeações realizadas.

Cada entrada do log inclui:

- Caminho original do arquivo
- Novo caminho após renomeação
- Data e hora da operação

### Exemplo:

```json
[
  {
    "antigo": "/pasta/IMG_1234.jpg",
    "novo": "/pasta/foto_2026-04-10_001.jpg",
    "data": "2026-04-10 15:30:22"
  }
]
```

---

## 🧪 Tecnologias utilizadas
- Python 3
- Biblioteca `os`
- Biblioteca `re`
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
* Filtra arquivos com base nas extensões informadas
* Ordena os arquivos por data de modificação
* Obtém a data de cada arquivo
* Formata a data no padrão YYYY-MM-DD
* Define automaticamente o prefixo com base no tipo do arquivo
* Reinicia a numeração a cada nova data
* Gera um novo nome com:
> * prefixo (foto, audio, video, documento)
> * data
> * número sequencial
* Evita sobrescrever arquivos existentes
* Renomeia os arquivos

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
