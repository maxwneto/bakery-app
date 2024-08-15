from models import *
from dao import *
from datetime import datetime

class ControllerCategoria:
    def cadastraCategoria(self, novaCategoria):
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
        cat = list(filter(lambda x: x.categoria == categoriaRemover, x))
        
        if len(cat) == 0:
            print('A categoria que você deseja remover não existe.')
        else:
            for i in range(len(x)):
                if x[i].categoria ==  categoriaRemover:
                    del x[i]
                    break
            print('Categoria removida com sucesso')

            with open('categoria.txt','w') as file_object:
                for i in x:
                    file_object.writelines(i.categoria)
                    file_object.writelines('\n')
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



a = ControllerCategoria()
a.mostrarCategorias()
