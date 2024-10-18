from tkinter import *

def contador_de_faltas(dias_letivos, faltas, aulas_por_dia):
    faltas_total = int(faltas/aulas_por_dia)
    porcentagem =  int(dias_letivos * 0.25)

    if faltas_total > porcentagem:
        return f"Confira os dados, com esses você está reprovada"
    else:
        final = porcentagem - faltas_total
        return f"Você ainda pode faltar: {final} dias"

def get_aulas_por_dia():
    return int(campo_texto_3.get())

def get_dias_letivos():
    return int(campo_texto.get())

def get_faltas():
    return int(campo_texto_2.get())

def mostrar_resultado():
    dias = get_dias_letivos()
    faltas = get_faltas()
    aulas_dia = get_aulas_por_dia()
    resultado = contador_de_faltas(dias, faltas, aulas_dia)
    texto_faltas.config(text=resultado)


janela = Tk()
janela.title("Contador de Notas")
janela.geometry("400x400")

texto_orientacao = Label(janela, text="Insira os dias letivos")
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

campo_texto = Entry(janela)
campo_texto.grid(column=0, row=1, padx=10, pady=10)

texto_orientacao_2 = Label(janela, text="Insira as faltas")
texto_orientacao_2.grid(column=0, row=2, padx=10, pady=10)

campo_texto_2 = Entry(janela)
campo_texto_2.grid(column=0, row=3, padx=10, pady=10)

texto_orientacao_3 = Label(janela, text="Insira a quantidade de aulas por dia")
texto_orientacao_3.grid(column=0, row=4, padx=10, pady=10)

campo_texto_3 = Entry(janela)
campo_texto_3.grid(column=0, row=5, padx=10, pady=10)

botao = Button(janela, text="resultado", command=mostrar_resultado)
botao.grid(column=0,row=6, padx=10, pady=10)

texto_faltas = Label(janela, text=" ")
texto_faltas.grid(column=0, row=7, padx=10, pady=10)

janela.mainloop()

