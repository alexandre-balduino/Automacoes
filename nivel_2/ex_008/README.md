
# 📜 Sistema de Logs com JSON

## 🧠 Objetivo
Criar um sistema em Python capaz de registrar e armazenar atividades em um arquivo JSON, permitindo o acompanhamento de ações realizadas pelo usuário.

---

## ⚙️ Funcionalidades
- [x] Registrar ações (ex: criação, exclusão, edição)
- [x] Salvar logs em arquivo `.json`
- [x] Listar histórico de atividades
- [x] Registrar data e hora de cada ação
- [ ] Filtrar logs por tipo de ação
- [ ] Limpar histórico de logs
- [ ] Exportar logs para `.txt`

---

## 🧪 Tecnologias utilizadas
- Python 3
- Biblioteca `json`
- Biblioteca `datetime`
- Biblioteca `os`

---

## ▶️ Como executar

1. Navegue até a pasta do exercício:

```bash
cd nivel_2/ex_008_logs_json
Execute o script:
Bash
python main.py
📂 Estrutura do projeto
Bash
ex_008_logs_json/
├── main.py
├── logs.json
└── README.md
💡 Exemplo de uso
Bash
[1] Registrar ação
[2] Ver logs
[3] Sair

Escolha uma opção: 1

Digite a ação: arquivo criado

✔ Log registrado com sucesso!
📄 Exemplo do arquivo JSON
JSON
[
  {
    "acao": "arquivo criado",
    "data": "2026-04-04 10:30:21"
  },
  {
    "acao": "arquivo deletado",
    "data": "2026-04-04 10:32:10"
  }
]
🔧 Como funciona
O programa verifica se o arquivo logs.json existe
Caso exista:
carrega os logs com json.load()
Caso não exista:
cria uma lista vazia
Ao registrar uma ação:
adiciona um dicionário com:
ação
data/hora atual
Salva os dados com json.dump()
🚀 Melhorias futuras
Filtrar logs por data
Filtrar por tipo de ação
Criar níveis de log (INFO, WARNING, ERROR)
Interface interativa mais avançada
Integração com outros projetos (ex: lixeira inteligente)
📌 Observações
Os logs são armazenados localmente em formato JSON
Cada ação registrada inclui data e hora
O arquivo cresce conforme novas ações são registradas
🎯 Aprendizados
Neste exercício foram praticados:
Uso de JSON para armazenamento de dados
Registro de eventos (logging)
Manipulação de datas com datetime
Estruturação de sistemas com histórico de ações