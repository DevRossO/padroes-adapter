class CarregadorUSBC:
    def carregar_usb_c(self):
        raise NotImplementedError()

class CarregadorMicroUSB:
    def carregar_micro_usb(self):
        print("Carregando via Micro-USB...")

class AdapterMicroUSB(CarregadorUSBC):
    def __init__(self, carregador):
        self.carregador = carregador

    def carregar_usb_c(self):
        print("Adaptando USB-C → Micro-USB")
        self.carregador.carregar_micro_usb()

class Celular:
    def carregar(self, carregador: CarregadorUSBC):
        carregador.carregar_usb_c()

carregador_antigo = CarregadorMicroUSB()
adapter = AdapterMicroUSB(carregador_antigo)

celular = Celular()
celular.carregar(adapter)
