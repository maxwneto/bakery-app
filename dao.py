from models import  *
class DaoCategoria:
    @classmethod
    def salvar(cls, categoria):
        with open('categoria.txt','a') as file_object:
            file_object.writelines(categoria)
            file_object.writelines('\n')

    @classmethod
    def ler(cls):
        with open('categoria.txt','r') as file_object:
            cls.categoria = file_object.readlines()

            cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))

            catList = []

            for i in cls.categoria:
                catList.append(Categoria(i))
            
            return catList

class DaoVenda:    
    @classmethod
    def salvar(cls, venda:Venda):
        with open('venda.txt','a') as    file_object:
            file_object.writelines(venda.itensVendidos.nome + "|" + venda.itensVendidos.preco + "|" + 
                                    venda.itensVendidos.categoria + "|" + 
                                    venda.vendedor + "|" + venda.cliente + "|" + str(venda.quantidadeVendida)
                                    + "|" + venda.data)
            file_object.writelines('\n')

    @classmethod
    def ler(cls):
        with open('venda.txt','r') as file_object:
            cls.venda = file_object.readlines()

        cls.venda = list(map(lambda x: x.replace('\n', ''), cls.venda))       
        cls.venda = list(map(lambda x: x.split('|'), cls.venda))
        
        listaVendas = []
        for i in cls.venda:
            listaVendas.append(Venda(Produto(i[0], i[1], i[2]), i[3], i[4], i[5],i[6]))

        return listaVendas

class DaoEstoque:
    @classmethod
    def salvar(cls, produto: Produto, quantidade):
        with open ('estoque.txt', 'a') as file_object:
            file_object.writelines(produto.nome + "|" + produto.preco + "|" +
                                   produto.categoria + "|" + str(quantidade))
            file_object.writelines('\n')

    @classmethod
    def ler(cls):
        with open('estoque.txt','r') as file_object:
            cls.estoque = file_object.readlines()

        cls.estoque = list(map(lambda x: x.replace ('\n',''), cls.estoque))
        cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))

        estoque_list= []
        if len(cls.estoque) > 0:
            for i in cls.estoque:
                estoque_list.append(Estoque(Produto(i[0],i[1], i[2], i[3])))

        return estoque_list
    
class DaoFornecedor:
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open('fornecedor.txt','a') as file_object:
            file_object.writelines(fornecedor.nome + "|" + fornecedor.cnpj + "|" + fornecedor.telefone + 
                                   "|" + fornecedor.categoria)
            file_object.writelines('\n')

    @classmethod
    def ler(cls):
        with open('fornecedores.txt', 'r') as file_object:
            cls.fornecedores = file_object.readlines()

        cls.fornecedores = list(map(lambda x: x.replace('\n', ''), cls.fornecedores))
        cls.fornecedores = list(map(lambda x: x.split('|'), cls.fornecedores))

        fornecedores_list = []
        for i in cls.fornecedores:
            fornecedores_list.append(Fornecedor(i[0],i[1],i[2],i[3]))
        
        return fornecedores_list
        
class DaoEmpregado:
    @classmethod
    def salvar(cls, empregado: Empregado):
        with open('empregado.txt','a') as file_object:
            file_object.writelines(empregado.nome + "|" + empregado.cnpj + "|" + empregado.telefone + 
                                   "|" + empregado.categoria)
            file_object.writelines('\n')

    @classmethod
    def ler(cls):
        with open('empregagos.txt', 'r') as file_object:
            cls.empregados = file_object.readlines()

        cls.empregados = list(map(lambda x: x.replace('\n', ''), cls.empregados))
        cls.empregados = list(map(lambda x: x.split('|'), cls.empregados))

        empregados_list = []
        for i in cls.empregados:
            empregados_list.append(Empregado(i[0],i[1],i[2],i[3]))
        
        return empregados_list


    