print("-------- CADASTRO E VENDA DE MOTOCLICLETA HARLEY DAVIDSON --------")
print(" --------------LOJAS MULTVERSOS MOTOR -------------")

#Harley-Davidson Bad Boy -  valor 50900.00 - quantidade 6
#Harley-Davidson Dyna Fat Bob FXDF - valor 45000.00 - quantidade 5
#Harley-Davidson Electra Glide Classi - valor 57000.00 - quantidade 3
#Harley-Davidson FLH 1200 - valor 88990.00 - quantidade 1

def listarMotocicletas():
    for i in range(0, len(produtos)):
        print("Produto {} - {} - R${:.2f} - Quantidade em estoque, {}".format(i, produtos[i][0], produtos[i][1], produtos[i][2]))

produtos = []

while True:
    opcao = int(input("Tecle sua opção:\n1 - Cadastrar produto\n2 - Listar produtos\n3 - Vender\n4 - Sair do programa\nDigite uma das opções:"))

    if opcao == 1:
        nome = input("Qual o nome do Motocicletas em estoque?")
        preco = float(input("Qual o preço da Motocicleta?"))
        quantidade = int(input("Qual a quantidade de Motocicleta em estoque?"))

        produto = []

        produto.append(nome)
        produto.append(preco)
        produto.append(quantidade)
        produtos.append(produto)

    if opcao == 2:
        listarMotocicletas()


    if opcao == 3:
        print("Escolha um dos Modelos de Motocicleta Harley-Davidson:")
        listarMotocicletas()

        numero = int(input("Informe o Código do Produto a ser vendido?"))

        quantidade = int(input("Qual a quantidade a ser vendida?"))

        if produtos[numero][2] >= quantidade:
            print("Produto vendido com sucesso! Informações da venda:\nProduto: {}\nQuantidade: {}\nValor total da venda: R${:.2f}".format(produtos[numero][0], quantidade, quantidade*produtos[numero][1]))
            produtos[numero][2] -= quantidade
        else:
            print("Quantidade indisponível em estoque")

    if opcao == 4:
        print(" +++++++++ LOJAS MULTVERSOS MOTOR AGRADECE PELA SUA COMPRA! ++++++++++")
        break




