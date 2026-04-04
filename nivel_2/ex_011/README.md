
# 📂 Organizador de Arquivos por Tipo

## 🧠 Objetivo
Criar um script em Python que organize automaticamente arquivos de uma pasta em subpastas com base no tipo (extensão) dos arquivos.

---

## ⚙️ Funcionalidades
- [x] Ler arquivos de uma pasta
- [x] Identificar o tipo do arquivo pela extensão
- [x] Criar pastas automaticamente (se não existirem)
- [x] Mover arquivos para as pastas corretas
- [x] Evitar sobrescrita de arquivos
- [ ] Permitir desfazer organização (modo reverso)
- [ ] Criar categorias personalizadas
- [ ] Interface interativa (menu)

---

## 🧪 Tecnologias utilizadas
- Python 3
- Biblioteca `os`
- Biblioteca `shutil`

---

## ▶️ Como executar

1. Navegue até a pasta do exercício:

```bash
cd nivel_2/ex_011_organizador_arquivos
Execute o script:
Bash
python main.py
📂 Estrutura do projeto
Bash
ex_011_organizador_arquivos/
├── main.py
└── README.md
💡 Exemplo de uso
Antes:

pasta/
├── foto1.jpg
├── documento.pdf
├── musica.mp3
├── planilha.xlsx
Depois de executar o script:

pasta/
├── imagens/
│   └── foto1.jpg
├── documentos/
│   └── documento.pdf
├── musicas/
│   └── musica.mp3
├── planilhas/
│   └── planilha.xlsx
🧾 Tipos de arquivos (exemplo)
Extensão
Pasta destino
.jpg, .png
imagens
.pdf, .txt
documentos
.mp3
musicas
.xlsx, .csv
planilhas
outros
outros
🔧 Como funciona
O programa percorre todos os arquivos da pasta
Para cada arquivo:
identifica a extensão com os.path.splitext()
Define a pasta de destino com base na extensão
Cria a pasta (se não existir) com os.makedirs()
Move o arquivo com shutil.move()
⚠️ Cuidados importantes
Ignorar pastas (trabalhar apenas com arquivos)
Evitar sobrescrever arquivos com o mesmo nome
Trabalhar com caminhos absolutos quando necessário
🚀 Melhorias futuras
Interface interativa (modo menu)
Escolher pasta via input
Criar log das movimentações
Permitir desfazer organização
Criar regras personalizadas pelo usuário
Integrar com watchdog (organização automática em tempo real)
📌 Observações
O script organiza apenas arquivos da pasta atual
Subpastas não são processadas (pode ser uma melhoria)
As categorias podem ser adaptadas conforme necessidade
🎯 Aprendizados
Neste exercício foram praticados:
Manipulação de arquivos e diretórios
Uso de os e shutil
Automação de tarefas reais
Organização de dados no sistema de arquivos
Boas práticas com arquivos
