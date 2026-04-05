
# 💰 Controle Financeiro com JSON

## 🧠 Objetivo
Criar um sistema em Python para registrar e gerenciar transações financeiras (receitas e despesas), utilizando JSON para persistência de dados.

---

## ⚙️ Funcionalidades
- [x] Registrar receita
- [x] Registrar despesa
- [x] Listar transações
- [x] Calcular saldo atual
- [x] Salvar dados em `.json`
- [x] Carregar dados ao iniciar o programa
- [ ] Editar transações
- [ ] Remover transações
- [ ] Filtrar por tipo (receita/despesa)
- [ ] Filtrar por data

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
cd nivel_2/ex_010_controle_financeiro
```

2. Execute o script:

```Bash
python main.py
```

---

## 📂 Estrutura do projeto

```Bash
ex_010_controle_financeiro/
├── main.py
├── dados.json
└── README.md
```

---

## 💡 Exemplo de uso

```Bash
[1] Registrar receita
[2] Registrar despesa
[3] Ver transações
[4] Ver saldo
[5] Sair

Escolha uma opção: 1

Descrição: Salário
Valor: 2500

✔ Receita registrada com sucesso!
```

---

## 📄 Exemplo do arquivo JSON

```JSON
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
  }
]
```

---

## 🔧 Como funciona

* O programa verifica se o arquivo dados.json existe
* Caso exista:
> * carrega as transações com json.load()
* Caso não exista:
> * inicia uma lista vazia
* Cada transação possui:
> * id único
> * descrição
> * valor
> * tipo (receita ou despesa)
> * data
* O saldo é calculado somando:
> * receitas (+)
> * despesas (-)

---

## 📊 Exemplo de cálculo de saldo

```Bash
Saldo atual: R$ 2350.00

---

## 🚀 Melhorias futuras

* Editar e remover transações
* Categorias (alimentação, transporte, etc.)
* Múltiplas contas (carteira, banco)
* Exportar para CSV ou Excel
* Interface gráfica (Kivy)
* Integração com APIs financeiras

---
## 📌 Observações

* Os dados são armazenados localmente em JSON
* O saldo é calculado dinamicamente
* O arquivo é atualizado a cada nova transação

---

## 🎯 Aprendizados

Neste exercício foram praticados:
* Manipulação de dados financeiros
* Uso de JSON para persistência
* Trabalhar com datas (datetime)
* Estruturação de sistemas reais
* Lógica de cálculo (saldo, receitas e despesas)
