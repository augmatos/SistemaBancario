# 🏦 Sistema Bancário

> Sistema bancário orientado a objetos em Python demonstrando abstração, herança, encapsulamento e polimorfismo

---

## 📌 Sobre o Projeto

**Sistema Bancário** é uma implementação educacional de um sistema bancário simplificado em Python. O projeto foi desenvolvido como exercício prático dos **4 pilares da Programação Orientada a Objetos (OOP)**:

- ✅ **Abstração** — classes abstratas definem contratos
- ✅ **Herança** — reutilização de código através de hierarquias de classes
- ✅ **Encapsulamento** — proteção de dados com properties
- ✅ **Polimorfismo** — métodos implementados de formas diferentes

---

## 🏗️ Arquitetura do Sistema

### Diagrama de Classes

```
                    ┌─────────────┐
                    │   Pessoa    │
                    │─────────────│
                    │ -nome       │
                    │ -idade      │
                    └──────┬──────┘
                           │
                           │ herda
                           │
                    ┌──────▼──────┐
                    │   Cliente   │
                    │─────────────│
                    │ +conta      │
                    │ +inserir_.. │
                    └─────────────┘


        ┌───────────────────────────────────┐
        │      Conta (Abstrata)             │
        │───────────────────────────────────│
        │ -agencia, -conta, -saldo          │
        │ +depositar(valor)                 │
        │ +sacar(valor) [abstrato]          │
        │ +detalhes()                       │
        └────┬──────────────────────┬───────┘
             │ herda                │ herda
             │                      │
   ┌─────────▼─────────┐  ┌────────▼─────────┐
   │  ContaPoupanca    │  │  ContaCorrente   │
   │───────────────────│  │──────────────────│
   │ +sacar(valor)     │  │ -limite = 900    │
   │ (sem limite)      │  │ +sacar(valor)    │
   │                   │  │ (com limite)     │
   └───────────────────┘  └──────────────────┘


┌──────────────────────────┐
│      Banco               │
│──────────────────────────│
│ -agencias = [...]        │
│ -clientes = []           │
│ -contas = []             │
│ +inserir_cliente()       │
│ +inserir_conta()         │
│ +autenticar(cliente)     │
└──────────────────────────┘
```

---

## 📂 Estrutura do Projeto

```
SistemaBancario/
│
├── cliente.py        # Herda de Pessoa
├── conta.py          # Classes abstratas e concretas de conta
├── banco.py          # Entidade Banco
└── main.py           # Demonstração de uso
```

---

## 🔍 Componentes Principais

### 1️⃣ Pessoa (Classe Base)

```python
class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome      # Encapsulamento: atributo privado
        self._idade = idade
    
    @property              # Property para acesso controlado
    def nome(self):
        return self._nome
```

**Conceitos:** Encapsulamento, Properties

---

### 2️⃣ Cliente (Herança)

```python
class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)  # Chama construtor da classe pai
        self.conta = None
    
    def inserir_conta(self, conta):
        self.conta = conta
```

**Conceitos:** Herança, `super()`, Composição

---

### 3️⃣ Conta (Abstração)

```python
from abc import ABC, abstractmethod

class Conta(ABC):  # Classe abstrata
    @abstractmethod
    def sacar(self, valor): pass  # Método abstrato
```

**Conceitos:** Abstração, Classes abstratas, Métodos abstratos

---

### 4️⃣ Polimorfismo: ContaPoupanca vs ContaCorrente

```python
# Conta Poupança - sem limite
class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente')
        else:
            self.saldo -= valor

# Conta Corrente - com limite de R$ 900
class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=900):
        super().__init__(agencia, conta, saldo)
        self.limite = limite
    
    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:  # Usa o limite
            print('Saldo insuficiente')
        else:
            self.saldo -= valor
```

**Conceitos:** Polimorfismo, Sobrescrita de métodos, Argumentos com valor padrão

---

## 🚀 Como Usar

### Pré-requisitos
- Python 3.x instalado

### Execução
```bash
python main.py
```

### Exemplo de Uso Personalizado

```python
from banco import Banco
from cliente import Cliente
from conta import ContaPoupanca, ContaCorrente

# Criar banco
banco = Banco()

# Criar cliente
cliente = Cliente('Augusto', 23)

# Criar conta poupança
conta_poupanca = ContaPoupanca(11111, 125976, 1000)

# Associar conta ao cliente
cliente.inserir_conta(conta_poupanca)

# Registrar no banco
banco.inserir_cliente(cliente)
banco.inserir_conta(conta_poupanca)

# Validar e usar conta
if banco.autenticar(cliente):
    cliente.conta.depositar(500)  # Deposita R$ 500
    cliente.conta.sacar(200)      # Saca R$ 200
```

---

## 📊 Demonstração do Sistema

```
# Saída do programa:
Agencia: 11111 Conta: 125976 Saldo: 0 
Agencia: 11111 Conta: 125976 Saldo: -20 
####################
Agencia: 22222 Conta: 486521 Saldo: 0 
Agencia: 22222 Conta: 486521 Saldo: -20 
####################
Cliente não autenticado.
```

---

## 🛠️ Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

**Módulos:**
- `abc` — Classes abstratas e métodos abstratos

---

## 📚 Conceitos de OOP Aplicados

| Pilar | Definição | Implementação |
|-------|-----------|---------------|
| **Abstração** | Esconder detalhes complexos | Classe `Conta` abstrata define interface |
| **Herança** | Reutilizar código via hierarquia | `Cliente` herda de `Pessoa` |
| **Encapsulamento** | Proteger dados internos | Atributos `_nome`, `_idade` com @property |
| **Polimorfismo** | Mesmo método, comportamentos diferentes | `sacar()` varia em ContaPoupanca vs ContaCorrente |

---

## 💡 Funcionalidades

- ✅ Criar clientes
- ✅ Criar contas (poupança ou corrente)
- ✅ Fazer depósitos
- ✅ Sacar dinheiro (com validação de saldo)
- ✅ Contas correntes com limite extra
- ✅ Autenticar cliente no banco
- ✅ Visualizar detalhes da conta

---

## 🔮 Possíveis Extensões

- [ ] Sistema de transações (histórico)
- [ ] Juros em contas poupança
- [ ] Transferências entre contas
- [ ] Persistência em banco de dados (SQLite)
- [ ] Interface gráfica com Tkinter
- [ ] API REST com Flask
- [ ] Testes unitários com pytest
- [ ] Sistema de autenticação com senha

---

## 🎓 Exemplo de Saída Esperada

```
# Cliente 1 - Conta Poupança (agência válida)
Agencia: 11111 Conta: 125976 Saldo: 0 
Agencia: 11111 Conta: 125976 Saldo: -20 
####################

# Cliente 2 - Conta Corrente (agência válida, com limite)
Agencia: 22222 Conta: 486521 Saldo: 0 
Agencia: 22222 Conta: 486521 Saldo: -20 
####################

# Cliente 3 - Conta em agência não registrada (falha autenticação)
Cliente não autenticado.
```

---

## 👨‍💻 Autor

**Augusto Matos** — Analista de Dados & Desenvolvedor Python

[![LinkedIn](https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/augusto-matos-b92887204)
[![Gmail](https://img.shields.io/badge/Outlook-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white)](mailto:augusto.ivan83@outlook.com)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/augmatos)

---

## 📝 Licença

Este projeto é de código aberto e disponível para fins educacionais.

---

## 🔗 Referências Úteis

- [Python OOP - Documentação Oficial](https://docs.python.org/3/tutorial/classes.html)
- [ABC - Abstract Base Classes](https://docs.python.org/3/library/abc.html)
- [Python Properties](https://docs.python.org/3/library/functions.html#property)
