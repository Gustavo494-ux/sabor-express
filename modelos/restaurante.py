class Restaurante:
    resturantes = []
    
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria= categoria
        self.ativo = False
        Restaurante.resturantes.append(self)
        
    def __str__(self) -> str:
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():  
        for restaurante in Restaurante.resturantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

restaurante_praca = Restaurante('Praça','Gourmet')
restaurante_pizza = Restaurante('Pizza Express','Pizza')

# resturantes = [restaurante_pizza,restaurante_praca]

# print(restaurante_pizza)
# print(restaurante_praca)


Restaurante.listar_restaurantes()