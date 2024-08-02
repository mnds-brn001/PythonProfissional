import matplotlib.pyplot as plt

x=[80, 85, 90, 95, 100, 105, 110, 115, 120, 125]
y=[240, 250, 260, 270, 280, 290, 300, 310, 320,330]

font1= {'family':'serif','color':'blue','size':20}
font2={'family':'serif','color':'darkred','size':15}

plt.title("Dados do relógio esportivo", fontdict=font1, loc='left') # loc (localization): left, right, center
plt.xlabel("Pulso Médio", fontdict=font2)
plt.ylabel("Queima de calorias", fontdict=font2)

# plt.grid()
# plt.grid(axis="x")
# plt.grid(axis="y", color="green", linestyle="--", linewidth=0.5) # linewidth: grossura da linha do gráfico
plt.grid(color="green", linestyle="--", linewidth=0.5)

plt.plot(x,y)
plt.show()