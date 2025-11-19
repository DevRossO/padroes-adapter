# Padrão de Projeto: Adapter (Python)

## 📌 Visão Geral

O padrão **Adapter** é um padrão estrutural do catálogo *GoF* que permite que dois sistemas com **interfaces incompatíveis** funcionem juntos.  
Ele atua como um **"tradutor"** entre duas classes, convertendo a interface de uma classe existente para outra interface esperada pelo cliente.

---

## 🎯 Problema que o Adapter Resolve

Imagine que o seu sistema espera trabalhar com um método chamado `conectar_usb_c()`, mas você precisa usar um módulo legado que só possui o método `conectar_usb_a()`.

Sem o Adapter:
- o código fica acoplado ao sistema antigo  
- você precisa alterar a classe existente  
- a manutenção fica ruim  

Com o Adapter:
- você cria uma classe intermediária  
- ela traduz chamadas modernas → para chamadas antigas  
- o cliente não precisa saber que existe um sistema legado  

---

## 📐 Estrutura (Diagrama)

```mermaid
classDiagram
    class Cliente {
        +usar_dispositivo(entrada)
    }

    class EntradaModerna {
        +conectar_usb_c()
    }

    class EntradaAntiga {
        +conectar_usb_a()
    }

    class AdapterEntrada {
        -entrada_antiga: EntradaAntiga
        +conectar_usb_c()
    }

    Cliente --> EntradaModerna
    AdapterEntrada --|> EntradaModerna
    AdapterEntrada --> EntradaAntiga