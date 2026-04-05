
# 📋 Sistema de Cadastro com JSON


## 🧠 Objetivo
Criar um sistema em Python capaz de cadastrar, armazenar e gerenciar dados de usuários utilizando arquivos JSON como forma de persistência.

---

## ⚙️ Funcionalidades
- [x] Cadastrar novo usuário
- [x] Listar usuários cadastrados
- [x] Buscar usuário por nome
- [x] Salvar dados em arquivo `.json`
- [x] Carregar dados ao iniciar o programa
- [ ] Editar usuário
- [ ] Remover usuário
- [ ] Validar dados de entrada

---

## 🧪 Tecnologias utilizadas
- Python 3
- Biblioteca `json`
- Biblioteca `os`

---

## ▶️ Como executar

1. Navegue até a pasta do exercício:

```bash
cd nivel_2/ex_007_cadastro_json
```

Execute o script:

```Bash
python main.py
```

---

## 📂 Estrutura do projeto

```Bash
ex_007_cadastro_json/
├── main.py
├── dados.json
└── README.md
```

---

## 💡 Exemplo de uso

```Bash
[1] Cadastrar usuário
[2] Listar usuários
[3] Buscar usuário
[4] Sair

Escolha uma opção: 1

Nome: João
Idade: 25
Email: joao@email.com
✔ Usuário cadastrado com sucesso!
```

---

## 📄 Exemplo do arquivo JSON

```JSON
[
  {
    "nome": "João",
    "idade": 25,
    "email": "joao@email.com"
  },
  {
    "nome": "Maria",
    "idade": 30,
    "email": "maria@email.com"
  }
]
```

---

## 🔧 Como funciona

* O programa verifica se o arquivo dados.json existe
* Caso exista:
> * carrega os dados com json.load()
* Caso não exista:
> * cria uma lista vazia
* Ao cadastrar:
> * adiciona o novo usuário na lista
> * salva com json.dump()
* Os dados permanecem salvos mesmo após encerrar o programa

---

## 🚀 Melhorias futuras

* Editar e remover usuários
* Validação de email
* Interface interativa mais amigável
* Separar lógica em módulos
* Criar versão com banco de dados (SQLite)

---

## 📌 Observações

* Os dados são armazenados localmente em formato JSON
* O arquivo é atualizado a cada alteração
* Ideal para sistemas simples sem necessidade de banco de dados

---

## 🎯 Aprendizados

Neste exercício foram praticados:
* Leitura e escrita de arquivos JSON
* Persistência de dados
* Estruturação de sistemas simples
* Manipulação de listas e dicionários
* Criação de menus interativos
