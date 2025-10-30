# programa para receber dados de obra, autor, ano da obra, fator de impacto e se o autor é ou não romano e retornar a informação completa para o usuário. 

def main():
    # declaração de variáveis com entrada de dados
    obra = input("Digite o nome da obra:\n")
    autor = input("Digite o nome do autor:\n")
    ano = int(input("Digite o ano da obra:\n"))
    era = input("informe se o ano é a.e.c. ou e.c.:\n")
    impacto = float(input("Digite o fator de impacto da obra para a pesquisa:\n"))
    teste = input("O autor é Romano? [s/n]").strip().lower()
    
    # lógica booleana
    romano = (teste != 'n')
    
    # uso de Docstring para explicar bloco de código: use três aspas (simples ou duplas)
    ''' Como os comandos de limpar tela diferem nos mais diversos SOs (Sistemas Operacionais),
    chamaremos a biblioteca OS para implementar a limpeza de tela '''
    # no linux (posix) para limpar a tela do terminal se usa o comando 'clear', no windows (nt) o comando de terminal correspondente é 'cls'
    
    import os
    # os.system equivale à função system() em C.
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # entrega dos resultados formatados
    print("Resultado:")
    ''' para inserir variáveis, comandos ou expressões dentro de uma string
    é usar uma f-string (formatted string literal) que pode conter campos cambiáveis
    contendo expressões isoladas por chaves {} '''
    print(f"{obra} foi escrita no ano de {ano} {era} por {autor}.\n"
          f"O fator de impacto da obra sobre a pesquisa é {impacto}%.\n"
          f"É {'verdadeiro' if romano else 'falso'} que o autor seja romano.")
          
''' Ao rodar o código, o Python atribui à variável __name__ a função __main__
que será a função principal do código, quando outra função diferente não é atribuída.
Por isso, precisamos chamar sempre a função principal da seguinte forma: '''
if __name__ == "__main__":
    main()
