# 🗑️ Lixeira Simulada de Arquivos

## 🧠 Objetivo
Criar um sistema simples em Python que simula o funcionamento de uma lixeira, permitindo mover arquivos, restaurá-los ou removê-los permanentemente.

---

## ⚙️ Funcionalidades
- [x] Enviar arquivos para a lixeira (mover arquivos)
- [x] Criar automaticamente a pasta `lixeira/`
- [x] Listar arquivos presentes na lixeira
- [x] Restaurar arquivos para o local original
- [x] Deletar arquivos permanentemente
- [ ] Confirmar ações críticas (ex: exclusão)
- [ ] Evitar conflitos de nomes
- [ ] Registrar ações em log (JSON)

---

## 🧪 Tecnologias utilizadas
- Python 3
- Biblioteca `os`
- Biblioteca `shutil`

---

## ▶️ Como executar

1. Navegue até a pasta do exercício:

```bash
cd ex_003_lixeira_simulada
```

2. Execute o script:

```Bash
python main.py
```

---

## 📂 Estrutura do projeto

```Bash
ex_003_lixeira_simulada/
├── main.py
├── lixeira/
└── dados/ (opcional)
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

## 🔧 Como funciona

* O usuário escolhe uma opção no menu
* Ao enviar para a lixeira:
> * o arquivo é movido para a pasta /lixeira
* Ao restaurar:
> * o arquivo volta para seu local original
* Ao deletar:
> * o arquivo é removido permanentemente do sistema

---

## 🚀 Melhorias futuras

* Salvar caminho original dos arquivos em JSON
* Interface mais amigável no terminal
* Suporte a múltiplos arquivos
* Sistema de confirmação antes de deletar
* Criar versão com interface gráfica (Kivy)

---

## 📌 Observações

* A lixeira é simulada como uma pasta dentro do projeto
* Arquivos restaurados dependem do armazenamento do caminho original
* Caso não haja controle de origem, o arquivo pode ser restaurado manualmente

---

## 🎯 Aprendizados

* Neste exercício foram praticados:
* Manipulação de arquivos e diretórios
* Movimentação de arquivos com shutil
* Estruturação de menus interativos
* Simulação de sistemas reais
* Controle básico de estado de arquivos
