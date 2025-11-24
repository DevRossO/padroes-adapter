class CarregadorMicroUSB:
    def carregar_micro_usb(self):
        print("Carregando via Micro-USB...")

class Celular:
    def carregar(self, carregador):
        carregador.carregar_usb_c()

carregador_antigo = CarregadorMicroUSB()
celular = Celular()

celular.carregar(carregador_antigo) 
