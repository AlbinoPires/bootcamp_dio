import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Função para exibir a mensagem de agradecimento e fechar a janela
def sair():
    nome = entry_nome.get()
    messagebox.showinfo("Obrigado!", f"Obrigado pela interação, {nome}! Você é o maior herói dessa jornada!")
    janela.quit()  # Fecha a janela após a interação

# Função que será chamada ao final da interação
def finalizar_interacao():
    nome = entry_nome.get()
    idade = entry_idade.get()
    tipo_heroi = var_tipo.get()

    if not nome or not idade or not tipo_heroi:
        messagebox.showwarning("Aviso", "Preencha todos os campos!")
        return

    # Função de ataque personalizada
    def atacar():
        ataque = ""
        if tipo_heroi.lower() == 'mago':
            ataque = 'usou sua magia ensinada por Merlin'
        elif tipo_heroi.lower() == 'guerreiro':
            ataque = 'usou sua espada sagrada Templária'
        elif tipo_heroi.lower() == 'monge':
            ataque = 'usou suas artes marciais Kong-Fu'
        elif tipo_heroi.lower() == 'ninja':
            ataque = 'usou suas técnicas Shuriken'
        else:
            ataque = 'realizou um ataque comum'

        # Saída personalizada
        return f"O {tipo_heroi.capitalize()} {nome} atacou usando {ataque}\nClasse do Herói: {tipo_heroi.capitalize()} - Nome: {nome} - Idade: {idade}"

    # Exibe a mensagem personalizada do ataque na janela principal
    resultado = atacar()
    label_resultado.config(text=resultado)

# Configurando a janela principal
janela = tk.Tk()
janela.title("Jogo de Heróis")
janela.geometry("600x400")

# Definindo a imagem de fundo
bg_image = Image.open("fundopython.jpg")  # Nome do fundo ajustado
bg_image = bg_image.resize((600, 400), Image.ANTIALIAS)
bg = ImageTk.PhotoImage(bg_image)

# Canvas para exibir a imagem de fundo
canvas = tk.Canvas(janela, width=600, height=400)
canvas.pack(fill="both", expand=True)

# Exibindo a imagem no fundo
canvas.create_image(0, 0, image=bg, anchor="nw")

# Adicionando os widgets de interação com fundo preto e fonte metálica

# Caixa de fundo para "Bem-vindo ao Jogo dos Heróis!"
label_bemvindo = tk.Label(janela, text="Bem-vindo ao Jogo dos Heróis!", font=("Arial", 18), bg="black", fg="gold")
canvas.create_window(300, 50, window=label_bemvindo)

# Caixa de fundo para "Nome do Herói"
label_nome = tk.Label(janela, text="Nome do Herói:", font=("Arial", 12), bg="black", fg="gold")
canvas.create_window(150, 100, window=label_nome)

# Caixa de entrada para Nome
entry_nome = tk.Entry(janela, bg="black", fg="gold")
canvas.create_window(350, 100, window=entry_nome)

# Caixa de fundo para "Idade do Herói"
label_idade = tk.Label(janela, text="Idade do Herói:", font=("Arial", 12), bg="black", fg="gold")
canvas.create_window(150, 140, window=label_idade)

# Caixa de entrada para Idade
entry_idade = tk.Entry(janela, bg="black", fg="gold")
canvas.create_window(350, 140, window=entry_idade)

# Caixa de fundo para "Escolha o tipo de Herói"
label_tipo = tk.Label(janela, text="Escolha o tipo de Herói:", font=("Arial", 12), bg="black", fg="gold")
canvas.create_window(150, 180, window=label_tipo)

# Opções de tipo de herói
var_tipo = tk.StringVar(value="Mago")
tipos_heroi = ["Mago", "Guerreiro", "Monge", "Ninja"]
dropdown = tk.OptionMenu(janela, var_tipo, *tipos_heroi)
dropdown.config(bg="black", fg="gold")
canvas.create_window(350, 180, window=dropdown)

# Label para exibir o resultado do ataque
label_resultado = tk.Label(janela, text="", font=("Arial", 12), bg="black", fg="gold")
canvas.create_window(300, 300, window=label_resultado)

# Botão para finalizar a interação
botao_finalizar = tk.Button(janela, text="Finalizar Interação", command=finalizar_interacao, bg="black", fg="gold")
canvas.create_window(300, 240, window=botao_finalizar)

# Botão para sair e exibir a mensagem final de agradecimento
botao_sair = tk.Button(janela, text="Sair", command=sair, bg="black", fg="gold")
canvas.create_window(300, 340, window=botao_sair)

# Loop principal da aplicação
janela.mainloop()
