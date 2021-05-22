def vogais(nome):
	i = 0
	qtd = 0
	for a in nome:
		if nome[i] == 'a' or nome[i] == 'e' or nome[i] == 'i' or nome[i] == 'o' or nome[i] == 'u':
			qtd += 1

		i += 1

	print('Este nome tem ',qtd, ' vogais')



vogais(input("Digite um nome "))