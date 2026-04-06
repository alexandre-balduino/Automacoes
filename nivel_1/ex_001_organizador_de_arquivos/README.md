# 📁 Organizador de Arquivos

```markdown
⚡ Projeto desenvolvido como exercício prático de automação com Python.
Focado em manipulação de arquivos, organização de diretórios e boas práticas.
```

## 🧠 Objetivo
Criar um script em Python capaz de organizar automaticamente arquivos de um diretório, separando-os em pastas com base em suas extensões.

---

## ⚙️ Funcionalidades
- [x] Ler todos os arquivos de uma pasta
- [x] Identificar a extensão de cada arquivo
- [x] Criar pastas automaticamente (se não existirem)
- [x] Mover arquivos para suas respectivas pastas
- [x] Evitar sobrescrita de arquivos com o mesmo nome
- [x] Gerar log das operações realizadas

---

## 🧪 Tecnologias utilizadas
- Python 3
- Biblioteca `os`
- Biblioteca `shutil`
- Biblioteca `logging`

---

## ▶️ Como executar

```bash
git clone https://github.com/alexandre-balduino/automacoes.git
cd ex_001_organizador_arquivos
python main.py
```

---

## 📂 Estrutura esperada

Antes:

```
pasta/
├── foto.jpg
├── documento.pdf
├── musica.mp3
```

Depois:

```
pasta/
├── imagens/
│   └── foto.jpg
├── documentos/
│   └── documento.pdf
├── audios/
│   └── musica.mp3
```

---

## 📝 Exemplo de log

```Bash
2026-04-05 10:00:00 - foto.jpg -> imagens
2026-04-05 10:00:01 - documento.pdf -> documentos
2026-04-05 10:00:02 - musica.mp3 -> audios
```

---

## 📌 Observações

- O script considera apenas arquivos (ignora pastas)
- As pastas de destino são criadas automaticamente
- O log é salvo automaticamente na pasta do script
- Pode ser adaptado para organizar a pasta de Downloads

---

## 🎯 Aprendizados

- Neste projeto foram praticados:
* Manipulação de arquivos e diretórios com `os`
* Movimentação de arquivos com `shutil`
* Uso de logs com `logging`
* Estruturação de scripts em Python
* Automação de tarefas repetitivas