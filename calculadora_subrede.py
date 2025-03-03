import tkinter as tk
from tkinter import messagebox, scrolledtext
import ipaddress

def abrir_calculadora():
    """Função para abrir a janela da calculadora de sub-rede."""
    janela_calculadora = tk.Toplevel()
    janela_calculadora.title("Calculadora de Sub-Rede")

    # Funções da calculadora (já implementadas anteriormente)
    def calcular_subrede():
        try:
            explicacao.delete(1.0, tk.END)
            ip = entrada_ip.get()
            mascara = entrada_mascara.get()
            if not ip or not mascara:
                raise ValueError("Por favor, insira o IP e a máscara de sub-rede.")
            rede = ipaddress.IPv4Network(f"{ip}/{mascara}", strict=False)
            explicacao.insert(tk.END, f"Calculando informações para o IP {ip} com máscara {mascara}:\n\n")
            explicacao.insert(tk.END, f"1. Endereço de rede:\n")
            explicacao.insert(tk.END, f"   Endereço de rede: {rede.network_address}\n\n")
            explicacao.insert(tk.END, f"2. Máscara de sub-rede:\n")
            explicacao.insert(tk.END, f"   Máscara de sub-rede: {rede.netmask}\n\n")
            explicacao.insert(tk.END, f"3. Endereço de broadcast:\n")
            explicacao.insert(tk.END, f"   Endereço de broadcast: {rede.broadcast_address}\n\n")
            ips_disponiveis = rede.num_addresses - 2
            explicacao.insert(tk.END, f"4. Quantidade de IPs disponíveis:\n")
            explicacao.insert(tk.END, f"   IPs disponíveis: {ips_disponiveis}\n\n")
            ip_inicial = rede.network_address + 1
            ip_final = rede.broadcast_address - 1
            explicacao.insert(tk.END, f"5. Intervalo de IPs válidos:\n")
            explicacao.insert(tk.END, f"   Intervalo de IPs válidos: {ip_inicial} - {ip_final}\n\n")
            resultado_label.config(text=(
                f"Endereço de rede: {rede.network_address}\n"
                f"Máscara de sub-rede: {rede.netmask}\n"
                f"Endereço de broadcast: {rede.broadcast_address}\n"
                f"Quantidade de IPs disponíveis: {ips_disponiveis}\n"
                f"Intervalo de IPs válidos: {ip_inicial} - {ip_final}"
            ))
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def limpar():
        entrada_ip.delete(0, tk.END)
        entrada_mascara.delete(0, tk.END)
        explicacao.delete(1.0, tk.END)
        resultado_label.config(text="")

    # Interface da calculadora
    rotulo_ip = tk.Label(janela_calculadora, text="Digite um endereço IP (ex: 192.168.1.10):")
    rotulo_ip.pack(pady=5)

    entrada_ip = tk.Entry(janela_calculadora)
    entrada_ip.pack(pady=5)

    rotulo_mascara = tk.Label(janela_calculadora, text="Digite a máscara de sub-rede (ex: 255.255.255.0):")
    rotulo_mascara.pack(pady=5)

    entrada_mascara = tk.Entry(janela_calculadora)
    entrada_mascara.pack(pady=5)

    frame_botoes = tk.Frame(janela_calculadora)
    frame_botoes.pack(pady=10)

    botao_calcular = tk.Button(frame_botoes, text="Calcular", command=calcular_subrede)
    botao_calcular.pack(side=tk.LEFT, padx=5)

    botao_limpar = tk.Button(frame_botoes, text="Limpar", command=limpar)
    botao_limpar.pack(side=tk.LEFT, padx=5)

    resultado_label = tk.Label(janela_calculadora, text="", justify="left")
    resultado_label.pack(pady=10)

    explicacao = scrolledtext.ScrolledText(janela_calculadora, width=70, height=20, wrap=tk.WORD)
    explicacao.pack(pady=10)