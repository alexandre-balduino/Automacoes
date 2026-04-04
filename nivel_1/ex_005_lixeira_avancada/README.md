# 🗑️ Lixeira Inteligente com JSON

## 🧠 Objetivo
Criar uma versão avançada de uma lixeira de arquivos, capaz de armazenar o caminho original dos arquivos utilizando JSON, permitindo restaurá-los automaticamente para sua localização original.

---

## ⚙️ Funcionalidades
- [x] Enviar arquivos para a lixeira (mover arquivos)
- [x] Criar automaticamente a pasta `lixeira/`
- [x] Registrar caminho original dos arquivos em `.json`
- [x] Listar arquivos presentes na lixeira
- [x] Restaurar arquivos para o local original
- [x] Deletar arquivos permanentemente
- [ ] Evitar conflitos de nomes
- [ ] Sistema de confirmação para exclusão
- [ ] Log de operações

---

## 🧪 Tecnologias utilizadas
- Python 3
- Biblioteca `os`
- Biblioteca `shutil`
- Biblioteca `json`

---

## ▶️ Como executar

1. Navegue até a pasta do exercício:

```bash
cd ex_005_lixeira_inteligente
```

2. Execute o script:

```Bash
python main.py
```

---

## 📂 Estrutura do projeto

```Bash
ex_005_lixeira_inteligente/
├── main.py
├── lixeira/
├── dados.json
└── README.md
```

---

## 💡 Exemplo de uso

```Bash
[1] Enviar arquivo para lixeira
[2] Ver lixeira
[3] Restaurar arquivo
[4] Deletar permanentemente
[5] Sair
```

---

## 📄 Exemplo do arquivo JSON

```JSON
{
  "arquivo.txt": "/caminho/original/arquivo.txt",
  "foto.jpg": "/imagens/foto.jpg"
}
```

---
## 🔧 Como funciona

* Ao enviar um arquivo para a lixeira:
> * o arquivo é movido para a pasta /lixeira
> * seu caminho original é salvo no arquivo dados.json
* Ao restaurar um arquivo:
> * o programa consulta o JSON
> * move o arquivo de volta para o caminho original
* Ao deletar:
> * o arquivo é removido permanentemente
> * sua referência é removida do JSON

---

## 🚀 Melhorias futuras

* Evitar sobrescrever arquivos ao restaurar
* Criar nomes únicos automaticamente
* Interface mais amigável no terminal
* Histórico de ações (log)
* Suporte a múltiplos arquivos

---

## 📌 Observações

* A lixeira é simulada como uma pasta local
* O JSON é responsável por manter o controle dos caminhos originais
* Caso o JSON seja perdido, a restauração automática não será possível

## 🎯 Aprendizados

Neste exercício foram praticados:
* Manipulação de arquivos e diretórios
* Uso de json para persistência de dados
* Integração entre sistema de arquivos e dados estruturados
* Evolução de um sistema simples para um sistema mais completo
