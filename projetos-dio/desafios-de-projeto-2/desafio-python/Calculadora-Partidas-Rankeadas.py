import tkinter as tk
from tkinter import messagebox

# Função para calcular o nível baseado no número de vitórias
def calcular_nivel(vitorias):
    if vitorias < 10:
        return "Ferro", "gray"
    elif 10 <= vitorias <= 20:
        return "Bronze", "brown"
    elif 21 <= vitorias <= 50:
        return "Prata", "silver"
    elif 51 <= vitorias <= 80:
        return "Ouro", "gold"
    elif 81 <= vitorias <= 90:
        return "Diamante", "blue"
    elif 91 <= vitorias <= 100:
        return "Lendário", "purple"
    else:
        return "Imortal", "red"

# Função para exibir o resultado na interface
def mostrar_resultado():
    try:
        vitorias = int(entry_vitorias.get())
        derrotas = int(entry_derrotas.get())
        saldo = vitorias - derrotas
        nivel, cor = calcular_nivel(vitorias)
        resultado_label.config(text=f"O Herói tem um saldo de partidas {saldo} e está classificado como {nivel}.", fg=cor)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Função para sair da aplicação
def sair():
    root.destroy()

# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora de Partidas Rankeadas")
root.geometry("600x300")
root.configure(bg="black")

# Labels e entradas para vitórias e derrotas
tk.Label(root, text="Digite o número de vitórias:", fg="green", bg="black").pack(pady=10)
entry_vitorias = tk.Entry(root)
entry_vitorias.pack()

tk.Label(root, text="Digite o número de derrotas:", fg="red", bg="black").pack(pady=10)
entry_derrotas = tk.Entry(root)
entry_derrotas.pack()

# Botão para calcular o resultado
tk.Button(root, text="Calcular", command=mostrar_resultado).pack(pady=20)

# Label para mostrar o resultado
resultado_label = tk.Label(root, text="", fg="white", bg="black")
resultado_label.pack(pady=10)

# Botão para sair
tk.Button(root, text="Sair", command=sair).pack(pady=20)

# Iniciar a interface gráfica
root.mainloop()
