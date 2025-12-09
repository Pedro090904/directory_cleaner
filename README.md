````markdown
#  File Organizer (Organizador de Arquivos)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Concluído-green?style=for-the-badge)

> Um script de automação CLI (Command Line Interface) desenvolvido em Python para organizar diretórios bagunçados automaticamente, agrupando arquivos por extensão em pastas categorizadas.

##  Sobre o Projeto

Este projeto foi desenvolvido como um "Weekend Project" (Projeto de Fim de Semana) com o objetivo de resolver um problema real: a desorganização de pastas de trabalho e downloads.

A aplicação varre um diretório de origem definido pelo usuário, identifica as extensões dos arquivos e os move para pastas de destino criadas dinamicamente (ex: PDFs vão para `Documentos_PDF`, Imagens para `Imagens`, etc.), gerando um relatório detalhado ao final da operação.

##  Funcionalidades

- [x] **Mapeamento Inteligente:** Utiliza um dicionário extensível para mapear extensões de arquivos para pastas específicas.
- [x] **Criação Automática de Pastas:** Verifica a existência do diretório de destino e, caso não exista, cria-o automaticamente (`os.makedirs`).
- [x] **Input Dinâmico:** O usuário define os caminhos de origem e destino no momento da execução, tornando o script reutilizável para qualquer diretório.
- [x] **Relatório de Execução:** Ao final do processo, exibe um resumo detalhado de quais pastas foram criadas e quais arquivos foram movidos para elas.
- [x] **Tratamento de Erros:** O sistema continua a execução e loga o erro caso um arquivo específico falhe ao ser movido, garantindo robustez.

##  Tecnologias Utilizadas

O projeto foi construído utilizando **Python Puro**, com foco no domínio das bibliotecas nativas de manipulação do Sistema Operacional:

* **`os`**: Utilizado para navegação no sistema de arquivos, verificação de caminhos e criação recursiva de diretórios.
* **`shutil`**: Utilizado para operações de movimentação de arquivos de alta performance.

##  Como rodar o projeto

### Pré-requisitos
* Python 3.x instalado na máquina.

### Passo a passo

1. Clone este repositório:
   ```bash
   git clone (https://github.com/Pedro090904/directory_cleaner.git)
````

2.  Acesse a pasta do projeto:

    ```bash
    cd file-organizer
    ```

3.  Execute o script principal:

    ```bash
    python main.py
    ```


4.  Siga as instruções interativas no terminal:

      * Insira o caminho completo da pasta bagunçada (Origem).
      * Insira o caminho onde deseja salvar os arquivos organizados (Destino).

##  Lógica do Código

O script segue uma estrutura modular simples e eficiente:

1.  **Entrada:** Coleta e valida os caminhos fornecidos pelo usuário.
2.  **Processamento:** Itera sobre os arquivos da pasta origem usando `os.listdir`.
3.  **Verificação:** Checa a extensão de cada arquivo contra um dicionário de regras pré-definido.
4.  **Ação:** Cria os diretórios necessários e move os arquivos.
5.  **Feedback:** Popula um dicionário de relatório em tempo real e imprime o resumo no console.

##  Exemplo de Execução

```text
--- ORGANIZADOR DE ARQUIVOS v1.1 ---
Digite o caminho da pasta origem: C:\Users\Dev\Downloads
Digite o caminho da pasta destino: C:\Users\Dev\Documents\Organizados

Iniciando organização...

[OK] Movido: relatorio_financeiro.pdf -> Documentos_PDF
[OK] Movido: foto_praia.jpg -> Imagens
[OK] Movido: setup.exe -> Instaladores
...

========================================
RESUMO DA ORGANIZAÇÃO
========================================

📂 Pasta criada/usada: 'Documentos_PDF'
   Arquivos movidos (1):
   - relatorio_financeiro.pdf

📂 Pasta criada/usada: 'Imagens'
   Arquivos movidos (1):
   - foto_praia.jpg

📂 Pasta criada/usada: 'Instaladores'
   Arquivos movidos (1):
   - setup.exe

========================================
Total geral: 3 arquivos organizados.
```

## 👨‍💻 Autor

Desenvolvido por **Pedro de Sousa Mesquita**

  * [LinkedIn](https://www.linkedin.com/in/pedro-de-sousa-mesquita-930417306/)
  * [GitHub](https://github.com/Pedro090904)

-----

```
```