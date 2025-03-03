import tkinter as tk
from tkinter import messagebox, scrolledtext

def abrir_conversor_decimal_binario():
    """Função para abrir a janela do conversor decimal-binário."""
    janela_conversor = tk.Toplevel()
    janela_conversor.title("Conversor Decimal-Binário")

    def decimal_para_binario(decimal):
        """Converte um número decimal para binário."""
        try:
            decimal = int(decimal)
            if decimal < 0:
                raise ValueError("Números negativos não são suportados.")
            binario = bin(decimal)[2:]  # Converte para binário e remove o prefixo '0b'
            explicacao.insert(tk.END, f"Conversão de {decimal} para binário:\n")
            explicacao.insert(tk.END, f"  {decimal} em binário é: {binario}\n")
            return binario
        except ValueError:
            raise ValueError("Por favor, insira um número decimal válido.")

    def binario_para_decimal(binario):
        """Converte um número binário para decimal."""
        try:
            if not all(c in "01" for c in binario):
                raise ValueError("Por favor, insira um número binário válido (apenas 0s e 1s).")
            decimal = int(binario, 2)  # Converte de binário para decimal
            explicacao.insert(tk.END, f"Conversão de {binario} para decimal:\n")
            explicacao.insert(tk.END, f"  {binario} em decimal é: {decimal}\n")
            return decimal
        except ValueError:
            raise ValueError("Por favor, insira um número binário válido.")

    def converter():
        """Função chamada quando o botão 'Converter' é pressionado."""
        try:
            explicacao.delete(1.0, tk.END)
            if modo.get() == "decimal_para_binario":
                decimal = entrada.get()
                binario = decimal_para_binario(decimal)
                resultado_label.config(text=f"O número {decimal} em binário é: {binario}")
            elif modo.get() == "binario_para_decimal":
                binario = entrada.get()
                decimal = binario_para_decimal(binario)
                resultado_label.config(text=f"O binário {binario} em decimal é: {decimal}")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def limpar():
        """Função chamada quando o botão 'Limpar' é pressionado."""
        entrada.delete(0, tk.END)
        explicacao.delete(1.0, tk.END)
        resultado_label.config(text="")

    # Interface do conversor
    modo = tk.StringVar(value="decimal_para_binario")

    rotulo = tk.Label(janela_conversor, text="Digite um número decimal ou binário:")
    rotulo.pack(pady=10)

    entrada = tk.Entry(janela_conversor)
    entrada.pack(pady=10)

    frame_modo = tk.Frame(janela_conversor)
    frame_modo.pack(pady=10)

    tk.Radiobutton(frame_modo, text="Decimal para Binário", variable=modo, value="decimal_para_binario").pack(side=tk.LEFT, padx=5)
    tk.Radiobutton(frame_modo, text="Binário para Decimal", variable=modo, value="binario_para_decimal").pack(side=tk.LEFT, padx=5)

    frame_botoes = tk.Frame(janela_conversor)
    frame_botoes.pack(pady=10)

    botao_converter = tk.Button(frame_botoes, text="Converter", command=converter)
    botao_converter.pack(side=tk.LEFT, padx=5)

    botao_limpar = tk.Button(frame_botoes, text="Limpar", command=limpar)
    botao_limpar.pack(side=tk.LEFT, padx=5)

    resultado_label = tk.Label(janela_conversor, text="", justify="left")
    resultado_label.pack(pady=10)

    explicacao = scrolledtext.ScrolledText(janela_conversor, width=50, height=10, wrap=tk.WORD)
    explicacao.pack(pady=10)