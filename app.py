from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

Restaurante_praca = Restaurante('praça','Gourmet')

bebida_suco = Bebida('Suco de Melancia',5.0, 'grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Paozinho',2.00, 'O Melhor pão da cidade')
prato_paozinho.aplicar_desconto()

Restaurante_praca.adicionar_no_cardapio(bebida_suco)
Restaurante_praca.adicionar_no_cardapio(prato_paozinho)

def main():
   Restaurante_praca.exibir_cardapio
   
if __name__ == '__main__':
    main()