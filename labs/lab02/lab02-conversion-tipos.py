# Tendencias e Innovación en Tecnología Agrícola (TEA)

minutos = input("Minutos jugados? ")
valorPorMinuto = input("Valor por Minuto? ")

# se utiliza la conversión de tipo a int
# si no se hace la conversión existirá error porque trata de multiplicar strings
# calculando el valor total de los minutos jugados

total = int(minutos) * int(valorPorMinuto)

# display total
print(total)
