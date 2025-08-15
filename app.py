listaDeProdutos = []

def exibirMenu():
    while True:
        print("1 - Cadastrar Produto")
        print("2 - Listar Produtos")
        print("3 - Adicionar Produto ja Cadastrado")
        print("4 - Atualizar Produto")
        print("5 - Sair")
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            cadastrarProduto()
        elif opcao == 2:
            listarProdutos()
        elif opcao == 3:
            adicionarProduto()
        elif opcao == 4:
            atualizarListaDeProdutos()
        elif opcao == 5:
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
        codigo = int(input("Digite o código do produto que deseja adicionar: ")) - 1
        for produto in listaDeProdutos:
            if codigo == listaDeProdutos.index(produto):
                quantidade = int(input("Digite a quantidade a ser adicionada: "))
                produto['quantidade'] = produto.get('quantidade', 0) + quantidade
                print(f"Quantidade atualizada para o produto '{produto['nome']}': {produto['quantidade']}")
                return

def atualizarListaDeProdutos():
    codigo = int(input("Digite o código do produto que deseja atualizar: ")) - 1
    for produto in listaDeProdutos:
        if codigo == listaDeProdutos.index(produto):
            while True:
                print("- Atualizar Produto -")  
                print("1 - Nome")
                print("2 - Preço")
                print("3 - Quantidade")
                print("4 - Voltar ao Menu Principal")
                opcao = int(input("Escolha uma opção: "))
                if opcao == 1:
                    novoNome = input("Digite o novo nome do produto: ")
                    produto['nome'] = novoNome 
                    print(f"Produto '{novoNome}' atualizado com sucesso!")
                    return
                elif opcao == 2:
                    novoPreco = float(input("Digite o novo preço do produto: "))
                    produto['preco'] = novoPreco
                    print(f"Preço atualizado: '{novoPreco:.2f}'")
                elif opcao == 3:
                    novaQuantidade = int(input("Digite a nova quantidade do produto: "))
                    produto['quantidade'] = novaQuantidade
                    print(f"Quantidade atualizada: '{novaQuantidade}'")
                elif opcao == 4:
                    print("Saindo...")
                    break
                else:
                    print("Opção inválida. Tente novamente.")          


def listarProdutos():
    if not listaDeProdutos:
        print("Nenhum produto cadastrado.")
    else:
        print("Lista de Produtos:")
        for produto in listaDeProdutos:
            print(f" --- Nome: {produto['nome']}, Preço: R$ {produto['preco']:.2f}, Código: {listaDeProdutos.index(produto) + 1}"
                  f"\n | Quantidade: {produto.get('quantidade', 0)} |")


if __name__ == "__main__":
    exibirMenu()