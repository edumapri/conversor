import tkinter as tk
from tkinter import messagebox, scrolledtext

def abrir_conversor_mascara_rede():
    """Função para abrir a janela do conversor de máscara de rede."""
    janela_conversor = tk.Toplevel()
    janela_conversor.title("Conversor de Máscara de Rede")

    def cidr_para_decimal(cidr):
        """Converte uma máscara CIDR (ex: /24) para notação decimal (ex: 255.255.255.0)."""
        try:
            cidr = int(cidr)
            if cidr < 0 or cidr > 32:
                raise ValueError("O valor CIDR deve estar entre 0 e 32.")
            bits = "1" * cidr + "0" * (32 - cidr)  # Cria a máscara em binário
            octetos = [bits[i:i+8] for i in range(0, 32, 8)]  # Divide em 4 octetos
            decimal = ".".join(str(int(octeto, 2)) for octeto in octetos)  # Converte cada octeto para decimal
            explicacao.insert(tk.END, f"Conversão de /{cidr} para decimal:\n")
            explicacao.insert(tk.END, f"  /{cidr} em decimal é: {decimal}\n")
            return decimal
        except ValueError:
            raise ValueError("Por favor, insira um valor CIDR válido (0 a 32).")

    def decimal_para_cidr(decimal):
        """Converte uma máscara decimal (ex: 255.255.255.0) para notação CIDR (ex: /24)."""
        try:
            octetos = decimal.split(".")
            if len(octetos) != 4:
                raise ValueError("A máscara deve conter exatamente 4 octetos.")
            bits = ""
            for octeto in octetos:
                octeto_int = int(octeto)
                if octeto_int < 0 or octeto_int > 255:
                    raise ValueError("Cada octeto deve estar entre 0 e 255.")
                bits += f"{octeto_int:08b}"  # Converte cada octeto para binário de 8 bits
            cidr = bits.count("1")  # Conta os bits '1' para obter o valor CIDR
            explicacao.insert(tk.END, f"Conversão de {decimal} para CIDR:\n")
            explicacao.insert(tk.END, f"  {decimal} em CIDR é: /{cidr}\n")
            return cidr
        except ValueError:
            raise ValueError("Por favor, insira uma máscara decimal válida.")

    def converter():
        """Função chamada quando o botão 'Converter' é pressionado."""
        try:
            explicacao.delete(1.0, tk.END)
            if modo.get() == "cidr_para_decimal":
                cidr = entrada.get().strip("/")
                decimal = cidr_para_decimal(cidr)
                resultado_label.config(text=f"A máscara /{cidr} em decimal é: {decimal}")
            elif modo.get() == "decimal_para_cidr":
                decimal = entrada.get()
                cidr = decimal_para_cidr(decimal)
                resultado_label.config(text=f"A máscara {decimal} em CIDR é: /{cidr}")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def limpar():
        """Função chamada quando o botão 'Limpar' é pressionado."""
        entrada.delete(0, tk.END)
        explicacao.delete(1.0, tk.END)
        resultado_label.config(text="")

    # Interface do conversor
    modo = tk.StringVar(value="cidr_para_decimal")

    rotulo = tk.Label(janela_conversor, text="Digite uma máscara CIDR (ex: /24) ou decimal (ex: 255.255.255.0):")
    rotulo.pack(pady=10)

    entrada = tk.Entry(janela_conversor)
    entrada.pack(pady=10)

    frame_modo = tk.Frame(janela_conversor)
    frame_modo.pack(pady=10)

    tk.Radiobutton(frame_modo, text="CIDR para Decimal", variable=modo, value="cidr_para_decimal").pack(side=tk.LEFT, padx=5)
    tk.Radiobutton(frame_modo, text="Decimal para CIDR", variable=modo, value="decimal_para_cidr").pack(side=tk.LEFT, padx=5)

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