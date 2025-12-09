#  File Organizer (Organizador de Arquivos)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Concluído-green?style=for-the-badge)

> Um script de automação CLI (Command Line Interface) para organizar diretórios bagunçados automaticamente, agrupando arquivos por extensão em pastas categorizadas.

##  Sobre o Projeto

Este projeto foi desenvolvido como um "Weekend Project" (Projeto de Fim de Semana) com o objetivo de resolver um problema real: a desorganização de pastas como "Downloads". 

A aplicação varre um diretório de origem, identifica as extensões dos arquivos e os move para pastas de destino criadas dinamicamente (ex: PDFs vão para `Documentos_PDF`, Imagens para `Imagens`, etc.), gerando um relatório final da operação.

##  Funcionalidades

- [x] **Mapeamento Inteligente:** Usa um dicionário extensível para mapear extensões de arquivos para pastas específicas.
- [x] **Criação Automática de Pastas:** Verifica se a pasta de destino existe e, se não, a cria automaticamente (`os.makedirs`).
- [x] **Input Dinâmico:** O usuário define os caminhos de origem e destino na execução.
- [x] **Relatório de Execução:** Ao final, exibe um resumo detalhado de quais pastas foram criadas e quais arquivos foram movidos para elas.
- [x] **Tratamento de Erros:** Continua a execução mesmo se um arquivo específico falhar ao ser movido.

##  Tecnologias Utilizadas

O projeto foi construído utilizando **Python Puro**, focando no domínio das bibliotecas nativas de manipulação de sistema:

* **`os`**: Para navegação no sistema de arquivos, verificação de caminhos e criação de diretórios.
* **`shutil`**: Para operações de movimentação de arquivos de alta performance.

##  Como rodar o projeto

### Pré-requisitos
* Python 3.x instalado.

### Passo a passo

1. Clone o repositório:
   ```bash
   git clone [https://github.com/SEU-USUARIO/file-organizer.git](https://github.com/SEU-USUARIO/file-organizer.git)
