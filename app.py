from modelos.restaurante import Restaurante

Restaurante_praca = Restaurante('praça','Gourmet')

Restaurante_praca.receber_avaliacao('Guilherme',10)
Restaurante_praca.receber_avaliacao('Fernanda',8)
Restaurante_praca.receber_avaliacao('Pedro',2)

def main():
   Restaurante.listar_restaurantes()
   
if __name__ == '__main__':
    main()