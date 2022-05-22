print("-------- CADASTRO E VENDA DE MOTOCLICLETA HARLEY DAVIDSON --------")
def listarprodutos():
    for i in range(0,len(produtos)):
        print("Produto {} - [} - R${:.2f} - quantidade em estoque, {}" .format(i, produtos[i] [0], produtos [i][1], produtos [i] [2]))
        
produtos = []

while True:
    opção = int(input("tecle sua opção:\n1 = Cadsstrar produto\n2 = Listar produtos\n3 = Vender\n4 = Sair do programa"))
    if opção == 1:
        nome = input("Qual o nome do produto:")
        preço = float(input("Qual o preço do produto:"))
        quantidade = int(input("Qual a quantidade em estoque:"))

        produto = []

        produto.append(nome)
        produto.append(preço)
        produto.append(quantidade)
        produtos.append(produto)
    if opção == 2:
        listarprodutos()





