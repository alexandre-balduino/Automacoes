
# 🤖 Gerador Automático de Relatórios

## 🧠 Objetivo
Criar um sistema em Python que leia dados (CSV ou JSON), processe essas informações e gere automaticamente um relatório em arquivo `.txt`.

---

## ⚙️ Funcionalidades
- [x] Ler dados de um arquivo `.csv` ou `.json`
- [x] Processar informações (totais, médias, etc.)
- [x] Gerar relatório automaticamente
- [x] Salvar relatório em arquivo `.txt`
- [x] Nomear o relatório com data/hora
- [ ] Exportar para `.json`
- [ ] Exportar para `.csv`
- [ ] Agendar execução automática (cron/Termux)
- [ ] Gerar múltiplos relatórios

---

## 🧪 Tecnologias utilizadas
- Python 3
- Biblioteca `csv`
- Biblioteca `json`
- Biblioteca `datetime`
- Biblioteca `os`

---

## ▶️ Como executar

1. Navegue até a pasta do exercício:

```bash
cd nivel_3/ex_014_relatorios_automaticos
Execute o script:
Bash
python main.py
📂 Estrutura do projeto
Bash
ex_014_relatorios_automaticos/
├── main.py
├── dados.csv   # ou dados.json
├── relatorios/
└── README.md
📄 Exemplo de entrada (CSV)
Csv
descricao,valor
Salario,2500
Mercado,150
Internet,100
Freelance,800
📄 Exemplo de relatório gerado
Plain text
RELATÓRIO FINANCEIRO
Data: 2026-04-04 10:30

Total: R$ 3550.00
Média: R$ 887.50
Maior valor: R$ 2500.00
Menor valor: R$ 100.00
Quantidade de registros: 4
🔧 Como funciona
O programa lê o arquivo de entrada (CSV ou JSON)
Extrai os valores
Calcula:
total
média
maior valor
menor valor
quantidade de registros
Gera uma string formatada (relatório)
Cria a pasta relatorios/ (se não existir)
Salva o relatório com nome baseado em data/hora
🧠 Exemplo de nome do arquivo
Bash
relatorio_2026-04-04_10-30.txt
⚠️ Cuidados importantes
Garantir que o arquivo de entrada exista
Tratar erros de leitura
Criar pasta automaticamente (os.makedirs)
Converter valores corretamente (float)
Evitar sobrescrever relatórios
🚀 Melhorias futuras
Gerar relatórios em HTML
Criar dashboard simples
Enviar relatório por email
Integrar com APIs
Rodar automaticamente todo dia (cron no Termux)
Integrar com seu sistema financeiro (ZapBudget)
📌 Observações
O sistema pode ser adaptado para qualquer tipo de dado
Ideal para automações periódicas
Pode ser usado com logs, finanças, vendas, etc.
🎯 Aprendizados
Neste exercício foram praticados:
Automação completa (entrada → processamento → saída)
Geração de arquivos
Organização de relatórios
Uso de data e hora
Estruturação de sistemas automatizados
