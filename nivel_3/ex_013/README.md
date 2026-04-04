
# 📊 Analisador de CSV (Relatórios Automáticos)

## 🧠 Objetivo
Criar um sistema em Python que leia um arquivo CSV com dados (ex: vendas, finanças ou usuários) e gere relatórios automáticos com base nessas informações.

---

## ⚙️ Funcionalidades
- [x] Ler arquivo `.csv`
- [x] Exibir dados formatados
- [x] Calcular totais (ex: soma de valores)
- [x] Calcular média
- [x] Encontrar maior e menor valor
- [x] Gerar relatório no terminal
- [ ] Exportar relatório para `.txt`
- [ ] Exportar relatório para `.json`
- [ ] Filtrar dados (por data, categoria, etc.)
- [ ] Criar gráficos simples (futuro)

---

## 🧪 Tecnologias utilizadas
- Python 3
- Biblioteca `csv`
- Biblioteca `os`

---

## ▶️ Como executar

1. Navegue até a pasta do exercício:

```bash
cd nivel_3/ex_012_analisador_csv
Execute o script:
Bash
python main.py
📂 Estrutura do projeto
Bash
ex_012_analisador_csv/
├── main.py
├── dados.csv
└── README.md
📄 Exemplo de CSV
Csv
descricao,valor
Salario,2500
Mercado,150
Internet,100
Luz,200
Freelance,800
💡 Exemplo de saída
Bash
--- RELATÓRIO ---

Total: R$ 3750.00
Média: R$ 750.00
Maior valor: R$ 2500.00
Menor valor: R$ 100.00
🔧 Como funciona
O programa abre o arquivo CSV
Lê os dados linha por linha com csv.reader ou csv.DictReader
Armazena os valores em uma lista
Realiza cálculos:
soma total
média
maior valor
menor valor
Exibe o relatório formatado
⚠️ Cuidados importantes
Converter valores para float
Ignorar cabeçalho corretamente
Validar dados inválidos
Tratar arquivos inexistentes
🚀 Melhorias futuras
Filtrar por tipo (receita/despesa)
Agrupar por categoria
Gerar gráficos (matplotlib)
Interface interativa
Integrar com JSON (exercícios anteriores)
Exportar relatórios automaticamente
📌 Observações
O CSV deve estar no formato correto
Os valores devem ser numéricos
O sistema pode ser adaptado para qualquer tipo de dado
🎯 Aprendizados
Neste exercício foram praticados:
Leitura de arquivos CSV
Processamento de dados
Geração de relatórios
Lógica de análise de dados
Estruturação de sistemas analíticos
