listaDeProdutos = []

def exibirMenu():
    while True:
        print("1 - Cadastrar Produto")
        print("2 - Listar Produtos")
        print("3 - Adicionar Produto ja Cadastrado")
        print("4 - Sair")
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            cadastrarProduto()
        elif opcao == 2:
            listarProdutos()
        elif opcao == 3:
            adicionarProduto()
        elif opcao == 4:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


def cadastrarProduto():
    nomeDoProduto = input("Digite o nome do produto: ")
    precoDoProduto = float(input("Digite o preço do produto: "))
    produto = {"nome": nomeDoProduto, "preco": precoDoProduto}
    listaDeProdutos.append(produto)
    print(f"Produto '{nomeDoProduto}' cadastrado com sucesso!")


def adicionarProduto():
    for produto in listaDeProdutos:
        print(f"Nome: {produto['nome']}, Código: {listaDeProdutos.index(produto) + 1}")
        codigo = int(input("Digite o código do produto que deseja adicionar: ")) - 1
        if codigo == listaDeProdutos.index(produto):
            quantidade = int(input("Digite a quantidade a ser adicionada: "))
            produto['quantidade'] = produto.get('quantidade', 0) + quantidade
            print(f"Quantidade atualizada para o produto '{produto['nome']}': {produto['quantidade']}")
            return


def listarProdutos():
    if not listaDeProdutos:
        print("Nenhum produto cadastrado.")
    else:
        print("Lista de Produtos:")
        for produto in listaDeProdutos:
            print(f"Nome: {produto['nome']}, Preço: R$ {produto['preco']:.2f}, Código: {listaDeProdutos.index(produto) + 1}")


if __name__ == "__main__":
    exibirMenu()