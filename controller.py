from models import *
from dao import *
from datetime import datetime

class ControllerCategoria:
    def cadastrarCategoria(self, novaCategoria):
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novaCategoria:
                existe = True

        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print('Categoria cadastrada com sucesso!')
        else:
            print('Categoria informada já existe!')
    
    def removerCategoria(self, categoriaRemover):
        x = DaoCategoria.ler()
        cat = list(filter(lambda item: item.categoria == categoriaRemover, x))
        
        if len(cat) == 0:
            print(f"A categoria '{categoriaRemover}' que você deseja remover não existe.")
        else:
            for i in range(len(x)):
                if x[i].categoria == categoriaRemover:
                    del x[i]
                    print(f"Categoria '{categoriaRemover}' removida com sucesso")
                    break            

            DaoCategoria.atualizarCategoria(x)

    def alterarCategoria(self, alterarCategoria, categoriaDesejada):
        x = DaoCategoria.ler()
        cat = list(filter( lambda c: c.categoria == alterarCategoria, x))

        if len(cat) > 0:
            cat1 = list(filter(lambda c : c.categoria == categoriaDesejada, x))
            if len(cat1) == 0:
                x  = list(map(lambda c: Categoria(categoriaDesejada) if c.categoria == alterarCategoria else c, x))

                with open('categoria.txt','w') as file_object:
                    for i in x:
                        file_object.writelines(i.categoria)
                        file_object.writelines('\n')
                print('A categoria foi alterada com sucesso!')

            else:
                print('A categoria que deseja alterar já existe!')
        
        else:
            print('A categoria que você deseja alterar não existe!')
    
    def mostrarCategorias(self):
        categorias = DaoCategoria.ler()
        if len(categorias) == 0:
            print('Categoria vazia!')
        else:
            for cat in categorias:
                print(f'Categoria: {cat.categoria}')

class ControllerEstoque:
    def cadastrarProduto(self, nome, preco, categoria, quantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()

        cat_compara = list(filter(lambda cat: cat.categoria == categoria,y))
        estoque = list(filter(lambda est: est.produto.nome == nome,x))

        if len(cat_compara) > 0:
            if len(estoque) == 0:
                produto= Produto(nome, preco, categoria)
                DaoEstoque.salvar(produto,quantidade)
                print('Produto cadastrado com sucesso.')
            else:
                print('Produto já existe me estoque.')
        else:
            print('Categoria inexistente.')

    def removerProduto(self, nome):
        estoque = DaoEstoque.ler()
        produto_encontrado = list(filter(lambda item: item.produto.nome == nome, estoque))

        if produto_encontrado:
            for i in range(len(estoque)):
                if estoque[i].produto.nome == nome:
                    del estoque[i]  # Remover da memória
                    print('Produto removido com sucesso!')
                    break
        else:
            print('Produto que deseja remover não existe.')

        with open('estoque.txt', 'w') as file_object:
            for item in estoque:
                file_object.write(f"{item.produto.nome}|{item.produto.preco}|"
                                f"{item.produto.categoria}|{item.quantidade}\n")
    def alterarProduto(self, nomeAlterar, novoNome, novoPreco, novaCategoria, novaQuantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x : x.categoria == novaCategoria, y))

        if len(h) > 0 :
            estoque = list(filter(lambda x : x.produto.nome == nomeAlterar, x))
            if len(estoque) > 0:
                estoque = list(filter(lambda x : x.produto.nome == novoNome, x))
                if len(estoque) == 0:
                    x = list(map(lambda x: Estoque(Produto(novoNome, novoPreco, novaCategoria), novaQuantidade)if(x.produto.nome == nomeAlterar) else(x), x))
                    print('Produto alterado com sucesso.')
                else:
                    print('Produto já cadastrado.')
            else:
                print('O produto que deseja alterar não existe.')
            
            DaoEstoque.atualizarProduto(x)

        else:
            print('A categoria informada não existe.')
        
    def mostrarEstoque(self):
        estoque = DaoEstoque.ler()
        if len(estoque) == 0:
            print('Estoque vazio.')
        else:
            print('##### Produtos: #####')
            print('---------------------')
            for i in estoque:               
                print(f'Nome: {i.produto.nome}\n'
                      f'Preço: {i.produto.preco}\n'
                      f'Categoria: {i.produto.categoria}\n'
                      f'Quantidade: {i.quantidade}')
                print('---------------------')
                    
class ControllerVenda:
    def cadastrarVenda(self, nomeProduto, vendedor, cliente, quantidadeVendida):
        x = DaoEstoque.ler()
        temp = []
        existe = False
        quantidade = False

        for i in x:
            if existe == False:
                if i.produto.nome == nomeProduto:
                    existe = True
                    if i.quantidade >= quantidadeVendida:
                        quantidade = True
                        i.quantidade = int(i.quantidade) - int(quantidadeVendida)

                        vendido = Venda(Produto(i.produto.nome,i.produto.preco, i.produto.categoria), 
                                        quantidadeVendida, vendedor, cliente)
                        valorCompra = int(quantidadeVendida) * float(i.produto.preco)
                        DaoVenda.salvar(vendido)
        
        temp.append([Produto(i.produto.nome,i.produto.preco, i.produto.categoria),i.quantidade])

        file_object = open('estoque.txt','w')
        file_object.write = ("")

        for i in temp:
            with open('estoque.txt', 'a') as file_object:
                file_object.writelines(f"{i[0].nome}|{i[0].preco}|{i[0].categoria}|{i[1]}\n")
        
        if not existe:
            print('O produto não existe.')
            return None
        elif not quantidade:
            print('Quantidade insuficiente em estoque.')
        else:
            return valorCompra




a = ControllerVenda()
a.cadastrarVenda('Contra filé','William','Heitor',2)
""" a = ControllerEstoque()
a.cadastrarProduto('Contra filé','49.90','Carne',100) """
""" a.alterarProduto('Maçã', 'Maçã Verde', '5.00', 'Frutas', 10) """