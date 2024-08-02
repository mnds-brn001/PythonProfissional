import matplotlib.pyplot as plt

font1= {'family':'Arial', 'color': 'blue'}
font2= {'family':'serif','color':'darkred'}

# plot 1:
x= [0, 1, 2, 3]
y= [3, 8, 1, 10]
plt.subplot(1,2,1)
plt.title("Vendas", fontdict=font1)
plt.plot(x,y)

# plot 2:
x= [0, 1, 2, 3]
y= [10, 20, 30, 40]
plt.subplot(1,2,2)
plt.title("Renda", fontdict=font1)
plt.plot(x,y)

plt.suptitle("Minha Loja", fontdict=font2)
plt.show()