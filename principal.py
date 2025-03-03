import tkinter as tk
from tkinter import messagebox
from conversor_decimal_binario import abrir_conversor_decimal_binario
from conversor_binario import abrir_conversor
from calculadora_subrede import abrir_calculadora
from conversor_mascara_rede import abrir_conversor_mascara_rede
from identificador_rede import abrir_identificador_rede

def abrir_conversor_ip_binario():
    """Abre a janela do conversor  binário."""
    abrir_conversor()

def abrir_calculadora_subrede():
    """Abre a janela da calculadora de sub-rede."""
    abrir_calculadora()

# Configuração da janela principal
janela_principal = tk.Tk()
janela_principal.title("Escolha o Programa")

# Rótulo de instrução
rotulo = tk.Label(janela_principal, text="Escolha um programa para abrir:")
rotulo.pack(pady=20)

# Botão para abrir o conversor decimal-binário
botao_conversor_decimal_binario = tk.Button(
    janela_principal,
    text="Conversor Decimal-Binário",
    command=abrir_conversor_decimal_binario
)
botao_conversor_decimal_binario.pack(pady=10)


# Botão para abrir o conversor de IP para binário
botao_conversor = tk.Button(janela_principal, text="Conversor Octeto Decimal ou Binário", command=abrir_conversor_ip_binario)
botao_conversor.pack(pady=10)

# Botão para abrir a calculadora de sub-rede
botao_calculadora = tk.Button(janela_principal, text="Identificador dos Octetos de Rede", command=abrir_calculadora_subrede)
botao_calculadora.pack(pady=10)

# Botão para abrir o conversor de máscara de rede
botao_conversor_mascara_rede = tk.Button(
    janela_principal,
    text="Conversor de Máscara de Rede CDR",
    command=abrir_conversor_mascara_rede
)
botao_conversor_mascara_rede.pack(pady=10)

# Botão para abrir o identificador de rede
botao_identificador_rede = tk.Button(
    janela_principal,
    text="Identificador de Rede CDR",
    command=abrir_identificador_rede
)
botao_identificador_rede.pack(pady=10)

# Iniciar a interface gráfica
janela_principal.mainloop()