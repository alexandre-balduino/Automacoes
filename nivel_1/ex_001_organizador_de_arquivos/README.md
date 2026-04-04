# 📁 Organizador de Arquivos

## 🧠 Objetivo
Criar um script em Python capaz de organizar automaticamente arquivos de um diretório, separando-os em pastas com base em suas extensões.

---

## ⚙️ Funcionalidades
- [x] Ler todos os arquivos de uma pasta
- [x] Identificar a extensão de cada arquivo
- [x] Criar pastas automaticamente (se não existirem)
- [x] Mover arquivos para suas respectivas pastas
- [ ] Evitar sobrescrita de arquivos com o mesmo nome
- [ ] Gerar log das operações realizadas

---

## 🧪 Tecnologias utilizadas
- Python 3
- Biblioteca `os`
- Biblioteca `shutil`

---

## ▶️ Como executar

1. Clone o repositório ou copie o código
2. Navegue até a pasta do exercício:

```bash
cd ex_001_organizador_arquivos
```

3. Execute o script:

```Bash
python main.py
```

---

## 📂 Estrutura esperada

Antes da execução:

```Bash
pasta/
├── foto.jpg
├── documento.pdf
├── musica.mp3
```

Depois da execução:

```Bash
pasta/
├── imagens/
│   └── foto.jpg
├── documentos/
│   └── documento.pdf
├── audio/
│   └── musica.mp3
```

---

## 💡 Exemplo de saída

```Bash
Movendo foto.jpg → /imagens
Movendo documento.pdf → /documentos
Movendo musica.mp3 → /audio
```

---

## 🚀 Melhorias futuras

* Tratar arquivos com nomes duplicados
* Permitir escolher o diretório via input
* Criar interface no terminal (menu interativo)
* Gerar relatório em JSON
* Suporte a mais tipos de arquivos

---

## 📌 Observações

* O script considera apenas arquivos (ignora pastas)
* As pastas de destino são criadas automaticamente
* Pode ser adaptado para organizar a pasta de Downloads

---

## 🎯 Aprendizados

Neste exercício foram praticados:
* Manipulação de arquivos e diretórios com `os`
* Movimentação de arquivos com `shutil`
* Estruturação de scripts em Python
* Automação de tarefas repetitivas
