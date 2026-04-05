
# ✅ Gerenciador de Tarefas (To-Do List)

## 🧠 Objetivo
Criar um sistema em Python para gerenciar tarefas (to-do list), permitindo adicionar, listar, concluir e remover tarefas, com persistência de dados em JSON.

---

## ⚙️ Funcionalidades
- [x] Adicionar nova tarefa
- [x] Listar tarefas
- [x] Marcar tarefa como concluída
- [x] Remover tarefa
- [x] Salvar tarefas em `.json`
- [x] Carregar tarefas ao iniciar o programa
- [ ] Editar tarefas
- [ ] Filtrar tarefas (pendentes/concluídas)
- [ ] Prioridade de tarefas

---

## 🧪 Tecnologias utilizadas
- Python 3
- Biblioteca `json`
- Biblioteca `os`

---

## ▶️ Como executar

1. Navegue até a pasta do exercício:

```bash
cd nivel_2/ex_009_todo_list
```

Execute o script:

```Bash
python main.py
```

## 📂 Estrutura do projeto

```Bash
ex_009_todo_list/
├── main.py
├── tarefas.json
└── README.md
```

## 💡 Exemplo de uso

```Bash
[1] Adicionar tarefa
[2] Listar tarefas
[3] Concluir tarefa
[4] Remover tarefa
[5] Sair

Escolha uma opção: 1

Digite a tarefa: Estudar Python

✔ Tarefa adicionada com sucesso!
```

---

## 📄 Exemplo do arquivo JSON

```JSON
[
  {
    "id": 1,
    "descricao": "Estudar Python",
    "concluida": false
  },
  {
    "id": 2,
    "descricao": "Fazer exercícios",
    "concluida": true
  }
]
```

---

## 🔧 Como funciona

* O programa verifica se o arquivo tarefas.json existe
* Caso exista:
> * carrega as tarefas com json.load()
* Caso não exista:
> * inicia uma lista vazia
* Cada tarefa possui:
> * id único
> * descrição
> * status (concluída ou não)
* Ao modificar tarefas:
> * os dados são atualizados no JSON

---

## 🚀 Melhorias futuras

* Editar tarefas
* Filtrar por status (pendente/concluída)
* Adicionar prioridade (baixa, média, alta)
* Adicionar data de criação
* Interface interativa mais avançada
* Criar versão com interface gráfica (Kivy)

---

## 📌 Observações

* Os dados são armazenados localmente em JSON
* O ID das tarefas deve ser único
* O arquivo é atualizado a cada alteração

---

## 🎯 Aprendizados

Neste exercício foram praticados:
* CRUD completo com JSON
* Manipulação de listas e dicionários
* Persistência de dados
* Estruturação de sistemas interativos
* Organização de lógica de aplicação
