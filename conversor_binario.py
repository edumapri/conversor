import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk

def abrir_conversor():
    """Função para abrir a janela do conversor binário."""
    janela_conversor = tk.Toplevel()
    janela_conversor.title("Conversor octeto com valor Decimal ou binário")

    # Funções do conversor (já implementadas anteriormente)
    def octeto_para_binario(octeto, explicacao):
        if octeto < 0 or octeto > 255:
            raise ValueError("Octeto deve estar entre 0 e 255.")
        binario = ""
        explicacao.insert(tk.END, f"Convertendo o octeto {octeto} para binário:\n")
        for i in range(7, -1, -1):
            bit = (octeto >> i) & 1
            binario += str(bit)
            explicacao.insert(tk.END, f"  Bit {7 - i}: {octeto} >> {i} = {octeto >> i} (bit {bit})\n")
        explicacao.insert(tk.END, f"O octeto {octeto} em binário é: {binario}\n")
        return binario

    def binario_para_octeto(binario, explicacao):
        if len(binario) != 8 or not all(c in "01" for c in binario):
            raise ValueError("O binário deve ter exatamente 8 bits (0s e 1s).")
        decimal = 0
        explicacao.insert(tk.END, f"Convertendo o binário {binario} para decimal:\n")
        for i, bit in enumerate(binario[::-1]):
            if bit == '1':
                decimal += 2 ** i
            explicacao.insert(tk.END, f"  Bit {i}: {bit} * 2^{i} = {int(bit) * (2 ** i)}\n")
        explicacao.insert(tk.END, f"O binário {binario} em decimal é: {decimal}\n")
        return decimal

    def ip_para_binario(ip, explicacao):
        octetos = ip.split(".")
        if len(octetos) != 4:
            raise ValueError("O valor deve conter exatamente 4 octetos.")
        binario_total = []
        for octeto in octetos:
            try:
                octeto_int = int(octeto)
                binario_octeto = octeto_para_binario(octeto_int, explicacao)
                binario_total.append(binario_octeto)
            except ValueError:
                raise ValueError(f"Octeto inválido: {octeto}")
        return ".".join(binario_total)

    def binario_para_ip(binario_ip, explicacao):
        octetos_binarios = binario_ip.split(".")
        if len(octetos_binarios) != 4:
            raise ValueError("O endereço binário deve conter exatamente 4 octetos.")
        ip_total = []
        for binario in octetos_binarios:
            try:
                octeto_decimal = binario_para_octeto(binario, explicacao)
                ip_total.append(str(octeto_decimal))
            except ValueError:
                raise ValueError(f"Binário inválido: {binario}")
        return ".".join(ip_total)

    def converter():
        try:
            explicacao.delete(1.0, tk.END)
            if modo.get() == "decimal_para_binario":
                ip = entrada.get()
                binario_ip = ip_para_binario(ip, explicacao)
                resultado_label.config(text=f"O IP {ip} em binário é:\n{binario_ip}")
            elif modo.get() == "binario_para_decimal":
                binario_ip = entrada.get()
                ip_decimal = binario_para_ip(binario_ip, explicacao)
                resultado_label.config(text=f"O binário {binario_ip} em decimal é:\n{ip_decimal}")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def limpar():
        entrada.delete(0, tk.END)
        explicacao.delete(1.0, tk.END)
        resultado_label.config(text="")

    # Interface do conversor
    modo = tk.StringVar(value="decimal_para_binario")

    rotulo = tk.Label(janela_conversor, text="Digite um valor (ex: 192.168.1.55 ou 255.255.0.0) ou binário (ex: 11000000.10101000.00000001.00110111):")
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

    explicacao = scrolledtext.ScrolledText(janela_conversor, width=70, height=20, wrap=tk.WORD)
    explicacao.pack(pady=10)