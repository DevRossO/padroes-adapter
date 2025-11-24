# Padrão de Projeto: Adapter (Python)

## 📌 Visão Geral

O padrão **Adapter** é um padrão estrutural do catálogo *GoF* que permite que dois sistemas com **interfaces incompatíveis** funcionem juntos.  
Ele atua como um **"tradutor"** entre duas classes, convertendo a interface de uma classe existente para outra interface esperada pelo cliente.

---

## 🎯 Problema que o Adapter Resolve
O cliente (celular) só entende o método:
carregar_usb_c()

Mas o carregador antigo oferece apenas:
fornecer_energia_usb_a()

Sem o Adapter:

* O celular não tem como usar o carregador antigo
* Seria necessário alterar código legado
* O sistema fica acoplado e difícil de manter

Com o Adapter:

* Criamos uma classe intermediária
* Ela traduz USB-C → USB-A
* O cliente continua esperando apenas USB-C
* O carregador antigo funciona sem ser modificado

classDiagram
    class Celular {
        +carregar(carregador)
    }

    class CarregadorUSBC {
        +carregar_usb_c()
    }

    class CarregadorUSBA {
        +fornecer_energia_usb_a()
    }

    class AdapterUSBCtoA {
        -carregador_antigo: CarregadorUSBA
        +carregar_usb_c()
    }

    Celular --> CarregadorUSBC
    Celular --> AdapterUSBCtoA

    AdapterUSBCtoA --|> CarregadorUSBC
    AdapterUSBCtoA --> CarregadorUSBA

