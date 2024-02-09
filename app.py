from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

Restaurante_praca = Restaurante('praça','Gourmet')
bebida_suco = Bebida('Suco de Melancia',5.0, 'grande')
prato_paozinho = Prato('Paozinho',2.00, 'O Melhor pão da cidade')

def main():
   print(bebida_suco._nome)
   print(prato_paozinho._nome)
   
if __name__ == '__main__':
    main()