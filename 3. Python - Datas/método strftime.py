import datetime

x = datetime.datetime(2018, 6, 1)

print(x)

y = x.strftime("%B")
print(y)
#print(x.strftime("%B"))




"""
Diretivas |
%a : Dia da semana abreviado
%A: Dia da semana cheio
%w: Dia da semana em decimal 0,1,2 ... 6
%d: Dia do mês com um zero a esquerda 01,02,03 ... 31
%b: Nome do mês abreviado
%B: Nome do mês completo
%m: Mês númerico com zero, 01,02, ... ,12
%y: Ano sem o século com zero a esquerda 00, 01, 15, ... 24
%Y: Ano com o século e numero decimal, 0001, 0002, 2013,2024 ...
%H: Hora (24horas)
%I: Hora(12horas)
%p: Equivalente local a AM ou PM
%M: Minutos em decimal com zero a esquerda 01,02 ,03, 09, 10, 11. ..
%S: Segundos com zero a esquerda em formato decimal 01,02, 03 ,09, 11 ...
%f: Microssegundos como numeros decimais com até 6 digitos de zero a esquerda 000000, 000001, 000002 ...
%Z: Nome do Fuso Horario
%j: Dia do ANO com até 2 zeros a esquerda 001, 011, 210, 365...
%U: Número da semana do ano(Domingo como primeiro dia da semana) 00, 01, 02, .. ,53
%W: Número da semana do ano(Segundo como o primeiro dia da seman) 00, 01, 02, ..., 53
%c: Representação apropriada da data e da hora local
%x: Representação apropriada da Data local
%X: Representação apropriada do Horário local
"""
