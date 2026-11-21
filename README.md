Projecto_Python_Unisave_2026
# Sistema de Gestão de Estudantes - Universidade Save

Sistema em Python para gerir estudantes da Universidade Save, substituindo o controlo manual em papel. Permite cadastrar estudantes, listar todos os registados, pesquisar por número e guardar os dados de forma persistente em ficheiro JSON, facilitando a consulta rápida de informações académicas como curso, ano e nota final.

## Elementos do Grupo

* Nome Completo 1 (antoniojuniorlanga62)
* Nome Completo 2 (muiangaantonio717-ctrl)
* Nome Completo 3 (monteiroisabel015-ctrl)
* Nome Completo 4 (Liriavirgiliom-alt)

## Funcionalidades

* Cadastrar novo estudante com nome, número, curso, ano e nota final
* Listar todos os estudantes cadastrados
* Buscar estudante pelo número do estudante
* Guardar dados automaticamente em ficheiro JSON
* Carregar dados automaticamente ao iniciar o programa
* Menu interativo em consola, fácil de usar
* Tratamento de dados com persistência local sem precisar de internet

## Stack Técnica

* Linguagem: Python 3.x
* Paradigma: Programação Orientada a Objetos (POO)
* Armazenamento: JSON
* Dependências: Nenhuma (apenas biblioteca padrão do Python - `json` e `os`)

## Arquitetura

O projecto está organizado num único ficheiro principal com separação lógica de responsabilidades:

* `main.py`: Ficheiro principal que contém o menu interativo e a execução do programa
* `Classe Estudante`: Representa um estudante com os atributos nome, numero, curso, ano e nota, e o método `para_dicionario()` para converter o objeto em dicionário para guardar em JSON
* `carregar_estudantes()`: Lê os dados do ficheiro `estudantes.json` e devolve a lista de estudantes
* `salvar_estudantes()`: Guarda a lista de estudantes no ficheiro `estudantes.json` com formatação legível
* `cadastrar()`, `listar()` `buscar()`: Funções de negócio que implementam as funcionalidades do sistema
* `estudantes.json`: Ficheiro local onde os dados são armazenados de forma persistente

## Requisitos

* Python 3.8 ou superior instalado no computador.

## Instalação e Execução
```bash
git clone https://github.com/antoniojuniorlanga62-create/Projecto_Python_Unisave_2026.git
cd Projecto_Python_Unisave_2026
python main.py
