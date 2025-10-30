programa 
{
  funcao inicio() 
  {
    cadeia obra
    cadeia autor
    inteiro ano
    cadeia era
    real impacto
    caracter teste
    logico romano
    
    escreva("Digite o nome da obra:\n")
    leia(obra)
    escreva("Digite o nome do autor:\n")
    leia(autor)
    escreva("Digite o ano da obra:\n")
    leia(ano)
    escreva("Escreva E.C. para Era Comum ou A.E.C. para Antes da Era Comum.\n")
    leia(era)
    escreva("Digite o impacto da obra para a pesquisa:\n")
    leia(impacto)
    escreva("O autor é romano? [s/n]\n")
    leia(teste)

    romano = (teste!='n')
    limpa()
    escreva("Resultado:\n", obra, " foi escrita em: ", ano," ", era, " por ", autor, ".\nO impacto da obra para a pesquisa é de: ", impacto, "% e é ", romano, " que o autor seja romano.")

  }
}
