import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Gerenciador de Geometria")
root.geometry("400x200+650+300")

# Exemplo de Grid
# Coluna: |    Linhas: --  Células: (x,x)
# (0,0) (1,0) (2,0)

# (0,1) (1,1) (2,1)

# (0,2) (1,2) (2,2)

# (0,3) (1,3) (2,3)

# widget.grid(**options)
# widget.grid(column, row, sticky, padx, pady, ipadx, ipady)



root.mainloop()


# O método grid() possui os seguintes parâmetros:
# column     : O índice da coluna onde você deseja colocar o widget.
# row        : O índice da linha onde você deseja colocar o widget.
# rowspan    : Defina o número de linhas adjacentes que o widget pode abranger.
# columnspan : Defina o número de colunas adjacentes que o widget pode abranger.
# sticky     : Se a célula for maior do que o widget, a stickopção especifica em qual lado o widget deve ficar e como distribuir qualquer espaço extra dentro da célula que não seja ocupado pelo widget em seu tamanho original.
# padx       : Adicione preenchimento externo acima e abaixo do widget.
# pady       : Adicione preenchimento externo à esquerda e à direita do widget.
# ipadx      : Adicione preenchimento interno dentro do widget dos lados esquerdo e direito.
# ipady      : Adicione preenchimento interno dentro do widget nas partes superior e inferior.

# O valor de sticky tem os seguintes valores válidos:
# N  : Norte ou Centro Superior
# S  : Sul ou Centro Inferior
# E  : Leste ou Centro Direito
# W  : Oeste ou Esquerda Centro
# NW : Noroeste ou Esquerda Superior
# NE : Nordeste ou canto superior direito
# SE : Sudeste ou Inferior Direito
# SW : Sudoeste ou Inferior Esquerdo
# NS : NS estica o widget verticalmente. No entanto, ele deixa o widget centralizado horizontalmente.
# EW : W estica o widget horizontalmente. No entanto, ele deixa o widget centralizado verticalmente.