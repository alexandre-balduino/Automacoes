
# 💰📊 Sistema Financeiro Integrado (JSON + Relatórios)

## 🧠 Objetivo
Criar um sistema que utilize dados financeiros armazenados em JSON para gerar relatórios automáticos, consolidando informações como saldo, totais e estatísticas.

---

## ⚙️ Funcionalidades
- [x] Ler transações de um arquivo `.json`
- [x] Separar receitas e despesas
- [x] Calcular:
  - total de receitas
  - total de despesas
  - saldo final
- [x] Gerar relatório automático em `.txt`
- [x] Exibir resumo no terminal
- [ ] Filtrar por data
- [ ] Filtrar por categoria
- [ ] Exportar para `.csv`
- [ ] Interface interativa

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
cd nivel_3/ex_015_sistema_financeiro_integrado
Execute o script:
Bash
python main.py
📂 Estrutura do projeto
Bash
ex_015_sistema_financeiro_integrado/
├── main.py
├── dados.json
├── relatorios/
└── README.md
📄 Exemplo de dados.json
JSON
[
  {
    "id": 1,
    "descricao": "Salário",
    "valor": 2500.0,
    "tipo": "receita",
    "data": "2026-04-04"
  },
  {
    "id": 2,
    "descricao": "Mercado",
    "valor": 150.0,
    "tipo": "despesa",
    "data": "2026-04-04"
  },
  {
    "id": 3,
    "descricao": "Freelance",
    "valor": 800.0,
    "tipo": "receita",
    "data": "2026-04-04"
  }
]
💡 Exemplo de saída no terminal
Bash
--- RESUMO FINANCEIRO ---

Total de receitas: R$ 3300.00
Total de despesas: R$ 150.00
Saldo final: R$ 3150.00
📄 Exemplo de relatório gerado
Plain text
RELATÓRIO FINANCEIRO

Data: 2026-04-04 10:45

Total de receitas: R$ 3300.00
Total de despesas: R$ 150.00
Saldo final: R$ 3150.00

Quantidade de transações: 3
🔧 Como funciona
O programa lê o arquivo dados.json
Percorre todas as transações
Separa:
receitas (tipo == "receita")
despesas (tipo == "despesa")
Calcula:
total de receitas
total de despesas
saldo final
Exibe um resumo no terminal
Gera um relatório .txt automaticamente
⚠️ Cuidados importantes
Validar estrutura do JSON
Garantir que valores sejam numéricos
Tratar arquivo inexistente
Criar pasta de relatórios automaticamente
Evitar erros com listas vazias
🚀 Melhorias futuras
Filtro por período (mensal, semanal)
Categorias (alimentação, transporte, etc.)
Gráficos de gastos
Interface gráfica (KivyMD)
Integração com Google Sheets
Integração com WhatsApp (Meta AI 👀)
Múltiplos usuários
📌 Observações
Esse projeto é uma base real para sistemas financeiros
Pode evoluir diretamente para seu ZapBudget
Já representa um projeto de portfólio
🎯 Aprendizados
Neste exercício foram praticados:
Integração entre sistemas
Processamento de dados financeiros
Geração de relatórios automatizados
Organização de projetos reais
Lógica de negócio (financeira)
