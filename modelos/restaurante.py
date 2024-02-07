class Restaurante:
    restaurantes = []  # Corrigido de resturantes para restaurantes

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)  # Corrigido de resturantes para restaurantes

    def __str__(self) -> str:
        return f'{self._nome} | {self.categoria}'

    @classmethod
    def listar_restaurantes(cls):  
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Status"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return 'ativo' if self._ativo else 'desativado'

    def alternar_estado(self):
            self._ativo = not self._ativo
restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('pizza Express', 'Pizza')

resturantes = [restaurante_pizza, restaurante_praca]

Restaurante.listar_restaurantes()
