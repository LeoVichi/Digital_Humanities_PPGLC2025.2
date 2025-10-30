# programa para receber dados de obra, autor, ano da obra, fator de impacto e se o autor é ou não romano e retornar a informação completa para o usuário.
import os
def limpar():
    # limpar tela
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    # declaração de variáveis
    obra = input("Digite o nome da obra:\n")
    autor = input("Digite o nome do autor da obra:\n")
    ano = int(input("Digite o ano da obra:\n"))
    era = input("Digite e.c. para Era Comum e a.e.c. para Antes da Era Comum:\n")
    impacto = float(input("Informe o fator de impacto da obra para a pesquisa:\n"))
    teste = input("O autor é romano? [s/n]").strip().lower()
    
    # teste de lógica booleana
    romano = teste in ('s', 'sim', 'y', 'yes', 'claro', 'positivo')
    limpar()
    #Retorno dos resultados
    # repare nesse bloco o emprego de uma Docstring (Documentation string) fechada em aspas triplas
    
    print("Resultado:")
    ''' para inserir variáveis, expressões ou comandos dentro de uma string é possível
    usar o tipo f-string (formatted string literal) que pode conter campos 
    cambiáveis contendo expressões isoladas por chaves {}'''
    print(f"{obra} foi escrita no ano de {ano} {era} por {autor}.\n"
          f"o impacto da obra para a pesquisa atual é de {impacto}%.\n"
          f"É {'verdadeiro' if romano else 'falso'} que o autor seja romano.")
          

# atribuindo função principal à variável __name__
if __name__ == "__main__":
    main()
