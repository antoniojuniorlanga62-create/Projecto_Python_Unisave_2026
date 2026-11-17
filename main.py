
import json
import os

FICHEIRO = "estudantes.json"

class Estudante:
    def __init__(self, nome, numero, curso, ano, nota):
        self.nome = nome
        self.numero = numero
        self.curso = curso
        self.ano = ano
        self.nota = nota

    def para_dicionario(self):
        return {
            "nome": self.nome,
            "numero": self.numero,
            "curso": self.curso,
            "ano": self.ano,
            "nota": self.nota
        }
def carregar_estudantes():
    if not os.path.exists(FICHEIRO):
        return []
    with open(FICHEIRO, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_estudantes(lista):
    with open(FICHEIRO, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=4, ensure_ascii=False)
    print("Dados salvos com sucesso!")
def cadastrar():
    print("\n--- Novo Estudante ---")
    nome = input("Nome: ")
    numero = input("Número do estudante: ")
    curso = input("Curso: ")
    ano = input("Ano: ")
    nota = float(input("Nota final: "))

    novo = Estudante(nome, numero, curso, ano, nota)
    lista = carregar_estudantes()
    lista.append(novo.para_dicionario())
    salvar_estudantes(lista)

def listar():
    lista = carregar_estudantes()
    if not lista:
        print("\nNenhum estudante cadastrado.")
        return
    print("\n--- Lista de Estudantes ---")
    for e in lista:
        print(f"{e['numero']} | {e['nome']} | {e['curso']} - {e['ano']}º Ano | Nota: {e['nota']}")

def buscar():
    numero = input("\nDigite o número do estudante para buscar: ")
    lista = carregar_estudantes()
    for e in lista:
        if e['numero'] == numero:
            print(f"Encontrado: {e['nome']} | Curso: {e['curso']} | Nota: {e['nota']}")
            return
    print("Estudante não encontrado.")
def menu():
    while True:
        print("\n===== SISTEMA UNIVERSIDADE SAVE=====")
        print("1. Cadastrar estudante")
        print("2. Listar estudantes")
        print("3. Buscar estudante")
        print("4. Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            buscar()
        elif opcao == "4":
            print("Até logo!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()