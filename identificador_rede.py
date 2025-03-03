import tkinter as tk
from tkinter import messagebox, scrolledtext
import ipaddress

def abrir_identificador_rede():
    """Função para abrir a janela do identificador de rede."""
    janela_identificador = tk.Toplevel()
    janela_identificador.title("Identificador de Rede")

    def identificar_rede():
        """Identifica a máscara e o IP da rede com base na entrada CIDR."""
        try:
            explicacao.delete(1.0, tk.END)
            entrada_cidr = entrada.get()
            
            # Cria um objeto IPv4Network com a entrada CIDR
            rede = ipaddress.IPv4Network(entrada_cidr, strict=False)
            
            # Exibe as informações
            explicacao.insert(tk.END, f"Informações para {entrada_cidr}:\n\n")
            explicacao.insert(tk.END, f"1. Endereço de rede:\n")
            explicacao.insert(tk.END, f"   {rede.network_address}\n\n")
            explicacao.insert(tk.END, f"2. Máscara de sub-rede:\n")
            explicacao.insert(tk.END, f"   {rede.netmask}\n\n")
            explicacao.insert(tk.END, f"3. Endereço de broadcast:\n")
            explicacao.insert(tk.END, f"   {rede.broadcast_address}\n\n")
            explicacao.insert(tk.END, f"4. Quantidade de IPs disponíveis:\n")
            explicacao.insert(tk.END, f"   {rede.num_addresses - 2}\n\n")
            explicacao.insert(tk.END, f"5. Intervalo de IPs válidos:\n")
            explicacao.insert(tk.END, f"   {rede.network_address + 1} - {rede.broadcast_address - 1}\n\n")
            
            resultado_label.config(text=(
                f"Endereço de rede: {rede.network_address}\n"
                f"Máscara de sub-rede: {rede.netmask}\n"
                f"Endereço de broadcast: {rede.broadcast_address}\n"
                f"Quantidade de IPs disponíveis: {rede.num_addresses - 2}\n"
                f"Intervalo de IPs válidos: {rede.network_address + 1} - {rede.broadcast_address - 1}"
            ))
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def limpar():
        """Função chamada quando o botão 'Limpar' é pressionado."""
        entrada.delete(0, tk.END)
        explicacao.delete(1.0, tk.END)
        resultado_label.config(text="")

    # Interface do identificador de rede
    rotulo = tk.Label(janela_identificador, text="Digite um endereço de rede no formato CIDR (ex: 192.168.1.0/24):")
    rotulo.pack(pady=10)

    entrada = tk.Entry(janela_identificador)
    entrada.pack(pady=10)

    frame_botoes = tk.Frame(janela_identificador)
    frame_botoes.pack(pady=10)

    botao_identificar = tk.Button(frame_botoes, text="Identificar", command=identificar_rede)
    botao_identificar.pack(side=tk.LEFT, padx=5)

    botao_limpar = tk.Button(frame_botoes, text="Limpar", command=limpar)
    botao_limpar.pack(side=tk.LEFT, padx=5)

    resultado_label = tk.Label(janela_identificador, text="", justify="left")
    resultado_label.pack(pady=10)

    explicacao = scrolledtext.ScrolledText(janela_identificador, width=70, height=20, wrap=tk.WORD)
    explicacao.pack(pady=10)